# Incident Escalation Matrix

Replace all placeholders with organization-specific contacts, service levels, and legal/regulatory obligations. Do not place personal phone numbers or sensitive contact details in a public repository.

| Trigger | Initial owner | Notify | Target response | Immediate action | Decision authority |
|---|---|---|---|---|---|
| Suspected privacy or security exposure | Security/privacy incident lead | security, privacy, technical owner | [per policy] | contain access, preserve evidence | designated incident authority |
| Unsafe, harmful, or high-impact output | Business and technical owners | governance, safety/domain reviewer | [per policy] | pause or constrain affected path | accountable business/risk owner |
| Material reliability or availability degradation | Technical/release owner | operations, product, governance | [per policy] | activate rollback or degraded mode | release owner |
| Prompt injection or unauthorized tool behavior | Security and technical owners | governance, tool owner | [per policy] | disable/restrict tool path | security owner |
| Repeated evaluation or monitoring control failure | AI/model and governance owners | technical, business, risk owners | [per policy] | hold rollout or schedule corrective review | governance decision forum |

## Escalation record

For each escalation, record:

- trigger and evidence
- incident or risk ID
- systems/versions affected
- containment decision and time
- accountable decision owner
- communication obligations and completed notifications
- recovery condition and follow-up review date
