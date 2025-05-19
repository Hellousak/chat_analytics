import pandas as pd
import plotly.express as px
import altair as alt
from collections import defaultdict
import streamlit as st
from config import category_tree


def show_map(df):
    country_counts = df["session_country_name"].value_counts().reset_index()
    country_counts.columns = ["session_country_name", "count"]

    fig = px.choropleth(
        country_counts,
        locations="session_country_name",
        locationmode="country names",
        color="count",
        color_continuous_scale="Purples",
        title="Chats according to the country"
    )

    fig.update_geos(
        showcountries=True,
        showframe=False,
        lataxis_range=[35, 70],  # výška (latitude)
        lonaxis_range=[-15, 40]  # šířka (longitude)
    )

    fig.update_layout(
        margin={"r":0, "t":50, "l":0, "b":0},
        title_x=0.65
    )

    st.plotly_chart(fig)


def show_tags_chart(df, selected_country, selected_category, selected_subcategory):


    tag_counter = defaultdict(list)

    # Filtrování podle země
    if selected_country != "All":
        df = df[df["session_country_name"] == selected_country]

    # Procházení kategorií a sběr tagů
    for categories in df["categorized_tags"]:
        for cat, tags in categories.items():
            tag_counter[cat].extend(tags)

    # Výběr tagů
    if selected_category == "All":
        all_tags = sum(tag_counter.values(), [])
    else:
        all_tags = tag_counter[selected_category]

    # Filtrace podle subkategorie
    if selected_subcategory != "All":
        allowed_tags = category_tree["Product"].get(selected_subcategory, [])
        all_tags = [tag for tag in all_tags if tag in allowed_tags]

    # Spočítání výskytu
    tag_freq = pd.Series(all_tags).value_counts().head(50)
    tag_df = tag_freq.reset_index()
    tag_df.columns = ["tag", "count"]
    tag_df["index"] = tag_df.index
    colors = ["#211C84", "#4D55CC", "#7A73D1", "#B5A8D5"]
    tag_df["color"] = tag_df["index"].map(lambda i: colors[i % len(colors)])

    chart = (
        alt.Chart(tag_df)
        .mark_bar()
        .encode(
            x=alt.X("count", title="Number of chats"),
            y=alt.Y("tag:N", sort='-x', title="Topic"),
            color=alt.Color("color:N", scale=None, legend=None)
        )
    )

    st.altair_chart(chart, use_container_width=True)

