import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

import streamlit as st
import pandas as pd

from graph.workflow import graph

# ----------------------------
# Page Configuration
# ----------------------------

st.set_page_config(
    page_title="Enterprise AI Operations Center",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Enterprise AI Operations Center")

# ----------------------------
# User Query
# ----------------------------

query = st.text_input(
    "Ask AI",
    value="Generate business report"
)

# ----------------------------
# Run Workflow
# ----------------------------

if st.button("Analyze", use_container_width=True):

    with st.spinner("Running AI Agents..."):

        response = graph.invoke(
            {
                "query": query,
                "intent": "",
                "result": [],
                "analytics": {},
                "charts": {},
                "forecast": {},
                "report": ""
            }
        )

    st.success("Analysis Complete!")

    # ==========================
    # Business Metrics
    # ==========================

    analytics = response["analytics"]

    st.subheader("📈 Business Metrics")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Customers",
        analytics["total_customers"]
    )

    col2.metric(
        "Average Revenue",
        f"₹{analytics['average_revenue']:,.2f}"
    )

    col3.metric(
        "Average Churn",
        f"{analytics['average_churn_probability']:.2f}"
    )

    col4.metric(
        "Highest Churn",
        f"{analytics['highest_churn_probability']:.2f}"
    )

    st.divider()

    # ==========================
    # Revenue Chart
    # ==========================

    charts = response["charts"]

    if "revenue_chart" in charts:

        st.subheader("📊 Revenue Visualization")

        st.plotly_chart(
            charts["revenue_chart"],
            use_container_width=True
        )

    st.divider()

    # ==========================
    # SQL Results
    # ==========================

    st.subheader("📋 High-Risk Customers")

    df = pd.DataFrame(response["result"])

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # ==========================
    # Forecast
    # ==========================

    forecast = response["forecast"]

    st.subheader("🔮 Revenue Forecast")

    f1, f2 = st.columns(2)

    f1.metric(
        "Current Average Revenue",
        f"₹{forecast['current_average_revenue']:,.2f}"
    )

    f2.metric(
        "Predicted Next Month",
        f"₹{forecast['predicted_next_month_revenue']:,.2f}",
        delta=forecast["growth_assumption"]
    )

    st.divider()

    # ==========================
    # AI Report
    # ==========================

    st.subheader("📄 Enterprise AI Report")

    st.code(
        response["report"],
        language="text"
    )