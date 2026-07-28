import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

import streamlit as st
import pandas as pd
import requests
import plotly.express as px

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
# Run Analysis
# ----------------------------

if st.button("Analyze", use_container_width=True):

    with st.spinner("Running AI Agents..."):

        api_response = requests.post(
            "http://127.0.0.1:8000/analyze",
            json={
                "query": query
            }
        )

        if api_response.status_code != 200:
            st.error("Failed to connect to FastAPI.")
            st.stop()

        response = api_response.json()

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
    # Revenue Chart
    # ==========================

    st.subheader("📊 Revenue Visualization")

    fig = px.bar(
        df,
        x="name",
        y="monthly_revenue",
        color="churn_probability",
        title="Top High-Risk Customers by Revenue",
        labels={
            "name": "Customer",
            "monthly_revenue": "Monthly Revenue",
            "churn_probability": "Churn Probability"
        }
    )

    st.plotly_chart(
        fig,
        use_container_width=True
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

    st.markdown(
        f"```text\n{response['report']}\n```"
    )