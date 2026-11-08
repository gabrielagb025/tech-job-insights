import streamlit as st

def show_key_metrics(df):
    """Show the key metrics of the filtered job offers."""

    st.metric("Total offers", len(df))

    average_salary = df["Salary (EUR)"].mean()
    st.metric("Average salary", f"{average_salary:,.0f} €")

    remote_share = (df["Work Mode"] == "Remote").mean() * 100
    st.metric("Remote jobs", f"{remote_share:.0f}%")