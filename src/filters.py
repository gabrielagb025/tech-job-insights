import streamlit as st

FILTER_COLUMNS = {
    "Technology": "Main Technology",
    "Experience level": "Experience Level",
    "Country": "Country",
    "Work mode": "Work Mode",
}


def apply_sidebar_filters(df):
    """Draw the sidebar filters and return the filtered DataFrame."""
    selections = {}
    for label, column in FILTER_COLUMNS.items():
        options = sorted(df[column].unique())
        selections[column] = st.sidebar.multiselect(label, options, placeholder="All")

    min_salary = int(df["Salary (EUR)"].min())
    max_salary = int(df["Salary (EUR)"].max())
    low, high = st.sidebar.slider(
        "Salary (EUR)", min_salary, max_salary, (min_salary, max_salary), step=1000
    )

    filtered_df = df
    for column, selected in selections.items():
        if selected: 
            filtered_df = filtered_df[filtered_df[column].isin(selected)]

    return filtered_df[filtered_df["Salary (EUR)"].between(low, high)]