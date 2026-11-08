import streamlit as st

from src.data_loader import load_data
from src.filters import apply_sidebar_filters
from src.metrics import show_key_metrics

st.set_page_config(page_title="Tech Job Insights", page_icon="💼", layout="wide")

df = load_data()

st.title("Tech Job Insights")


# Sidebar filters
filtered_df = apply_sidebar_filters(df)
if filtered_df.empty:
    st.warning("No job offers match the selected filters.")
    st.stop()

# Key metrics
show_key_metrics(filtered_df)

st.dataframe(filtered_df)