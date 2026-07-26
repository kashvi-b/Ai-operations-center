from sqlalchemy import text
from database.connection import engine


def sql_agent(state):
    try:
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

        with engine.connect() as conn:
            result = conn.execute(text(sql))
            rows = [dict(row._mapping) for row in result]

        state["result"] = rows

    except Exception as e:
        state["result"] = f"Database Error: {str(e)}"

    return state