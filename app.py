import streamlit as st
from src.data_loader import load_data

st.set_page_config(page_title="Tech Job Insights", page_icon="💼", layout="wide")


df = load_data()