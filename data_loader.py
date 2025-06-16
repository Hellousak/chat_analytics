import pandas as pd
from utils import extract_tags, categorize_tags
import streamlit as st


def upload_and_load_data(default_path="reportv-16812456-dhz5W4hbmklKUEhA.csv"):
    st.sidebar.markdown("## Upload data")

    use_default = st.sidebar.checkbox("Use default data", value=True)
    uploaded_file = None

    if not use_default:
        uploaded_file = st.sidebar.file_uploader("Upload CSV file", type="csv")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.success("Your CSV was uploaded.")
    else:
        st.info("The default CSV file is being used.")
        try:
            df = pd.read_csv(default_path)
        except FileNotFoundError:
            st.error(f"The default CSV file {default_path} was not found.")
            st.stop()

    df['session_start_date'] = pd.to_datetime(df['session_start_date (GMT+0)'], format="%Y-%m-%d %H:%M:%S")
    # Předpokládáme, že tento sloupec už je string nebo ISO datetime



    df["tags"] = df["tags"].apply(extract_tags)
    df['categorized_tags'] = df['tags'].apply(categorize_tags)

    return df
def filter_data(df, start_date, end_date):
    df = df.dropna(subset=["session_country_name", "tags"])
    return df[(df['session_start_date'].dt.date >= start_date) & (df['session_start_date'].dt.date <= end_date)]



