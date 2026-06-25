from pathlib import Path
import pandas as pd
import streamlit as st
import plotly.express as px

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"

st.set_page_config(
    page_title="GenAI and Agentic AI Risk Governance Lab",
    page_icon="🛡️",
    layout="wide",
)

@st.cache_data
def load_csv(name):
    return pd.read_csv(DATA_DIR / name)

use_cases = load_csv("genai_use_case_register.csv")
prompt_tests = load_csv("prompt_test_cases.csv")
tool_calls = load_csv("agent_tool_calls.csv")
pii_tests = load_csv("pii_leakage_tests.csv")
hallucinations = load_csv("hallucination_eval_log.csv")
guardrails = load_csv("guardrail_test_results.csv")
escalations = load_csv("human_escalation_log.csv")
risk_register = load_csv("genai_risk_register.csv")
monitoring = load_csv("genai_monitoring_plan.csv")
controls = load_csv("genai_control_library.csv")
control_scores = load_csv("control_effectiveness_score.csv")
findings = load_csv("red_team_findings.csv")
incidents = load_csv("genai_incident_log.csv")
decisions = load_csv("residual_risk_decisions.csv")

risk_rank = {"Low": 1, "Medium": 2, "High": 3, "Critical": 4}
severity_rank = {"Low": 1, "Medium": 2, "High": 3, "Critical": 4}

risk_view = risk_register.merge(
    use_cases[["use_case_id", "use_case_name", "business_function", "agentic_ai_flag", "customer_facing"]],
    on="use_case_id",
    how="left",
)
risk_view["inherent_score"] = risk_view["inherent_risk"].map(risk_rank)
risk_view["residual_score"] = risk_view["residual_risk"].map(risk_rank)

guardrail_view = guardrails.merge(
    use_cases[["use_case_id", "use_case_name"]],
    on="use_case_id",
    how="left",
)

tool_view = tool_calls.merge(
    use_cases[["use_case_id", "use_case_name", "risk_tier"]],
    on="use_case_id",
    how="left",
)

pii_view = pii_tests.merge(
    use_cases[["use_case_id", "use_case_name"]],
    on="use_case_id",
    how="left",
)

hallucination_view = hallucinations.merge(
    use_cases[["use_case_id", "use_case_name"]],
    on="use_case_id",
    how="left",
)

page = st.sidebar.radio(
    "Dashboard pages",
    [
        "Executive summary",
        "GenAI risk heatmap",
        "Prompt injection test results",
        "Tool-use approval exceptions",
        "PII leakage findings",
        "Hallucination findings",
        "Failed guardrails",
        "Human escalation volume",
        "Unresolved high-risk issues",
        "Control effectiveness",
        "Monitoring plan",
        "Risk register",
    ],
)

st.title("GenAI and Agentic AI Risk Governance Lab")
st.caption("Synthetic reference implementation for GenAI risk, agentic tool-use controls, guardrail testing, monitoring, and escalation.")

if page == "Executive summary":
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("GenAI use cases", len(use_cases))
    c2.metric("Agentic use cases", int((use_cases["agentic_ai_flag"] == "Yes").sum()))
    c3.metric("Customer-facing use cases", int((use_cases["customer_facing"] == "Yes").sum()))
    c4.metric("High/Critical risk use cases", int(use_cases["risk_tier"].isin(["High", "Critical"]).sum()))

    c5, c6, c7, c8 = st.columns(4)
    c5.metric("Failed guardrails", int((guardrails["pass_fail"] == "Fail").sum()))
    c6.metric("PII leakage detections", int((pii_tests["leakage_detected"] == "Yes").sum()))
    c7.metric("Hallucinations detected", int((hallucinations["hallucination_detected"] == "Yes").sum()))
    c8.metric("Open incidents", int((incidents["status"] != "Closed").sum()))

    st.subheader("Use cases by risk tier")
    tier_counts = use_cases["risk_tier"].value_counts().reset_index()
    tier_counts.columns = ["risk_tier", "count"]
    st.plotly_chart(px.bar(tier_counts, x="risk_tier", y="count"), use_container_width=True)

    st.subheader("Guardrail results")
    gr_counts = guardrails["pass_fail"].value_counts().reset_index()
    gr_counts.columns = ["result", "count"]
    st.plotly_chart(px.pie(gr_counts, names="result", values="count"), use_container_width=True)

elif page == "GenAI risk heatmap":
    st.subheader("Inherent vs residual risk")
    st.dataframe(
        risk_view[[
            "risk_id", "use_case_name", "risk_category", "inherent_risk",
            "residual_risk", "owner", "status"
        ]],
        use_container_width=True,
    )

    st.plotly_chart(
        px.scatter(
            risk_view,
            x="inherent_score",
            y="residual_score",
            color="risk_category",
            size="residual_score",
            hover_data=["use_case_name", "risk_description", "owner", "status"],
            labels={"inherent_score": "Inherent risk score", "residual_score": "Residual risk score"},
        ),
        use_container_width=True,
    )

