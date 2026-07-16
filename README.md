# Regulated AI Starter Repository

[![Use this template](https://img.shields.io/badge/Use%20this%20template-2ea44f?style=flat-square&logo=github)](https://github.com/simaba/regulated-ai/generate)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)

A GitHub template for organizing AI governance, evidence, release decisions, risk records, incident preparation, and model documentation in high-accountability environments.

The repository provides a starting structure, not a control system. Folder names, completed documents, true/false fields, or a passing CI job do not establish safety, compliance, fairness, production readiness, or release approval.

## What changed from a typical starter kit

The release configuration is built around decision propositions and evidence rather than universal thresholds and sector checkboxes.

It deliberately avoids claims such as:

- every classification system should meet the same accuracy or F1 target;
- a single disparate-impact ratio demonstrates fairness;
- “bias evaluation complete” proves an acceptable outcome;
- a legal or security review can be represented meaningfully by one boolean;
- healthcare, finance, insurance, or government systems share one fixed gate list;
- passing unit tests and documenting rollback make a system ready to release.

The right evidence depends on the actual use, people, data, authority, consequences, obligations, and operating environment.

## Start here

| Artifact | Use it for |
|---|---|
| [`docs/how-to-use-this-template.md`](docs/how-to-use-this-template.md) | adopting the repository without copying generic controls blindly |
| [`release/release-checklist.yaml`](release/release-checklist.yaml) | defining a scoped release decision, gates, evidence, conditions, and change triggers |
| [`examples/sample-release-checklist.yaml`](examples/sample-release-checklist.yaml) | fictional evidence-based conditional-pilot example |
| [`docs/release-config-validation.md`](docs/release-config-validation.md) | validator scope and decision-coherence rules |
| [`risk/risk-assessment-template.md`](risk/risk-assessment-template.md) | system-specific risk and evidence review |
| [`governance/model-inventory.md`](governance/model-inventory.md) | adapting inventory fields for deployed systems and ownership |
| [`incident/incident-response-playbook.md`](incident/incident-response-playbook.md) | defining incident authority and response |
| [`model-cards/model-card-template.md`](model-cards/model-card-template.md) | recording system and model information where a model card is useful |

## Repository structure

```text
regulated-ai/
├── docs/               adoption and validation guidance
├── examples/           fictional public-safe artifacts
├── governance/         policy, roles, inventory, and practitioner mappings
├── risk/               taxonomy, register, and assessment template
├── release/            evidence-based release decision artifacts
├── incident/           incident, escalation, and response templates
├── model-cards/        model-card starter structure
├── tools/              narrow structural and semantic validators
├── tests/              validator tests
└── .github/workflows/  CI checks for the starter artifacts
```

## Adoption sequence

### 1. Define scope and authoritative sources

Before filling templates, record:

- systems and lifecycle stages covered;
- intended and prohibited uses;
- user and affected populations;
- data, model, tool, permission, and environment boundaries;
- actual internal policies and decision authorities;
- official legal, regulatory, standards, and contractual sources that apply;
- information that must remain private.

Remove irrelevant directories rather than preserving them for appearance.

### 2. Assign decision and control ownership

Distinguish:

- product or use-case owner;
- technical, data, model, tool, and platform owners;
- control owners;
- independent reviewers;
- release and residual-risk decision owner;
- incident and remediation owner;
- correction, appeal, or redress owner where relevant.

A named person without authority or resources is not effective accountability.

### 3. Replace the release propositions

Edit [`release/release-checklist.yaml`](release/release-checklist.yaml). Each gate should be a question whose answer changes the scoped decision.

For example:

```yaml
metadata:
  project: "Fictional Catalog Assistant"
  version: "0.3.0-pilot"
  environment: "bounded-internal-pilot"
  decision_scope: "60 trained users; public records; read and draft tools only"
  decision_owner: "Fictional Pilot Sponsor"
  evidence_cutoff: "2026-09-30"

decision:
  outcome: "release_with_conditions"
  blockers: []
  required_actions:
    - "Complete the confirmatory legacy-record sample before expansion."
  conditions:
    - "Keep source-system tools read-only through the pilot."
  evidence_gaps:
    - "Rare legacy records remain under-sampled."
  residual_risks:
    - "Staff may over-trust fluent draft rationales."

gates:
  - id: "AUTH-001"
    question: "Are identity, authorization, confirmation, and action boundaries enforced for the reviewed scope?"
    hard_gate: true
    status: "pass"
    evidence:
      - "evidence/fictional-permission-test.json"
    owner: "Fictional Platform Owner"
    limitation: "Internal pilot configuration only."
```

The example is intentionally fictional. Replace the questions and evidence model with organization-specific requirements.

### 4. Validate structure and decision coherence

```bash
python -m pip install pyyaml
python -m unittest discover -s tests -v
python tools/validate_release_config.py \
  release/release-checklist.yaml \
  --mode template
python tools/validate_release_config.py \
  examples/sample-release-checklist.yaml \
  --mode ready
```

The validator checks structure and a small set of rules:

- no release with blockers or unresolved hard gates;
- no unconditional release with conditions or required actions;
- conditional release has a condition or required action;
- pass / not-applicable gates cite evidence;
- not-applicable gates include scoped rationale;
- deferred decisions identify evidence gaps;
- identifiers are unique and required fields are populated.

It does not verify the evidence, gate selection, risk acceptance, or legal and operational sufficiency.

### 5. Connect the artifacts

The repository becomes useful when records reference each other:

```text
inventory and context
        ↓
risk and impact assessment
        ↓
evaluation and control evidence
        ↓
release decision and conditions
        ↓
monitoring, incident, correction, and review
        ↓
change, renewal, rollback, or retirement
```

Avoid duplicating evidence into several documents without provenance. Link the authoritative record and state its version and freshness.

### 6. Define change triggers

A decision should be revisited after material changes to:

- model, provider, prompt, routing, retrieval, or policy;
- data, population, language, geography, or use case;
- tools, permissions, identities, and external action authority;
- infrastructure, region, or supplier;
- evaluator, threshold, rubric, or test set;
- applicable policy or obligation;
- incidents and newly discovered failure classes;
- conditions, exceptions, or owner authority.

## Relationship to NIST AI RMF

The directory structure and templates may support internal work related to Govern, Map, Measure, and Manage. They do not implement those functions by existing.

| Function | Possible repository support | Evidence still required outside the template |
|---|---|---|
| Govern | ownership, policy, inventory, decisions | actual authority, operating process, competence, culture |
| Map | context and risk templates | validated system and affected-population analysis |
| Measure | evidence and gate records | valid evaluations, control tests, uncertainty, outcomes |
| Manage | decision, incident, rollback, and follow-through | effective treatment, response capability, accepted residual risk |

Use official NIST sources as authoritative and verify practitioner mappings.

## Publication safety

A public copy must not contain real:

- customer, patient, employee, applicant, citizen, or user data;
- confidential vendor, pricing, contract, architecture, roadmap, prompt, or model result;
- internal decision rights, approval chains, risk assessments, incidents, logs, endpoints, credentials, or tool manifests;
- sensitive regulatory or legal advice;
- examples derived from internal work by changing only names.

Use invented organizations, `.example` or `.test` contact domains, synthetic data, and scenarios clearly separate from employment history.

## Quality standard

A useful customization should add:

- a decision-relevant proposition;
- traceable evidence and limitations;
- an accountable owner with authority;
- explicit condition, exception, or residual-risk semantics;
- an enforceable monitoring or stop trigger;
- a tested incident, containment, rollback, correction, or retirement path;
- an organization-specific source or requirement.

Avoid adding a document or checkbox merely because it is common in governance repositories.

## Maturity and scope

This is a starter template with working structural and decision-coherence validation. It is not a governance platform, formal control library, compliance assessment, legal opinion, safety case, or release authority.

## Related repositories

| Repository | Distinct role |
|---|---|
| [`governance-playbook`](https://github.com/simaba/governance-playbook) | enterprise governance operating model |
| [`release-governance`](https://github.com/simaba/release-governance) | release evidence and decision semantics |
| [`release-checklist`](https://github.com/simaba/release-checklist) | packaged configuration validator |
| [`nist-rmf-guide`](https://github.com/simaba/nist-rmf-guide) | practitioner navigation and evidence planning |
| [`agent-eval`](https://github.com/simaba/agent-eval) | evaluation validity and reporting |

---

*Maintained by [Sima Bagheri](https://github.com/simaba).*
