import streamlit as st

from src.data_loader import load_data
from src.filters import apply_sidebar_filters

st.set_page_config(page_title="Tech Job Insights", page_icon="💼", layout="wide")

df = load_data()

st.title("Tech Job Insights")


# Sidebar filters
filtered_df = apply_sidebar_filters(df)

st.dataframe(filtered_df)