elif page == "Prompt injection test results":
    st.subheader("Prompt and adversarial test cases")
    categories = st.multiselect("Filter prompt category", sorted(prompt_tests["prompt_category"].unique()))
    df = prompt_tests.copy()
    if categories:
        df = df[df["prompt_category"].isin(categories)]
    st.dataframe(df, use_container_width=True)

    result_counts = prompt_tests["test_result"].value_counts().reset_index()
    result_counts.columns = ["test_result", "count"]
    st.plotly_chart(px.bar(result_counts, x="test_result", y="count"), use_container_width=True)

elif page == "Tool-use approval exceptions":
    st.subheader("Tool calls requiring review or escalation")
    exceptions = tool_view[
        (tool_view["risk_flag"] == "Yes")
        | (tool_view["escalation_required"] == "Yes")
        | (tool_view["approval_status"].isin(["Rejected", "Pending"]))
    ]
    st.dataframe(exceptions, use_container_width=True)

    tool_counts = tool_calls["tool_accessed"].value_counts().reset_index()
    tool_counts.columns = ["tool_accessed", "count"]
    st.plotly_chart(px.bar(tool_counts, x="tool_accessed", y="count"), use_container_width=True)

elif page == "PII leakage findings":
    st.subheader("PII leakage tests")
    st.dataframe(pii_view, use_container_width=True)

    pii_counts = pii_tests.groupby(["pii_type", "leakage_detected"], as_index=False).size()
    st.plotly_chart(px.bar(pii_counts, x="pii_type", y="size", color="leakage_detected"), use_container_width=True)

elif page == "Hallucination findings":
    st.subheader("Hallucination evaluation log")
    st.dataframe(hallucination_view, use_container_width=True)

    hallucination_counts = hallucinations["hallucination_detected"].value_counts().reset_index()
    hallucination_counts.columns = ["hallucination_detected", "count"]
    st.plotly_chart(px.bar(hallucination_counts, x="hallucination_detected", y="count"), use_container_width=True)

elif page == "Failed guardrails":
    st.subheader("Failed or needs-review guardrails")
    failed = guardrail_view[guardrail_view["pass_fail"].isin(["Fail", "Needs review"])]
    st.dataframe(failed, use_container_width=True)

    severity_counts = failed["severity"].value_counts().reset_index()
    severity_counts.columns = ["severity", "count"]
    st.plotly_chart(px.bar(severity_counts, x="severity", y="count"), use_container_width=True)

elif page == "Human escalation volume":
    st.subheader("Human escalation log")
    esc_view = escalations.merge(
        use_cases[["use_case_id", "use_case_name", "business_function"]],
        on="use_case_id",
        how="left",
    )
    st.dataframe(esc_view, use_container_width=True)

    esc_counts = esc_view["severity"].value_counts().reset_index()
    esc_counts.columns = ["severity", "count"]
    st.plotly_chart(px.bar(esc_counts, x="severity", y="count"), use_container_width=True)

elif page == "Unresolved high-risk issues":
    st.subheader("Open high-risk findings and incidents")
    open_findings = findings[(findings["status"] != "Closed") & (findings["severity"].isin(["High", "Critical"]))]
    open_incidents = incidents[(incidents["status"] != "Closed") & (incidents["severity"].isin(["High", "Critical"]))]
    st.write("Open red-team findings")
    st.dataframe(open_findings, use_container_width=True)
    st.write("Open incidents")
    st.dataframe(open_incidents, use_container_width=True)

elif page == "Control effectiveness":
    st.subheader("Control effectiveness score")
    st.dataframe(control_scores, use_container_width=True)

    st.plotly_chart(
        px.bar(
            control_scores,
            x="guardrail_name",
            y="control_effectiveness_score",
            hover_data=["rating", "remediation_status", "failures"],
        ),
        use_container_width=True,
    )

elif page == "Monitoring plan":
    st.subheader("GenAI monitoring plan")
    st.dataframe(monitoring, use_container_width=True)

    status_counts = monitoring["status"].value_counts().reset_index()
    status_counts.columns = ["status", "count"]
    st.plotly_chart(px.bar(status_counts, x="status", y="count"), use_container_width=True)

elif page == "Risk register":
    st.subheader("GenAI risk register")
    st.dataframe(risk_view, use_container_width=True)

    st.subheader("Residual risk decisions")
    st.dataframe(decisions, use_container_width=True)

    st.subheader("Control library")
    st.dataframe(controls, use_container_width=True)
