# How to Use This Template

This repository is a starter kit. It should be copied, customized, and connected to your own governance and release workflow.

It is not legal advice, compliance certification, or a substitute for formal safety, privacy, legal, or regulatory review.

## Recommended first hour

After creating a repository from this template:

1. Replace placeholder organization names in `governance/ai-governance-policy.md`.
2. Name the business owner, technical owner, and governance owner in `governance/roles-and-responsibilities.md`.
3. Add your first AI system to `governance/model-inventory.md`.
4. Complete a first-pass risk assessment using `risk/risk-assessment-template.md`.
5. Update `release/release-checklist.yaml` for your risk tier and deployment environment.
6. Review the incident escalation path in `incident/escalation-matrix.md`.

## Recommended first week

Within the first week, aim to have:

- one completed model inventory entry
- one completed risk assessment
- one release checklist configuration
- one model card draft
- one incident response owner
- one release gate decision record

## What to customize first

| File | Why it matters |
|---|---|
| `governance/ai-governance-policy.md` | defines what AI governance means for your team |
| `governance/roles-and-responsibilities.md` | prevents unclear ownership |
| `risk/risk-taxonomy.yaml` | aligns risk categories to your industry and use cases |
| `release/release-checklist.yaml` | translates governance expectations into release controls |
| `incident/escalation-matrix.md` | defines what happens when something goes wrong |
| `model-cards/model-card-template.md` | standardizes system documentation |

## Risk-tiering guidance

| Tier | Use when | Minimum release expectation |
|---|---|---|
| Low | internal, reversible, limited user impact | technical review and basic monitoring |
| Medium | customer-facing or operationally important | governance review, risk assessment, rollback plan |
| High | regulated, safety-adjacent, hard to reverse, or high-impact | legal/compliance review, human oversight, formal sign-off, incident plan |

## Suggested workflow

```text
Intake → Risk assessment → Model card draft → Release checklist → Release gate review → Monitoring → Improvement review
```

For broader operating-model guidance, see `governance-playbook`.
For a release lifecycle decision artifact, see `release-governance`.
For CLI-based readiness validation, see `release-checklist`.

## Public example data rule

If this repository is public or shared externally, use only generic examples.

Do not include:

- customer data
- employee data
- confidential vendor or supplier details
- internal approval chains
- unreleased product names
- proprietary model performance results
- legal advice presented as final compliance interpretation

## Maintenance checklist

Review this repository at least quarterly:

- [ ] owner names are current
- [ ] risk taxonomy still matches actual use cases
- [ ] release checklist matches current gate expectations
- [ ] incident contacts and SLAs are current
- [ ] model inventory is complete
- [ ] lessons learned from incidents or monitoring reviews are reflected in templates
