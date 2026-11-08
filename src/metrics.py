import streamlit as st

def show_key_metrics(df):
    """Show the key metrics of the filtered job offers."""
    total_col, salary_col, remote_col = st.columns(3)

    total_col.metric("Total offers", len(df))

    average_salary = df["Salary (EUR)"].mean()
    salary_col.metric("Average salary", f"{average_salary:,.0f} €")

    remote_share = (df["Work Mode"] == "Remote").mean() * 100
    remote_col.metric("Remote jobs", f"{remote_share:.0f}%")