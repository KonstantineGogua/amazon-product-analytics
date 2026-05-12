from pathlib import Path
import pandas as pd

# -----------------------------
# LOAD DATA
# -----------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

raw_data_path = BASE_DIR / "data" / "amazon.csv"
cleaned_data_path = BASE_DIR / "data" / "cleaned_amazon.csv"

df = pd.read_csv(raw_data_path)

print("Raw dataset loaded successfully.")
print(df.head())
print(df.info())


# -----------------------------
# CLEAN DATA
# -----------------------------

df["discounted_price"] = (
    df["discounted_price"]
    .str.replace("₹", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(float)
)

df["actual_price"] = (
    df["actual_price"]
    .str.replace("₹", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(float)
)

df["discount_percentage"] = (
    df["discount_percentage"]
    .str.replace("%", "", regex=False)
    .astype(float)
)

df["rating"] = pd.to_numeric(df["rating"], errors="coerce")

df["rating_count"] = (
    df["rating_count"]
    .astype(str)
    .str.replace(",", "", regex=False)
)

df["rating_count"] = pd.to_numeric(df["rating_count"], errors="coerce")


# -----------------------------
# FEATURE ENGINEERING
# -----------------------------

df["savings"] = df["actual_price"] - df["discounted_price"]

df["savings_percentage"] = (
    df["savings"] / df["actual_price"]
) * 100


# -----------------------------
# HANDLE MISSING VALUES
# -----------------------------

df = df.dropna(subset=["rating", "rating_count"])

# -----------------------------
# CLEAN CATEGORY NAMES
# -----------------------------

df["main_category"] = (
    df["category"]
    .str.split("|")
    .str[0]
)


# -----------------------------
# SAVE CLEANED DATA
# -----------------------------

df.to_csv(cleaned_data_path, index=False)

print("\nCleaned dataset saved successfully.")
print(f"Saved to: {cleaned_data_path}")


# -----------------------------
# BUSINESS ANALYSIS
# -----------------------------

print("\nTop 10 Highest Rated Categories:")
top_categories = (
    df.groupby("category")["rating"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)
print(top_categories)


print("\nTop 10 Most Reviewed Products:")
top_reviewed = (
    df[["product_name", "rating_count"]]
    .sort_values(by="rating_count", ascending=False)
    .head(10)
)
print(top_reviewed)


print("\nAverage Discount By Category:")
discount_analysis = (
    df.groupby("category")["discount_percentage"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)
print(discount_analysis)


print("\nFinal Dataset Info:")
print(df.info())
# -----------------------------
# CREATE SQL-FRIENDLY CSV
# -----------------------------

sql_export_path = BASE_DIR / "data" / "cleaned_amazon_sql.csv"

# Keep only columns needed for SQL analysis
sql_df = df[
    [
        "product_id",
        "product_name",
        "category",
        "discounted_price",
        "actual_price",
        "discount_percentage",
        "rating",
        "rating_count",
        "savings",
        "savings_percentage"
    ]
].copy()

# Remove problematic special characters from text columns
for col in ["product_id", "product_name", "category"]:
    sql_df[col] = (
        sql_df[col]
        .astype(str)
        .str.encode("ascii", errors="ignore")
        .str.decode("ascii")
    )

sql_df.to_csv(sql_export_path, index=False, encoding="utf-8")

print("SQL-friendly dataset saved successfully.")
print(f"Saved to: {sql_export_path}")

