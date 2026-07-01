# Roles and Responsibilities

> Replace bracketed placeholders with organization-specific roles, names, decision rights, and escalation paths. This template is a starting point, not a substitute for legal, regulatory, security, privacy, safety, or employment requirements.

## Role map

| Role | Accountable for | Key decisions | Evidence maintained |
|---|---|---|---|
| Business owner | Intended use, value, user impact, and acceptance of residual business risk | Whether the use case should proceed | use-case brief, benefit assumptions, risk acceptance |
| Technical owner | Architecture, implementation quality, reliability, and change control | Technical readiness and rollback feasibility | design record, test results, release evidence |
| AI/model owner | Model selection, evaluation design, data/model changes, and documented limitations | Evaluation sufficiency and model-change approval | model card, evaluation report, version inventory |
| Risk/governance owner | Risk classification, required controls, decision records, and review cadence | Risk-tier assignment and governance gate recommendation | risk register, gate record, oversight evidence |
| Security/privacy reviewer | Data handling, access boundaries, logging, threat assessment, and incident requirements | Security/privacy conditions or blockers | review record, control evidence, exception record |
| Release owner | Deployment plan, monitoring activation, rollback readiness, and post-release review | Go/no-go execution after approvals | deployment record, runbook, monitoring confirmation |

## Decision rights

- A release recommendation must identify the accountable business, technical, and governance owners.
- A named owner may recommend a decision, but any required security, privacy, legal, safety, or regulatory review remains subject to the organization's approval rules.
- An unresolved blocker must identify an owner, a due date, and the decision authority that can accept or reject the residual risk.

## Escalation triggers

Escalate to the applicable owners when any of the following occurs:

- intended use, user population, autonomy, data source, or tool-permission scope changes materially
- a high-severity evaluation, security, privacy, safety, or compliance finding remains open
- monitoring indicates a material regression, unexpected behavior, or incident
- a release gate is bypassed, deferred, or accepted with conditions

## Review cadence

| Artifact | Owner | Review trigger | Minimum cadence |
|---|---|---|---|
| Model/system inventory | AI/model owner | new system or material change | quarterly |
| Risk register | Risk/governance owner | new risk, incident, or material change | monthly while active |
| Release checklist | Release owner | every release candidate | per release |
| Incident playbook | Security/privacy and release owners | incident, exercise, or control change | semiannual |
