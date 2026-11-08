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

# Charts
st.subheader("Market overview")
tech_col, salary_col, mode_col = st.columns(3)
tech_col.plotly_chart(technology_demand_chart(filtered_df))
salary_col.plotly_chart(salary_by_level_chart(filtered_df))
mode_col.plotly_chart(work_mode_chart(filtered_df))

# Jobs table
st.subheader("Job offers")
st.dataframe(filtered_df)