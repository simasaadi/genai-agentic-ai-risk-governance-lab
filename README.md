# GenAI and Agentic AI Risk Governance Lab

This repository is a synthetic reference implementation for governing generative AI and agentic AI risks in a banking-style operating environment.

It focuses on practical controls for prompt injection, tool use, hallucination, memory, personal information exposure, human oversight, guardrail testing, monitoring, incident escalation, and residual risk treatment.

All data in this repository is synthetic. No real bank, customer, employee, vendor, model, incident, prompt, tool call, or production control data is used.

## Purpose

The lab shows how a GenAI governance function can move beyond policy statements and create operating artifacts that answer:

- Which GenAI and agentic AI use cases exist
- Which systems are customer-facing
- Which use cases have tool access, memory, vendor involvement, or sensitive data exposure
- Which prompt injection, jailbreak, hallucination, privacy, and unauthorized-action risks were tested
- Which guardrails passed, failed, or need remediation
- Which human escalation paths were triggered
- Which residual risks require acceptance, mitigation, or committee escalation
- Which monitoring metrics should be tracked after deployment

## Synthetic scenarios

The lab includes synthetic scenarios for:

| Use case | Primary risk focus |
|---|---|
| Customer support chatbot | Hallucination, PII leakage, prompt injection |
| Internal policy assistant | Source grounding, access control, policy traceability |
| Complaint triage agent | Agentic tool use, unauthorized action, human approval |
| AI meeting summarizer | Overreliance, record accuracy, sensitive data |
| AI coding assistant | Secret exposure, insecure code, confidential information |
| AI document extraction tool | Field-level traceability, hallucinated extraction |
| AI email drafting assistant | Unauthorized customer commitments |
| Collections support assistant | Conduct risk, customer harm, escalation |
| Vendor contract review assistant | Third-party risk, legal overreach, data boundary |
| Fraud investigation summarization assistant | Unsupported inference, source grounding, case integrity |

## Core artifacts

| Artifact | Purpose |
|---|---|
| data/genai_use_case_register.csv | GenAI and agentic AI inventory |
| data/prompt_test_cases.csv | Prompt injection, jailbreak, hallucination, sensitive-data, and policy-bypass tests |
| data/agent_tool_calls.csv | Agent tool-use events, approval checks, and escalation flags |
| data/pii_leakage_tests.csv | PII exposure and masking test results |
| data/hallucination_eval_log.csv | Source-grounding and hallucination evaluation |
| data/guardrail_test_results.csv | Guardrail test results and remediation status |
| data/human_escalation_log.csv | Human review and escalation events |
| data/genai_risk_register.csv | Inherent risk, residual risk, guardrails, owners, and treatment plans |
| data/genai_monitoring_plan.csv | Monitoring metrics, thresholds, owners, and escalation paths |
| data/genai_control_library.csv | Reusable GenAI and agentic AI controls |
| data/control_effectiveness_score.csv | Control design and operating effectiveness scoring |
| data/red_team_findings.csv | Red-team findings and retest requirements |
| data/genai_incident_log.csv | GenAI incident containment, root cause, and closure evidence |
| data/residual_risk_decisions.csv | Residual risk decisions and approval conditions |

## Dashboard

The Streamlit dashboard includes pages for:

- Executive summary
- GenAI risk heatmap
- Prompt injection test results
- Tool-use approval exceptions
- PII leakage findings
- Hallucination findings
- Failed guardrails
- Human escalation volume
- Unresolved high-risk issues
- Control effectiveness
- Monitoring plan
- Risk register

## Run locally

Install dependencies:

    pip install -r requirements.txt

Run validation:

    python scripts/validate_data.py

Run the dashboard:

    streamlit run dashboard/app.py

## Governance focus

The implementation covers:

- GenAI governance
- Agentic AI control design
- Prompt injection testing
- PII leakage testing
- Hallucination evaluation
- Human-in-the-loop controls
- Tool-use approval workflows
- Guardrail testing
- Red-team findings
- Incident escalation
- Residual risk decisioning
- Control effectiveness scoring
- Post-deployment monitoring

## Disclaimer

This repository is a synthetic reference implementation. The data and examples do not represent any actual financial institution, customer, employee, vendor, model, prompt, risk decision, or control environment, and are not intended for production use.
