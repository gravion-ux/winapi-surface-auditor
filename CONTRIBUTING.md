# Contributing to winapi-surface-auditor

Thanks for your interest in contributing! This repository holds the source of the tool.

This document explains how to propose a change and what is expected before it
is merged.

## Getting started

1. Fork the repository and clone your fork:

   ```bash
   git clone https://github.com/<your-username>/winapi-surface-auditor.git
   cd winapi-surface-auditor
   ```

2. Create a branch for your change:

   ```bash
   git checkout -b my-change
   ```

## Run the tests

```bash
pytest -q
```

CI runs the same command on every push and pull request, so a green local run
means the CI check will be green too.

## Ground rules

- **One change per pull request.** Keep it focused.
- **No secrets.** Never commit API keys, tokens, passwords or personal data.
- **No drafting markers.** A `TODO`, `FIXME` or placeholder left in the
  source is a defect, not a note to self.
- **Match the existing style.** Follow the conventions already used in the
  files you touch.
- **Explain the change.** Say what changed, why, and how you verified it.

## Pull request rules

- The tests must pass locally and CI must be green on the final commit.
- New behaviour has a test, including the case it refuses.
- Public documentation (`README.md`) matches the code.
- The commit message says what changed, in one line.

## Reporting bugs and requesting features

Use the GitHub issue templates (Bug report / Feature request) so reports
include the information needed to evaluate them.

## Reporting security vulnerabilities

Please do **not** open a public issue for a security vulnerability. Follow
the private reporting process in [SECURITY.md](SECURITY.md) instead.

## Code of conduct

Participation in this project is governed by the
[Code of Conduct](CODE_OF_CONDUCT.md).

## Licence

By contributing, you agree that your contribution is provided under the
repository's existing licence.
