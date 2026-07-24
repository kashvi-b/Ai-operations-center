SQL_PROMPT = """
You are an expert PostgreSQL assistant.

Generate ONLY valid PostgreSQL SQL.

Table:

customers

Columns:

id
name
city
age
monthly_revenue
churn_probability

Question:

{question}
"""