# AI Incident Response Playbook

## Purpose

Use this playbook to coordinate investigation, containment, communication, recovery, and learning when an AI system causes or may cause material harm, privacy/security exposure, unsafe behavior, significant reliability degradation, or policy/control failure.

## 1. Detect and triage

- Record time, reporter, system/version, environment, and initial impact.
- Preserve relevant evidence according to approved retention and access controls.
- Classify the incident as low, medium, or high severity using the organization's incident policy.
- Identify whether immediate containment is needed: disable a tool, restrict a route, pause deployment, switch to manual review, or rollback.

## 2. Contain and protect

- Stop or limit unsafe, unauthorized, or unreliable behavior.
- Protect affected users, data, and downstream systems.
- Do not alter or delete evidence needed for investigation.
- Record each containment decision, actor, time, and rationale.

## 3. Investigate

| Question | Record |
|---|---|
| What happened? | observable symptoms, timeline, affected scope |
| Which version was active? | model, prompt/configuration, retrieval, tool, and deployment identifiers |
| Why did controls not prevent it? | missing, failed, bypassed, or insufficient controls |
| Who is affected? | users, customers, systems, or stakeholders, using approved privacy-safe detail |
| What evidence supports conclusions? | logs, evaluations, approvals, monitoring, and human review notes |

## 4. Recover and decide

- Define the recovery condition and accountable owner.
- Verify a rollback, fix, or containment control before restoring normal operation.
- Reassess risk tier and release readiness if the incident changes intended use, risk assumptions, model/tool configuration, or monitoring requirements.

## 5. Learn and improve

- Create a factual post-incident record using `incident/incident-report-template.md`.
- Add corrective actions with owners and review dates.
- Update the risk register, model inventory, evaluation suite, release checklist, and playbook when the incident exposes a systemic gap.
