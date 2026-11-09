import streamlit as st

from src.data_loader import load_data
from src.filters import apply_sidebar_filters
from src.metrics import show_key_metrics
from src.charts import technology_demand_chart, salary_by_level_chart, work_mode_chart

st.set_page_config(page_title="Tech Job Insights", page_icon="💼", layout="wide")

df = load_data()

st.title("Tech Job Insights")
st.caption("All figures reflect the filters selected in the sidebar.")


# Sidebar filters
filtered_df = apply_sidebar_filters(df)
if filtered_df.empty:
    st.warning("No job offers match the selected filters.")
    st.stop()

# Key metrics
st.subheader("Key metrics")
show_key_metrics(filtered_df)

# Charts and table
charts_tab, table_tab = st.tabs(["Market overview", "Job offers"])

with charts_tab:
    tech_col, salary_col, mode_col = st.columns(3)
    tech_col.plotly_chart(technology_demand_chart(filtered_df), theme=None, config={"displayModeBar": False})
    salary_col.plotly_chart(salary_by_level_chart(filtered_df), theme=None, config={"displayModeBar": False})
    salary_col.caption("Box: middle 50% of offers. Line: median salary.")
    mode_col.plotly_chart(work_mode_chart(filtered_df), theme=None, config={"displayModeBar": False})

with table_tab:
    st.dataframe(
        filtered_df,
        hide_index=True,
        column_config={
            "Job Title": st.column_config.TextColumn("Job title"),
            "Country": st.column_config.TextColumn("Country", width="small"),
            "Salary (EUR)": st.column_config.NumberColumn("Salary (€)", width="small"),
            "Work Mode": st.column_config.TextColumn("Mode", width="small"),
            "Experience Level": st.column_config.TextColumn("Level", width="small"),
            "Main Technology": st.column_config.TextColumn("Main tech", width="small"),
        },
    )