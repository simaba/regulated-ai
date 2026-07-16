from __future__ import annotations

import copy
import unittest

from tools.validate_release_config import validate


BASE = {
    "metadata": {
        "project": "Fictional Assistant",
        "version": "0.1.0",
        "environment": "internal-pilot",
        "decision_scope": "20 internal users; read-only tools",
        "decision_owner": "Fictional Sponsor",
        "evidence_cutoff": "2026-09-30",
    },
    "decision": {
        "outcome": "release_with_conditions",
        "blockers": [],
        "required_actions": ["Complete the confirmatory sample before expansion."],
        "conditions": ["Keep tools read-only."],
        "evidence_gaps": [],
        "residual_risks": ["Users may over-trust fluent drafts."],
    },
    "gates": [
        {
            "id": "AUTH-001",
            "question": "Is write authority disabled?",
            "hard_gate": True,
            "status": "pass",
            "evidence": ["evidence/auth-test.json"],
            "owner": "Fictional Platform Owner",
            "limitation": "Pilot scope only.",
        },
        {
            "id": "EVAL-001",
            "question": "Does the evidence support the bounded pilot?",
            "hard_gate": False,
            "status": "partial",
            "evidence": ["evidence/evaluation.md"],
            "owner": "Fictional Evaluation Owner",
            "limitation": "Rare slice remains small.",
        },
    ],
}


class ValidateReleaseDecisionTests(unittest.TestCase):
    def test_valid_conditional_release(self) -> None:
        self.assertEqual(validate(copy.deepcopy(BASE), "ready"), [])

    def test_release_rejects_conditions(self) -> None:
        payload = copy.deepcopy(BASE)
        payload["decision"]["outcome"] = "release"
        errors = validate(payload, "ready")
        self.assertIn("release cannot include required_actions or conditions", errors)

    def test_release_rejects_blocker(self) -> None:
        payload = copy.deepcopy(BASE)
        payload["decision"]["blockers"] = ["Unresolved authorization defect"]
        errors = validate(payload, "ready")
        self.assertIn("release_with_conditions cannot include unresolved blockers", errors)

    def test_hard_gate_must_be_resolved_for_release(self) -> None:
        payload = copy.deepcopy(BASE)
        payload["gates"][0]["status"] = "partial"
        errors = validate(payload, "ready")
        self.assertTrue(
            any("unresolved hard gates: AUTH-001" in error for error in errors),
            errors,
        )

    def test_pass_gate_requires_evidence(self) -> None:
        payload = copy.deepcopy(BASE)
        payload["gates"][0]["evidence"] = []
        errors = validate(payload, "ready")
        self.assertIn("gates[0] with status pass must cite evidence", errors)

    def test_not_applicable_requires_rationale(self) -> None:
        payload = copy.deepcopy(BASE)
        payload["gates"][0]["status"] = "not_applicable"
        payload["gates"][0]["limitation"] = ""
        errors = validate(payload, "ready")
        self.assertIn(
            "gates[0] with status not_applicable must explain the scoped rationale in limitation",
            errors,
        )

    def test_defer_requires_evidence_gap(self) -> None:
        payload = copy.deepcopy(BASE)
        payload["decision"]["outcome"] = "defer"
        payload["decision"]["required_actions"] = []
        payload["decision"]["conditions"] = []
        errors = validate(payload, "ready")
        self.assertIn("defer requires at least one evidence gap", errors)

    def test_do_not_release_requires_reason(self) -> None:
        payload = copy.deepcopy(BASE)
        payload["decision"]["outcome"] = "do_not_release"
        payload["decision"]["required_actions"] = []
        payload["decision"]["conditions"] = []
        errors = validate(payload, "ready")
        self.assertIn(
            "do_not_release requires a blocker or an unresolved hard gate",
            errors,
        )

    def test_duplicate_gate_ids_are_rejected(self) -> None:
        payload = copy.deepcopy(BASE)
        payload["gates"].append(copy.deepcopy(payload["gates"][0]))
        errors = validate(payload, "ready")
        self.assertIn("duplicate gate id: AUTH-001", errors)

    def test_ready_mode_rejects_placeholders(self) -> None:
        payload = copy.deepcopy(BASE)
        payload["metadata"]["decision_owner"] = "[TBD]"
        errors = validate(payload, "ready")
        self.assertIn("metadata.decision_owner contains a placeholder", errors)


if __name__ == "__main__":
    unittest.main()
