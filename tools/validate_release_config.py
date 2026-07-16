#!/usr/bin/env python3
"""Validate an evidence-based AI release decision configuration.

The validator checks structure and a small set of decision-coherence rules. It
cannot determine whether evidence is valid, a gate is appropriate, a residual
risk is acceptable, or a deployment is safe or compliant.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

import yaml


REQUIRED_TOP_LEVEL = ("metadata", "decision", "gates")
REQUIRED_METADATA = (
    "project",
    "version",
    "environment",
    "decision_scope",
    "decision_owner",
    "evidence_cutoff",
)
ALLOWED_OUTCOMES = {
    "release",
    "release_with_conditions",
    "hold",
    "do_not_release",
    "defer",
}
ALLOWED_GATE_STATUS = {
    "pass",
    "fail",
    "partial",
    "not_tested",
    "not_applicable",
}
PLACEHOLDER = re.compile(r"(?:\[?TBD\]?|YOUR_|REPLACE_|<[^>]+>)", re.IGNORECASE)


def _load(path: str | Path) -> dict[str, Any]:
    source = Path(path)
    try:
        payload = yaml.safe_load(source.read_text(encoding="utf-8"))
    except OSError as exc:
        raise ValueError(f"could not read {source}: {exc}") from exc
    except yaml.YAMLError as exc:
        raise ValueError(f"invalid YAML in {source}: {exc}") from exc
    if not isinstance(payload, dict):
        raise ValueError(f"{source} must contain a YAML mapping at the top level")
    return payload


def _is_nonempty_text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _is_placeholder(value: Any) -> bool:
    return not _is_nonempty_text(value) or bool(PLACEHOLDER.search(str(value)))


def _require_list(mapping: dict[str, Any], key: str, errors: list[str]) -> list[Any]:
    value = mapping.get(key, [])
    if not isinstance(value, list):
        errors.append(f"decision.{key} must be a list")
        return []
    return value


def _validate_gate(gate: Any, index: int, mode: str, errors: list[str]) -> None:
    prefix = f"gates[{index}]"
    if not isinstance(gate, dict):
        errors.append(f"{prefix} must be a mapping")
        return

    required = ("id", "question", "hard_gate", "status", "evidence", "owner")
    for field in required:
        if field not in gate:
            errors.append(f"{prefix} is missing required field: {field}")

    gate_id = gate.get("id")
    question = gate.get("question")
    hard_gate = gate.get("hard_gate")
    status = gate.get("status")
    evidence = gate.get("evidence")
    owner = gate.get("owner")
    limitation = gate.get("limitation")

    if gate_id is not None and not _is_nonempty_text(gate_id):
        errors.append(f"{prefix}.id must be non-empty text")
    if question is not None and not _is_nonempty_text(question):
        errors.append(f"{prefix}.question must be non-empty text")
    if hard_gate is not None and not isinstance(hard_gate, bool):
        errors.append(f"{prefix}.hard_gate must be true or false")
    if status is not None and status not in ALLOWED_GATE_STATUS:
        errors.append(
            f"{prefix}.status must be one of: {', '.join(sorted(ALLOWED_GATE_STATUS))}"
        )
    if evidence is not None and not isinstance(evidence, list):
        errors.append(f"{prefix}.evidence must be a list of evidence references")
    elif isinstance(evidence, list) and any(not _is_nonempty_text(item) for item in evidence):
        errors.append(f"{prefix}.evidence entries must be non-empty text")
    if owner is not None and not _is_nonempty_text(owner):
        errors.append(f"{prefix}.owner must be non-empty text")

    if mode == "ready":
        if _is_placeholder(gate_id):
            errors.append(f"{prefix}.id contains a placeholder")
        if _is_placeholder(question):
            errors.append(f"{prefix}.question contains a placeholder")
        if _is_placeholder(owner):
            errors.append(f"{prefix}.owner contains a placeholder")
        if status in {"pass", "not_applicable"} and not evidence:
            errors.append(f"{prefix} with status {status} must cite evidence")
        if status == "not_applicable" and not _is_nonempty_text(limitation):
            errors.append(
                f"{prefix} with status not_applicable must explain the scoped rationale in limitation"
            )


def validate(payload: dict[str, Any], mode: str) -> list[str]:
    """Return structural and decision-coherence errors."""
    errors: list[str] = []

    missing = [key for key in REQUIRED_TOP_LEVEL if key not in payload]
    if missing:
        return [f"missing required sections: {', '.join(missing)}"]

    metadata = payload.get("metadata")
    decision = payload.get("decision")
    gates = payload.get("gates")

    if not isinstance(metadata, dict):
        errors.append("metadata must be a mapping")
        metadata = {}
    if not isinstance(decision, dict):
        errors.append("decision must be a mapping")
        decision = {}
    if not isinstance(gates, list):
        errors.append("gates must be a list")
        gates = []

    missing_metadata = [key for key in REQUIRED_METADATA if key not in metadata]
    if missing_metadata:
        errors.append(f"missing metadata fields: {', '.join(missing_metadata)}")

    for field in REQUIRED_METADATA:
        if field in metadata and not _is_nonempty_text(metadata[field]):
            errors.append(f"metadata.{field} must be non-empty text")
        if mode == "ready" and field in metadata and _is_placeholder(metadata[field]):
            errors.append(f"metadata.{field} contains a placeholder")

    outcome = decision.get("outcome")
    if outcome not in ALLOWED_OUTCOMES:
        errors.append(
            f"decision.outcome must be one of: {', '.join(sorted(ALLOWED_OUTCOMES))}"
        )

    blockers = _require_list(decision, "blockers", errors)
    required_actions = _require_list(decision, "required_actions", errors)
    conditions = _require_list(decision, "conditions", errors)
    evidence_gaps = _require_list(decision, "evidence_gaps", errors)
    residual_risks = _require_list(decision, "residual_risks", errors)

    for key, values in (
        ("blockers", blockers),
        ("required_actions", required_actions),
        ("conditions", conditions),
        ("evidence_gaps", evidence_gaps),
        ("residual_risks", residual_risks),
    ):
        if any(not _is_nonempty_text(item) for item in values):
            errors.append(f"decision.{key} entries must be non-empty text")

    ids: set[str] = set()
    for index, gate in enumerate(gates):
        _validate_gate(gate, index, mode, errors)
        if isinstance(gate, dict) and _is_nonempty_text(gate.get("id")):
            gate_id = str(gate["id"])
            if gate_id in ids:
                errors.append(f"duplicate gate id: {gate_id}")
            ids.add(gate_id)

    if mode == "template":
        return errors

    if not gates:
        errors.append("ready mode requires at least one gate")

    unresolved_hard_gates = [
        str(gate.get("id", f"gates[{index}]"))
        for index, gate in enumerate(gates)
        if isinstance(gate, dict)
        and gate.get("hard_gate") is True
        and gate.get("status") not in {"pass", "not_applicable"}
    ]

    if outcome in {"release", "release_with_conditions"}:
        if blockers:
            errors.append(f"{outcome} cannot include unresolved blockers")
        if unresolved_hard_gates:
            errors.append(
                f"{outcome} cannot proceed with unresolved hard gates: "
                + ", ".join(unresolved_hard_gates)
            )

    if outcome == "release" and (required_actions or conditions):
        errors.append("release cannot include required_actions or conditions")

    if outcome == "release_with_conditions" and not (required_actions or conditions):
        errors.append(
            "release_with_conditions requires at least one required action or condition"
        )

    if outcome == "defer" and not evidence_gaps:
        errors.append("defer requires at least one evidence gap")

    if outcome == "do_not_release" and not (blockers or unresolved_hard_gates):
        errors.append(
            "do_not_release requires a blocker or an unresolved hard gate"
        )

    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate a regulated-AI starter release decision configuration."
    )
    parser.add_argument("path")
    parser.add_argument(
        "--mode",
        choices=("template", "ready"),
        default="template",
        help=(
            "template checks structure; ready also rejects placeholders and "
            "checks selected decision semantics"
        ),
    )
    args = parser.parse_args(argv)

    try:
        errors = validate(_load(args.path), args.mode)
    except ValueError as exc:
        parser.error(str(exc))

    if errors:
        print("Release decision configuration is invalid:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Release decision configuration is valid for {args.mode} mode.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
