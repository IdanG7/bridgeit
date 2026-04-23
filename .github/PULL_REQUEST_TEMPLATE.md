## Summary

<!-- What does this PR do, and why? -->

## Type of change

- [ ] Bug fix (non-breaking change that fixes an issue)
- [ ] New feature (non-breaking change that adds functionality)
- [ ] Breaking change
- [ ] Documentation / refactor (no functional change)

## Test plan

<!-- How did you verify this works? -->

- [ ] Unit tests pass: `uv run pytest -m "not integration"`
- [ ] Integration tests pass (if touching pybag/DbgEng code): `$env:PYBAG_INTEGRATION = "1"; uv run pytest`
- [ ] `stackly doctor` reports clean
- [ ] Manual end-to-end sanity check (if behavior-changing): `scripts/e2e_smoke.py`

## Checklist

- [ ] CHANGELOG.md updated under `## Unreleased`
- [ ] Docs updated (README or CONTRIBUTING)
- [ ] Conventional commit message on the merge commit
