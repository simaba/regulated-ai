# Practitioner Mapping to NIST AI RMF

This is a practical cross-reference for organizing the starter kit. It is not an official NIST mapping, assessment, or endorsement. Verify current authoritative NIST material and organization-specific obligations before relying on it.

| AI RMF function | Starter-kit artifacts | Practical use |
|---|---|---|
| Govern | `governance/ai-governance-policy.md`, `governance/roles-and-responsibilities.md`, `governance/model-inventory.md` | define accountability, decision rights, inventory ownership, and review cadence |
| Map | `risk/risk-taxonomy.yaml`, `risk/risk-assessment-template.md`, `risk/risk-register.md` | document intended use, affected parties, context, hazards, assumptions, and residual risk |
| Measure | `model-cards/model-card-template.md`, `release/release-checklist.yaml`, `release/release-readiness-report.md` | record evaluation evidence, performance limits, test coverage, and readiness gaps |
| Manage | `release/deployment-approval.md`, `incident/incident-response-playbook.md`, `incident/escalation-matrix.md` | decide, monitor, respond, rollback, and improve |

## Mapping discipline

- Keep a link from each claimed control to a concrete artifact, owner, and review status.
- Record gaps as gaps; do not use a template field or completed checkbox as evidence by itself.
- Revisit the mapping when the intended use, risk tier, model/tool configuration, or applicable requirements change.
