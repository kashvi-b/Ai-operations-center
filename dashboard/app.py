import streamlit as st

st.set_page_config(
    page_title="Enterprise AI Operations Center",
    layout="wide"
)

st.title("Enterprise AI Operations Center")

st.write(
    """
Welcome to the Enterprise AI Operations Center.

This platform uses:

- LangGraph
- Multi-Agent AI
- XGBoost
- SHAP
- FastAPI
- PostgreSQL

to automate business analytics.
"""
)

st.sidebar.title("Navigation")

st.sidebar.info("Dashboard Coming Soon")