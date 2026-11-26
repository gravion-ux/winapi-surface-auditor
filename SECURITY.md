# Security Policy

This repository holds the source of the tool.

This policy covers problems **in this repository** -- the code, the
configuration and the documentation.

## Reporting a vulnerability

Please **do not open a public issue** for a vulnerability. Report it
privately, either way:

- GitHub's private vulnerability reporting:
  <https://github.com/gravion-ux/winapi-surface-auditor/security/advisories/new>
- Email: priyanshukumarthakur937@gmail.com

Please include:

- A one- or two-sentence description of the issue.
- The version or commit SHA it affects.
- The smallest reproduction you have -- the input or command that triggers
  the behaviour.
- The impact you believe it has.

You can expect an acknowledgement within a few days.

## Disclosure timing

Please allow **90 days** for a fix to be released before any public
disclosure. If a fix ships earlier, coordinated disclosure can happen as soon
as the fixed version is available.

## Scope

In scope -- this repository, for example:

- A crash, an incorrect result, or a silent failure in the tool itself.
- A path that reads or writes outside the directory the tool was pointed at.
- A command that runs something other than what its help text promises.
- Documentation that describes behaviour the code does not have.

Out of scope:

- Vulnerabilities in the platforms, services or products this tool was
  pointed at. Those go to the owner of that system, through its own
  disclosure channel.
- Missing features and design preferences.
- Reports about other repositories in this account.

## Supported versions

Only the current `main` branch is supported. Older commits are kept for
history, not for backports.
