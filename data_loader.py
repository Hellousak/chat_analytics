import pandas as pd
from utils import extract_tags, categorize_tags

def load_data(path):
    df = pd.read_csv(path)
    df['session_start_date'] = pd.to_datetime(df['session_start_date (GMT+0)'], format="%Y-%m-%d %H:%M:%S")
    df["tags"] = df["tags"].apply(extract_tags)
    df['categorized_tags'] = df['tags'].apply(categorize_tags)
    return df

def filter_data(df, start_date, end_date):
    df = df.dropna(subset=["session_country_name", "tags"])
    return df[(df['session_start_date'].dt.date >= start_date) & (df['session_start_date'].dt.date <= end_date)]
