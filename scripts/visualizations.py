from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# LOAD CLEANED DATA
# -----------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

cleaned_data_path = BASE_DIR / "data" / "cleaned_amazon.csv"

df = pd.read_csv(cleaned_data_path)

# -----------------------------
# TOP CATEGORY RATINGS
# -----------------------------

top_categories = (
    df.groupby("category")["rating"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

# -----------------------------
# CREATE CHART
# -----------------------------

plt.figure(figsize=(18, 10))

top_categories.plot(kind="barh")

plt.title("Top 10 Highest Rated Categories")
plt.xlabel("Average Rating")
plt.ylabel("Category")

plt.tight_layout()

# -----------------------------
# SAVE IMAGE
# -----------------------------

chart_path = BASE_DIR / "screenshots" / "top_categories.png"

plt.savefig(chart_path)

print("Chart saved successfully.")