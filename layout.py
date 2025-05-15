import streamlit as st

def show_filters(df):
    st.title("Chat Topics Dashboard")

    min_date = df['session_start_date'].min().date()
    max_date = df['session_start_date'].max().date()


    col1, col2, col3, col4 = st.columns(4)
    with col1:
        start_date = st.date_input("Start Date", value=min_date, min_value=min_date, max_value=max_date)
    with col2:
        end_date = st.date_input("End Date", value=max_date, min_value=min_date, max_value=max_date)
    with col3:
        countries = sorted(df["session_country_name"].dropna().unique())
        countries.insert(0, "All")
        selected_country = st.selectbox("Pick the Country", countries)
    with col4:
        # Toto bude aktualizováno později na základě filtrování
        all_categories = set()
        for tags_dict in df["categorized_tags"]:
            all_categories.update(tags_dict.keys())
        categories = ["All"] + sorted(all_categories)
        selected_category = st.selectbox("Choose category", categories)

    return start_date, end_date, selected_country, selected_category

def show_header(df, start_date, end_date):
    st.markdown(f"**{df.shape[0]} chats** from **{start_date}** to **{end_date}**")


