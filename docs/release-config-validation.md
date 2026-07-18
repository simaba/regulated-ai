# Release-Decision Configuration Validation

This starter repository validates the structure and selected decision semantics of a release record. It deliberately does not prescribe universal accuracy, fairness, industry, or approval gates.

## Modes

### Template

```bash
python tools/validate_release_config.py \
  release/release-checklist.yaml \
  --mode template
```

Template mode checks:

- required top-level sections;
- required metadata fields;
- supported decision outcomes and gate statuses;
- gate field types;
- list structure;
- unique gate identifiers.

Placeholders and unresolved gates are allowed because the file is a starting structure, not a release request.

### Ready

```bash
python tools/validate_release_config.py \
  examples/sample-release-checklist.yaml \
  --mode ready
```

Ready mode additionally checks:

- no placeholder string remains anywhere in the supplied record, including nested decision lists, evidence references, findings, and follow-through fields;
- `metadata.version` is a stable token rather than free-form prose;
- `metadata.evidence_cutoff` is a valid ISO date in `YYYY-MM-DD` form;
- the decision includes a non-empty rationale;
- at least one gate exists;
- passing and not-applicable gates cite evidence;
- not-applicable gates contain a scoped rationale;
- release and conditional release have no blockers;
- release and conditional release have no unresolved hard gates;
- unconditional release has no conditions or required actions;
- conditional release has at least one condition or required action;
- deferred decisions identify evidence gaps;
- do-not-release decisions identify a blocker or unresolved hard gate.

The version rule allows letters, digits, `.`, `_`, `+`, and `-`; it does not require semantic versioning. The purpose is to make the reviewed configuration identifiable and stable enough to compare with its evidence.

## Semantics

The configuration distinguishes:

- **hard gate:** a non-compensable requirement for the reviewed scope;
- **blocker:** unresolved finding that prevents release;
- **required action:** accepted follow-up work under a bounded conditional decision;
- **condition:** enforceable restriction on scope or operation;
- **evidence gap:** missing or unreliable support for a proposition;
- **residual risk:** risk remaining after controls, requiring organization-specific acceptance.

The validator checks internal coherence. It does not determine whether:

- a gate is appropriate;
- evidence is authentic, current, representative, or sufficient;
- a not-applicable rationale is correct;
- a finding severity is justified;
- a condition is enforceable in the real system;
- a residual-risk owner has proper authority;
- a release is safe, lawful, compliant, production-ready, or valuable.

## Tests

```bash
python -m unittest discover -s tests -v
```

The tests cover blocker, condition, hard-gate, evidence, nested-placeholder, date, version, deferred-decision, and duplicate-ID semantics.

## Customization

Organizations should replace the example propositions with gates derived from the actual:

- intended use and affected population;
- data, model, tool, permission, and action scope;
- harm and consequence model;
- applicable policies and obligations;
- evaluation and control evidence;
- operational, incident, recovery, and redress needs;
- release authority and residual-risk process.

Do not add a generic gate merely because it sounds responsible. Every gate should support a named decision and have an evidence owner, method, scope, and invalidation trigger.
