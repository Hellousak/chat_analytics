from config import prefix_mapping, category_tree, excluded_tags
import streamlit as st

def show_header(df, start_date, end_date):
    st.markdown(f"**{df.shape[0]} chats** from **{start_date}** to **{end_date}**")

def show_filters(df):
    st.title("Chat Topics Dashboard")

    min_date = df['session_start_date'].min().date()
    max_date = df['session_start_date'].max().date()

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        start_date = st.date_input("Start Date", value=min_date, min_value=min_date, max_value=max_date)

    with col2:
        end_date = st.date_input("End Date", value=max_date, min_value=min_date, max_value=max_date)

    with col3:
        filtered_df = df[
            df["categorized_tags"].notna() &
            df["categorized_tags"].apply(lambda cats: any(c not in excluded_tags for c in cats))
            ]
        countries = sorted(filtered_df["session_country_name"].dropna().unique())
        countries.insert(0, "All")
        selected_country = st.selectbox("Pick the Country", countries)

    with col4:
        # Získáme seznam kategorií z prefix_mapping a klíčů category_tree
        category_tree_keys = list(category_tree.keys())
        prefix_values = list(prefix_mapping.values())

        all_categories = ["All"] + sorted(set(prefix_values + category_tree_keys))
        selected_category = st.selectbox("Choose category", all_categories)
    with col5:
        if selected_category in category_tree:
            # Druhá úroveň: např. 'intercom', 'software', ...
            subcategory_keys = list(category_tree[selected_category].keys())
            selected_subcategory = st.selectbox("Choose subcategory", ["All"] + subcategory_keys)
        else:
            selected_subcategory = "Other"
        return start_date, end_date, selected_country, selected_category, selected_subcategory




