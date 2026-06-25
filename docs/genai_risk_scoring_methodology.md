# GenAI Risk Scoring Methodology

## Purpose

This methodology defines how GenAI and agentic AI risks are rated and treated in the lab.

## Risk levels

| Rating | Meaning |
|---|---|
| Low | Limited internal impact and no sensitive data or customer harm |
| Medium | Operational issue or control gap requiring monitoring |
| High | Potential customer, privacy, security, conduct, legal, or operational harm |
| Critical | Unauthorized action, material data exposure, systemic guardrail failure, or customer harm risk |

## Inherent risk

Inherent risk reflects risk before guardrails and oversight are considered.

Relevant factors include:

- Customer-facing status
- Sensitive data exposure
- External tool access
- Memory
- Vendor involvement
- Autonomous action capability
- Complaint, fraud, collections, legal, credit, or employment context
- Source-grounding requirement
- Human review dependency

## Residual risk

Residual risk reflects remaining risk after controls are considered.

Residual risk should account for:

- Guardrail design
- Guardrail test results
- Human approval checkpoints
- Monitoring thresholds
- Incident history
- Failed tests
- Vendor transparency
- Evidence completeness

## Treatment options

| Treatment | Meaning |
|---|---|
| Accept with monitoring | Risk is within appetite with ongoing monitoring |
| Mitigate | Additional control, remediation, or retest is required |
| Escalate | Senior risk or committee review is required |
| Reject | Use case should not proceed in current form |
| Restrict | Use case can proceed only with limited data, tools, users, or workflow scope |
