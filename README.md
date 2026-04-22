# Regulated AI Starter Kit

[![Use this template](https://img.shields.io/badge/Use%20this%20template-2ea44f?style=for-the-badge&logo=github)](https://github.com/simaba/regulated-ai/generate)
[![NIST AI RMF](https://img.shields.io/badge/NIST%20AI%20RMF-Aligned-0055A4?style=flat-square)](https://www.nist.gov/system/files/documents/2023/01/26/AI%20RMF%201.0.pdf)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![Maintained](https://img.shields.io/badge/Maintained-yes-green.svg?style=flat-square)](https://github.com/simaba/regulated-ai)

A **GitHub template repository** giving AI teams a running start on governance,
compliance, and deployment readiness for regulated industries.

Click **Use this template** above to create your own copy pre-wired with:

- NIST AI RMF-aligned governance documentation
- Release readiness configuration stubs
- A structured risk taxonomy mapped to NIST AI RMF and EU AI Act concepts
- CI/CD validation workflows
- Incident response playbook stubs
- Model card templates

---

## Who this is for

Teams deploying AI in:
- **Healthcare** for clinical decision support, diagnostic AI, or patient risk scoring
- **Financial Services** for credit scoring, fraud detection, or model-assisted decisions
- **Insurance** for underwriting AI, claims automation, or risk assessment
- **Government** for benefits eligibility, document processing, or public-facing AI

---

## Repository structure

```text
regulated-ai/
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

---

## Quick start

### 1. Create your repository from this template

Click **Use this template** and create a new repository such as `acme-ai-governance` or `{team}-ai-deployment-kit`.

### 2. Customize the governance policy

Edit `governance/ai-governance-policy.md` and replace `[Organization Name]` placeholders with your organization name, decision rights, and internal approval path.

### 3. Configure your release checklist

Edit `release/release-checklist.yaml` to reflect your actual controls, owners, and risk tier.

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

### 4. Run the CI validation

Push to any branch to trigger the included GitHub Actions checks.

```bash
git add .
git commit -m "Configure regulated AI starter kit"
git push
```

### 5. Complete your risk assessment

Copy `risk/risk-assessment-template.md` and fill it out for each AI system you are deploying. The template is designed to make risk assumptions, evidence gaps, and ownership explicit.

---

## NIST AI RMF alignment

This starter kit is organized around the four core NIST AI RMF functions:

| Function | Implementation in this kit |
|---|---|
| **Govern** | `governance/` directory for policy, roles, and model inventory |
| **Map** | `risk/` directory for taxonomy and per-system assessments |
| **Measure** | `release/` directory for pre-deployment checks and readiness artifacts |
| **Manage** | `incident/` directory for monitoring, escalation, and response |

---

## Related resources

| Repository | What it adds |
|---|---|
| [governance-playbook](https://github.com/simaba/governance-playbook) | Full governance playbook with broader operating-model guidance |
| [release-checklist](https://github.com/simaba/release-checklist) | CLI validator and stricter release gate logic |
| [release-governance](https://github.com/simaba/release-governance) | Release lifecycle governance framework |
| [nist-rmf-guide](https://github.com/simaba/nist-rmf-guide) | Practitioner guide for implementing NIST AI RMF |
| [ai-prism](https://github.com/simaba/ai-prism) | Curated list of governance tools, frameworks, and references |

---

## License

MIT License. See [LICENSE](LICENSE).

---

*Maintained by [Sima Bagheri](https://github.com/simaba) · Built for AI teams working in regulated environments.*
