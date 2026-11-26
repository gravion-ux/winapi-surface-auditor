## What this changes

<!-- One or two sentences. What is different after this pull request? -->

## Why

<!-- Link the issue it closes, or state the problem it solves. -->

## Safety boundary

<!-- If this adds or widens a capability, say what it still cannot do:
     which input it accepts, what it is scoped to, what it refuses.
     A capability with no stated boundary is not ready to merge. -->

## How it was verified

<!-- The exact command you ran, and what it printed. The test count must
     go up, not down. -->

## Checklist

- [ ] - [ ] `pytest -q` passes locally
- [ ] No credential, token, or real endpoint appears anywhere in the diff
- [ ] New behaviour has a test, including the case it refuses
- [ ] Public docs (`README.md`) match the code
