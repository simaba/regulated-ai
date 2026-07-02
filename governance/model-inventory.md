# AI System and Model Inventory

Maintain one row per deployed or evaluated AI system. Do not place credentials, private endpoint details, sensitive customer data, or proprietary evaluation outputs in a public copy of this file.

| System ID | System / capability | Intended use | Owner | Risk tier | Data categories | Model / version | Tool permissions | Environment | Status | Last review |
|---|---|---|---|---|---|---|---|---|---|---|
| AI-001 | [Name] | [Bounded intended use] | [Role] | low / medium / high | [e.g., public, internal, sensitive] | [Model identifier] | read-only / write / external | development / staging / production | planned / active / retired | YYYY-MM-DD |

## Required inventory notes

For each active system, record or link:

- intended users and prohibited uses
- accountable business, technical, and governance owners
- model/provider, prompt/configuration, retrieval, and tool-permission versions
- data provenance, retention, and access boundary summary
- evaluation/report location and current known limitations
- monitoring, incident, rollback, and retirement owner

## Change events requiring an inventory update

- a new model, provider, prompt, retrieval source, tool, or permission boundary
- a change in intended use, user population, autonomy, or risk classification
- a material evaluation result, incident, or release decision
- decommissioning or withdrawal of the system
