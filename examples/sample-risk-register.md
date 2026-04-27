# Sample Risk Register

This example is generic and illustrative. It does not describe a real system.

| ID | Risk | Tier | Impact | Likelihood | Owner | Mitigation | Status |
|---|---|---|---|---|---|---|---|
| R-001 | Agent routes sensitive documents to the wrong review queue | Medium | High | Medium | Example Product Owner | require confidence threshold, human review for sensitive categories, and regression tests | Open |
| R-002 | Model performance degrades on underrepresented document types | Medium | Medium | Medium | Example ML Owner | evaluate subgroup performance and add monitoring for category-level drift | Mitigating |
| R-003 | Logging captures unnecessary sensitive metadata | High | High | Low | Example Privacy Owner | minimize logs, mask identifiers, and review retention policy | Mitigating |
| R-004 | Rollback process is documented but not tested | Medium | Medium | Medium | Example Platform Owner | run staging rollback drill before production gate | Open |
| R-005 | Users over-trust triage recommendation without reading confidence signal | Medium | Medium | Medium | Example UX Owner | display confidence and require human confirmation for medium/high-risk outputs | Open |

## Review notes

- Risks should have named owners and dated follow-up actions.
- High-impact risks should not be closed without evidence.
- Release approval should be conditional if high-impact risks remain open.
- Link each risk to the relevant release checklist item, model card section, or incident response control where possible.
