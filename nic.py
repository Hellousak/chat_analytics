import pandas as pd

# Vytvoříme testovací tabulku
data = {
    "ID": [1, 2, 3, 4],
    "session_country_name": ["Germany", "Czechia", None, "Austria"],
    "tags": [["f_send"], None, ["s_fix"], ["f_pdf"]]
}

df = pd.DataFrame(data)

print("📋 Původní tabulka:")
print(df)

# Použijeme dropna na konkrétní sloupce
df_clean = df.dropna()

print("\n✅ Vyčištěná tabulka (dropna se subsetem):")
print(df_clean)
