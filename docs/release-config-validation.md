# Release-Config Validation

This starter repository distinguishes two checks:

1. **Template validation** checks that `release/release-checklist.yaml` has the expected structure and supported metadata. The default file intentionally contains `false` gates and placeholder values because it is not a release request.
2. **Readiness-example validation** checks that `examples/sample-release-checklist.yaml` satisfies the repository's illustrative minimum gates for its declared risk tier and industry.

Run locally:

```bash
python -m pip install pyyaml
python tools/validate_release_config.py release/release-checklist.yaml --mode template
python tools/validate_release_config.py examples/sample-release-checklist.yaml --mode ready
```

The validator is intentionally narrow. It does not certify safety, compliance, legal sufficiency, production readiness, or an actual deployment decision. It only makes the starter template's structural and illustrative gate contract explicit and testable.
