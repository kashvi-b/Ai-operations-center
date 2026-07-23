from sqlalchemy import text
from database.connection import engine


def sql_agent(state):
    query = state["query"].lower()

    if "customer" in query and "churn" in query:

        sql = """
        SELECT
            id,
            name,
            city,
            churn_probability
        FROM customers
        WHERE churn_probability > 0.7
        ORDER BY churn_probability DESC
        LIMIT 10;
        """

        with engine.connect() as conn:
            rows = conn.execute(text(sql))
            results = rows.fetchall()

        state["result"] = results

    else:
        state["result"] = "No SQL query matched."

    return state