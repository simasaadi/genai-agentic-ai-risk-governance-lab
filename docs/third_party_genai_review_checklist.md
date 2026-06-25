# Third-Party GenAI Review Checklist

## Vendor model transparency

- Does the vendor disclose model type and material limitations?
- Does the vendor disclose whether submitted data is used for model training?
- Can training on submitted data be disabled?
- Are model changes communicated before deployment?
- Are testing results available for security, privacy, bias, and robustness?

## Data handling

- What data is sent to the vendor?
- Where is data stored?
- Where is data processed?
- What is the retention period?
- Are logs retained?
- Are prompts and outputs retained?
- Are subcontractors involved?
- Are cross-border transfers involved?

## Security and access

- Is encryption applied in transit and at rest?
- Is role-based access enforced?
- Are administrative actions logged?
- Is vulnerability management documented?
- Are API keys and secrets protected?
- Is incident notification contractually defined?

## Contractual controls

- Audit rights
- Data deletion rights
- Model training restriction
- Incident notification timeline
- Subcontractor disclosure
- Service availability requirements
- Exit and portability requirements
- Regulatory cooperation requirements

## GenAI-specific controls

- Prompt injection controls
- PII leakage controls
- Hallucination or unsupported response controls
- Source-grounding support
- Content filtering
- Human oversight options
- Tool-use restrictions
- Monitoring exports
- Audit logs

## Decision

| Decision | Meaning |
|---|---|
| Approved | No blocking gaps |
| Approved with conditions | Use limited to documented restrictions |
| Pending evidence | Vendor must provide missing evidence |
| Escalated | Risk owner or committee decision required |
| Rejected | Use case should not proceed with the vendor as proposed |
