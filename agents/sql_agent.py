from sqlalchemy import text
from database.connection import engine


def sql_agent(state):
    """
    Executes SQL queries based on the user's request.
    """

    query = state["query"].lower()

    try:

        if "customer" in query and "churn" in query:

            sql = """
            SELECT
                id,
                name,
                city,
                monthly_revenue,
                churn_probability
            FROM customers
            WHERE churn_probability > 0.70
            ORDER BY churn_probability DESC
            LIMIT 10;
            """

        elif "revenue" in query:

            sql = """
            SELECT
                id,
                name,
                monthly_revenue
            FROM customers
            ORDER BY monthly_revenue DESC
            LIMIT 10;
            """

        elif "count" in query:

            sql = """
            SELECT COUNT(*) AS total_customers
            FROM customers;
            """

        else:
            state["result"] = "No SQL query matched."
            return state

        with engine.connect() as conn:
            result = conn.execute(text(sql))
            rows = [dict(row._mapping) for row in result]

        state["result"] = rows

    except Exception as e:
        state["result"] = f"Database Error: {str(e)}"

    return state