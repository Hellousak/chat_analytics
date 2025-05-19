from data_loader import upload_and_load_data, filter_data
from layout import show_filters, show_header
from charts import show_map, show_tags_chart

# Načtení dat
df = upload_and_load_data()

# Layout - filtry nahoře
start_date, end_date, selected_country, selected_category, selected_subcategory = show_filters(df)


# Filtrování
filtered_df = filter_data(df, start_date, end_date)

# Header info
show_header(filtered_df, start_date, end_date)

# Mapa
show_map(filtered_df)

# Tagy graf

if selected_category == "Product":
    show_tags_chart(filtered_df, selected_country, selected_category, selected_subcategory)
else:
    show_tags_chart(filtered_df, selected_country, selected_category, "All")
