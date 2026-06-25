# Agentic AI Control Standard

## Purpose

This standard defines minimum controls for agentic AI workflows that can call tools, retrieve data, draft communications, route cases, update records, or propose actions.

## Scope

This standard applies to any GenAI system that can take actions through tools, APIs, workflow systems, document repositories, CRM systems, complaint platforms, payment-status tools, email drafting tools, or external search tools.

## Control principles

### No autonomous external action without approval

Agentic AI must not complete external customer, vendor, payment, complaint, collections, account, legal, or regulatory actions without an approved human checkpoint.

The system may draft, summarize, classify, or recommend, but material action must remain subject to human approval.

### Tool access limits

Each agent must have a documented tool access matrix defining:

- Approved tools
- Approved data scope
- Prohibited tools
- Prohibited data fields
- Approved actions
- Actions requiring human approval
- Actions blocked entirely
- Logging requirements
- Emergency shutdown process

### Memory restrictions

Memory must be disabled or strictly restricted for workflows that process:

- Customer information
- Complaint details
- Account information
- Transaction details
- Employment information
- Vendor confidential information
- Investigation material
- Legal or regulatory content

Any enabled memory must have documented purpose, retention, deletion, access control, and privacy review.

### Human approval checkpoints

Human approval is required before:

- Sending external communications
- Updating customer or complaint records
- Making customer treatment recommendations
- Taking collections-related action
- Approving contract, vendor, legal, risk, or compliance decisions
- Using sensitive or confidential information beyond the approved scope
- Acting on a low-confidence or unsupported model output

### Audit logging

Audit logs must capture:

- Prompt
- Output
- Tool called
- Data source used
- Approval status
- Human approver
- Action completed or blocked
- Escalation status
- Timestamp
- System version or workflow version

### Exception handling

Exceptions must be logged when:

- A guardrail fails
- A tool action is blocked
- An approval is rejected
- PII leakage is detected
- Prompt injection succeeds
- A hallucination is confirmed
- A user complaint references AI output
- A human reviewer overrides the system

### Escalation path

High and critical issues should escalate to:

1. Business owner
2. Technology owner
3. Risk owner
4. Privacy or security reviewer if applicable
5. AI risk management office
6. AI risk committee for unresolved or material residual risk

### Periodic review

Agentic AI controls must be reviewed:

- Before pilot
- Before production
- After material workflow change
- After vendor model change
- After control failure
- At least quarterly for high-risk use cases
- At least monthly for critical-risk workflows
