from pathlib import Path

import pandas as pd
import streamlit as st

DATA_PATH = Path(__file__).parent.parent / "data" / "jobs.csv"


@st.cache_data
def load_data():
    """Load the job offers from the CSV file."""
    return pd.read_csv(DATA_PATH)