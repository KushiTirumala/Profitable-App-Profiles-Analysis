
---



import pandas as pd

# Load datasets
google_play = pd.read_csv("google_play_store.csv")
app_store = pd.read_csv("app_store.csv")

# Display dataset info
print("Google Play Dataset Info:")
print(google_play.info())

print("\nApp Store Dataset Info:")
print(app_store.info())

# Clean Google Play dataset
google_play.dropna(subset=["Category", "Installs"], inplace=True)
google_play["Installs"] = google_play["Installs"].str.replace('[+,]', '', regex=True)
google_play["Installs"] = pd.to_numeric(google_play["Installs"], errors="coerce")

# Frequency table for Google Play categories
gp_category_freq = google_play["Category"].value_counts(normalize=True) * 100
print("\nGoogle Play Category Distribution (%):")
print(gp_category_freq)

# Average installs by category
gp_avg_installs = google_play.groupby("Category")["Installs"].mean().sort_values(ascending=False)
print("\nAverage Installs by Category (Google Play):")
print(gp_avg_installs)

# Clean App Store dataset
app_store.dropna(subset=["prime_genre"], inplace=True)

# Frequency table for App Store categories
as_category_freq = app_store["prime_genre"].value_counts(normalize=True) * 100
print("\nApp Store Category Distribution (%):")
print(as_category_freq)

# Average user rating by category
as_avg_rating = app_store.groupby("prime_genre")["user_rating"].mean().sort_values(ascending=False)
print("\nAverage User Rating by Category (App Store):")
print(as_avg_rating)

# Business Recommendations
print("\nBusiness Insights & Recommendations:")
print("- Focus on categories with high installs and balanced competition.")
print("- Lifestyle, Productivity, and Education apps show strong engagement.")
print("- Monetization opportunities exist in niche but high-rating categories.")
