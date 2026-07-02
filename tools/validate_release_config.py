#!/usr/bin/env python3
"""Validate release-checklist YAML as either a template or a populated example.

This helper intentionally does not certify a deployment. It checks only the
small, explicit contract documented by this starter repository: required
structure, supported metadata, and a minimum set of configured gate values for
an illustrative ready-to-review example.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

import yaml


REQUIRED_TOP_LEVEL = ("metadata", "model_validation", "governance", "infrastructure")
REQUIRED_METADATA = (
    "project",
    "version",
    "environment",
    "regulated_industry",
    "risk_classification",
)
ALLOWED_RISKS = {"low", "medium", "high"}
ALLOWED_INDUSTRIES = {"general", "healthcare", "finance", "insurance", "government"}

REQUIRED_GATES_BY_RISK = {
    "low": (
        "governance.approvals.technical_review",
        "infrastructure.testing.unit_tests_passing",
    ),
    "medium": (
        "model_validation.performance.bias_evaluation_complete",
        "governance.approvals.technical_review",
        "governance.documentation.risk_assessment_complete",
        "infrastructure.testing.unit_tests_passing",
        "infrastructure.rollback.rollback_plan_documented",
    ),
    "high": (
        "model_validation.performance.bias_evaluation_complete",
        "governance.approvals.technical_review",
        "governance.approvals.ai_governance_review",
        "governance.approvals.legal_review",
        "governance.documentation.model_card_complete",
        "governance.documentation.risk_assessment_complete",
        "infrastructure.testing.unit_tests_passing",
        "infrastructure.testing.security_scan_passed",
        "infrastructure.rollback.rollback_plan_documented",
        "incident_readiness.runbook_complete",
    ),
}
INDUSTRY_GATES = {
    "healthcare": ("governance.regulatory.hipaa_assessment_complete",),
    "finance": ("governance.regulatory.sr_11_7_compliance",),
    "insurance": ("governance.regulatory.sr_11_7_compliance",),
    "government": ("governance.approvals.legal_review",),
}


def _nested(mapping: dict[str, Any], path: str) -> Any:
    value: Any = mapping
    for part in path.split("."):
        if not isinstance(value, dict):
            return None
        value = value.get(part)
    return value


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


def validate(payload: dict[str, Any], mode: str) -> list[str]:
    """Return structural or readiness errors for a release configuration."""
    errors: list[str] = []
    missing = [key for key in REQUIRED_TOP_LEVEL if key not in payload]
    if missing:
        errors.append(f"missing required sections: {', '.join(missing)}")
        return errors

    for section in REQUIRED_TOP_LEVEL:
        if not isinstance(payload[section], dict):
            errors.append(f"{section} must be a mapping")

    metadata = payload.get("metadata", {})
    if not isinstance(metadata, dict):
        return errors + ["metadata must be a mapping"]
    missing_metadata = [key for key in REQUIRED_METADATA if not metadata.get(key)]
    if missing_metadata:
        errors.append(f"missing metadata fields: {', '.join(missing_metadata)}")
        return errors

    risk = str(metadata["risk_classification"]).lower()
    industry = str(metadata["regulated_industry"]).lower()
    if risk not in ALLOWED_RISKS:
        errors.append(f"metadata.risk_classification must be one of: {', '.join(sorted(ALLOWED_RISKS))}")
    if industry not in ALLOWED_INDUSTRIES:
        errors.append(f"metadata.regulated_industry must be one of: {', '.join(sorted(ALLOWED_INDUSTRIES))}")
    if errors or mode == "template":
        return errors

    gate_paths = (*REQUIRED_GATES_BY_RISK[risk], *INDUSTRY_GATES.get(industry, ()))
    for path in gate_paths:
        value = _nested(payload, path)
        if value is not True:
            errors.append(f"required readiness gate is not true: {path}")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate a regulated-AI starter release configuration."
    )
    parser.add_argument("path")
    parser.add_argument(
        "--mode",
        choices=("template", "ready"),
        default="template",
        help="template checks structure; ready also requires the stated minimum gates",
    )
    args = parser.parse_args(argv)

    try:
        errors = validate(_load(args.path), args.mode)
    except ValueError as exc:
        parser.error(str(exc))

    if errors:
        print("Release configuration is invalid:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Release configuration is valid for {args.mode} mode.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
