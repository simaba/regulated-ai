# Regulated AI Starter Kit

[![Use this template](https://img.shields.io/badge/Use%20this%20template-2ea44f?style=for-the-badge&logo=github)](https://github.com/simaba/regulated-ai/generate)
[![NIST AI RMF](https://img.shields.io/badge/NIST%20AI%20RMF-Informed-0055A4?style=flat-square)](https://www.nist.gov/system/files/documents/2023/01/26/AI%20RMF%201.0.pdf)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![Maintained](https://img.shields.io/badge/Maintained-yes-green.svg?style=flat-square)](https://github.com/simaba/regulated-ai)

A GitHub template repository for governance documentation, release-readiness artifacts, and deployment-readiness structure in regulated or high-accountability AI environments.

## Maturity

This is a **template repository**. It is intended to help teams start with better structure, not to certify that an AI system is safe, compliant, production-ready, or approved for release.

## Purpose

Use this template to create a starting repository with:

- NIST AI RMF-informed governance documentation
- release-readiness configuration stubs
- a structured risk taxonomy with practitioner mappings to NIST AI RMF and EU AI Act concepts
- CI/CD validation workflows
- incident-response playbook stubs
- model-card templates
- generic sample artifacts that show how to fill the templates safely

## Intended use cases

This starter kit is most relevant for teams deploying AI in:

- **Healthcare**: clinical decision support, diagnostic AI, or patient risk scoring
- **Financial services**: credit scoring, fraud detection, or model-assisted decisions
- **Insurance**: underwriting AI, claims automation, or risk assessment
- **Government**: benefits eligibility, document processing, or public-facing AI
- other high-accountability domains where governance, traceability, and release discipline matter

## Repository structure

```text
regulated-ai/
├── docs/
│   └── how-to-use-this-template.md
├── examples/
│   ├── sample-release-checklist.yaml
│   └── sample-risk-register.md
├── governance/
│   ├── ai-governance-policy.md
│   ├── roles-and-responsibilities.md
│   ├── model-inventory.md
│   └── nist-rmf-mapping.md
├── risk/
│   ├── risk-register.md
│   ├── risk-taxonomy.yaml
│   └── risk-assessment-template.md
├── release/
│   ├── release-checklist.yaml
│   ├── release-readiness-report.md
│   └── deployment-approval.md
├── incident/
│   ├── incident-response-playbook.md
│   ├── incident-report-template.md
│   └── escalation-matrix.md
├── model-cards/
│   └── model-card-template.md
└── .github/
    └── workflows/
        ├── validate-release-config.yml
        └── governance-checks.yml
```

## Quick start

### 1. Create your repository from this template

Click **Use this template** and create a new repository such as `acme-ai-governance` or `{team}-ai-deployment-kit`.

### 2. Follow the adoption guide

Start with [`docs/how-to-use-this-template.md`](docs/how-to-use-this-template.md). It explains what to edit in the first hour and first week after creating your copy.

### 3. Customize the governance policy

Edit `governance/ai-governance-policy.md` and replace `[Organization Name]` placeholders with your organization name, decision rights, and internal approval path.

### 4. Configure your release checklist

Edit `release/release-checklist.yaml` to reflect your actual controls, owners, and risk tier. See [`examples/sample-release-checklist.yaml`](examples/sample-release-checklist.yaml) for a generic filled example.

```yaml
metadata:
  project: "Your Project Name"
  version: "1.0.0"
  environment: "production"
  regulated_industry: "healthcare"
  risk_classification: "high"

model_validation:
  performance:
    accuracy_threshold: 0.95
    bias_evaluation_complete: true

governance:
  documentation:
    risk_assessment_complete: true
  approvals:
    technical_review: true
    legal_review: true

infrastructure:
  testing:
    unit_tests_passing: true
  rollback:
    rollback_plan_documented: true
```

### 5. Run the CI validation

Push to any branch to trigger the included GitHub Actions checks.

```bash
git add .
git commit -m "Configure regulated AI starter kit"
git push
```

### 6. Complete your risk assessment

Copy `risk/risk-assessment-template.md` and fill it out for each AI system you are deploying. Use [`examples/sample-risk-register.md`](examples/sample-risk-register.md) as a simple reference for owner, mitigation, and status discipline.

## NIST AI RMF mapping

This starter kit is organized around the four core NIST AI RMF functions:

| Function | Implementation in this kit |
|---|---|
| **Govern** | `governance/` directory for policy, roles, and model inventory |
| **Map** | `risk/` directory for taxonomy and per-system assessments |
| **Measure** | `release/` directory for pre-deployment checks and readiness artifacts |
| **Manage** | `incident/` directory for monitoring, escalation, and response |

This is a practitioner mapping, not an official NIST assessment or endorsement.

## Publication safety

The examples in this repository are intentionally generic. If you use this template in a public or shared repository, do not include customer data, employee data, confidential vendor details, unreleased product names, proprietary model results, internal approval chains, sensitive logs, or real incident details.

## Scope and disclaimer

This repository is shared in a personal capacity. It is not legal advice, compliance certification, regulatory approval, safety certification, or official guidance from NIST, the EU, ISO, or any employer.

References to NIST AI RMF, EU AI Act, release readiness, risk taxonomy, model cards, incident response, or regulated-industry obligations are practitioner mappings and examples. Always verify against official sources and internal requirements before using this template for compliance, safety, or release decisions.

## Related repositories

| Repository | What it adds |
|---|---|
| [governance-playbook](https://github.com/simaba/governance-playbook) | Full governance playbook with broader operating-model guidance |
| [release-checklist](https://github.com/simaba/release-checklist) | CLI validator and stricter release gate logic |
| [release-governance](https://github.com/simaba/release-governance) | Release lifecycle governance framework |
| [nist-rmf-guide](https://github.com/simaba/nist-rmf-guide) | Practitioner guide for implementing NIST AI RMF |
| [ai-prism](https://github.com/simaba/ai-prism) | Curated list of governance tools, frameworks, and references |

## License

MIT License. See [LICENSE](LICENSE).

---

*Maintained by [Sima Bagheri](https://github.com/simaba) · Built for AI teams working in regulated and high-accountability environments.*
