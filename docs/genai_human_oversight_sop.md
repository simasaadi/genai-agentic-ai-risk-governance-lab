# GenAI Human Oversight SOP

## Purpose

This SOP defines when human review, blocking, escalation, or residual risk acceptance is required for GenAI and agentic AI use cases.

## When human review is required

Human review is required when:

- The use case is customer-facing and output may affect customer understanding or treatment
- The use case involves complaints, fraud, collections, credit, legal, employment, or vendor decisions
- The output is not fully supported by approved sources
- The model confidence is below the approved threshold
- The output includes customer, complaint, transaction, account, employee, or vendor information
- The system proposes an external communication
- The system proposes a workflow action
- A user asks for legal, credit, collections, hardship, or product commitment advice
- A guardrail fails
- Residual risk is high or critical

## When output must be blocked

Output must be blocked when:

- It includes unmasked personal information without approved purpose
- It reveals confidential or restricted information
- It follows prompt injection or jailbreak instructions
- It provides unsupported legal, regulatory, credit, or collections advice
- It creates a customer commitment without approval
- It attempts unauthorized tool use
- It suggests discriminatory or biased treatment
- It fabricates source material
- It produces unsafe customer guidance

## When escalation is needed

Escalation is required when:

- Prompt injection succeeds
- PII leakage is detected
- Unauthorized tool action occurs or is attempted
- Customer harm is possible
- A high-risk output reaches a customer or operational queue
- A vendor issue affects model behavior or data handling
- A monitoring threshold is breached
- A repeated guardrail failure occurs
- Residual risk remains high after mitigation

## When residual risk must be accepted

Residual risk acceptance is required when:

- High or critical risk remains after controls
- The system will continue operating with known limitations
- A guardrail cannot fully eliminate risk
- A business process depends on human review to manage the remaining risk
- A vendor limitation cannot be fully remediated
- A monitoring threshold requires formal risk appetite approval

## Documentation requirements

Human oversight evidence should include:

- Prompt and response sample
- Tool call record
- Human decision
- Approval or rejection
- Rationale
- Escalation status
- Remediation action
- Closure evidence
