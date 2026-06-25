# GenAI Incident Response Workflow

## Purpose

This workflow defines how GenAI and agentic AI incidents are identified, contained, escalated, remediated, retested, and closed.

## Incident categories

- Prompt injection success
- Hallucination
- PII leakage
- Unsafe recommendation
- Unauthorized tool use
- Customer harm
- Repeated failed guardrail
- Vendor model issue
- Confidential information exposure
- Audit logging failure

## General workflow

1. Detect issue through monitoring, testing, user report, QA sample, DLP alert, tool-call log, or incident report.
2. Classify incident type and severity.
3. Preserve prompt, output, source, tool-call, and approval evidence.
4. Contain risk by blocking output, disabling tool access, restricting workflow, or pausing use case.
5. Notify the business owner, technology owner, risk owner, and relevant privacy, security, legal, or vendor reviewers.
6. Complete root-cause analysis.
7. Define remediation action.
8. Retest failed control.
9. Update risk register, monitoring plan, and control evidence.
10. Close only when closure evidence is reviewed.

## Prompt injection success

Containment:

- Block affected workflow
- Preserve prompt and output
- Disable affected tool action if needed
- Add test case to prompt injection suite

Remediation:

- Update prompt hierarchy
- Strengthen input sanitization
- Restrict tool boundary
- Retest direct and indirect injection cases

Escalation:

- AI security reviewer
- Technology owner
- AI risk committee for critical failure

## Hallucination

Containment:

- Remove unsupported output from customer or operational queue
- Add human review requirement
- Restrict unsupported response category

Remediation:

- Improve source-grounding logic
- Add refusal rule for missing source
- Retest factuality and unsupported inference prompts

## PII leakage

Containment:

- Suppress exposed output
- Secure or delete exposed logs as required
- Notify privacy incident response lead

Remediation:

- Strengthen masking
- Reduce data fields available to model
- Review retention and access
- Retest PII cases

## Unsafe recommendation

Containment:

- Block recommendation
- Require human review
- Remove unauthorized wording

Remediation:

- Update high-risk advice filter
- Define approved response templates
- Retest customer-impacting prompts

## Unauthorized tool use

Containment:

- Disable tool access
- Preserve tool-call logs
- Block action completion
- Review approval workflow

Remediation:

- Update tool permission matrix
- Add approval checkpoint
- Add transaction or action limits
- Retest agentic workflow

## Customer harm

Containment:

- Prioritize customer remediation
- Notify business owner and conduct risk
- Assess affected population
- Pause use case if required

Remediation:

- Root-cause analysis
- Process correction
- Customer remediation plan
- Committee reporting

## Repeated failed guardrail

Containment:

- Pause expansion
- Increase human review
- Notify AI risk management office

Remediation:

- Reassess control design
- Update residual risk rating
- Define additional mitigation
- Require risk owner approval before restart
