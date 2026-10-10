from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "raw" / "messy_customer_sales_data.csv"

df = pd.read_csv(DATA_PATH)

print("First five rows:")
print(df.head())

print("\nDataset dimensions:")
print(df.shape)

print("\nColumn information:")
df.info()

print("\nNumerical summary:")
print(df.describe())

print("\nMissing values per column:")
print(df.isna().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("*" * 60)
print("*" * 60)



# 1. Inspect unique values in categorical columns
for column in ["Gender", "City", "Country"]:
    print(f"\n--- {column} ---")
    print(df[column].value_counts(dropna=False).head(20))

# 2. Investigate Age
print("\n--- Age values ---")
print(df["Age"].value_counts(dropna=False).head(20))

# 3. Investigate purchase amounts
print("\n--- Purchase amount extremes ---")
print(df["Purchase_Amount"].sort_values().head(10))
print(df["Purchase_Amount"].sort_values(ascending=False).head(10))

# 4. Investigate feedback scores
print("\n--- Feedback score distribution ---")
print(df["Feedback_Score"].value_counts(dropna=False).sort_index())

# 5. Preview exact duplicate records
print("\n--- Duplicate rows ---")
print(df[df.duplicated(keep=False)].head(10))

print("*" * 60)
print("*" * 60)



# Keep the raw data unchanged
clean_df = df.copy()

# 1. Remove exact duplicate rows
duplicates_before = clean_df.duplicated().sum()
clean_df = clean_df.drop_duplicates()

print("Exact duplicates removed:", duplicates_before)

# 2. Standardize Gender
clean_df["Gender"] = (
    clean_df["Gender"]
    .astype("string")
    .str.strip()
    .str.lower()
    .replace({
        "m": "Male",
        "male": "Male",
        "f": "Female",
        "female": "Female"
    })
)

# 3. Standardize City
clean_df["City"] = (
    clean_df["City"]
    .astype("string")
    .str.strip()
    .str.title()
)

# 4. Standardize Country
clean_df["Country"] = (
    clean_df["Country"]
    .astype("string")
    .str.strip()
    .str.lower()
    .replace({
        "india": "India",
        "ind": "India"
    })
)

# 5. Convert Age to a numeric type
clean_df["Age"] = pd.to_numeric(
    clean_df["Age"],
    errors="coerce"
)

print("\nGender after cleaning:")
print(clean_df["Gender"].value_counts(dropna=False))

print("\nCity after cleaning:")
print(clean_df["City"].value_counts(dropna=False))

print("\nCountry after cleaning:")
print(clean_df["Country"].value_counts(dropna=False))

print("\nAge data type:", clean_df["Age"].dtype)
print("Missing ages:", clean_df["Age"].isna().sum())

print("*" * 60)
print("*" * 60)



# Clean Age values such as "30.0 years"
age_text = (
    df["Age"]
    .astype("string")
    .str.strip()
    .str.lower()
)

# Remove the word "years", then convert to numeric
age_text = age_text.str.replace(
    r"\s*years?\s*$",
    "",
    regex=True
)

clean_df["Age"] = pd.to_numeric(
    age_text,
    errors="coerce"
)

# Ages outside the chosen valid range are treated as missing
invalid_age_mask = (
    (clean_df["Age"] < 0)
    | (clean_df["Age"] > 100)
)

clean_df.loc[invalid_age_mask, "Age"] = float("nan")

print("Missing ages after cleaning:", clean_df["Age"].isna().sum())
print("Age data type:", clean_df["Age"].dtype)
print(clean_df["Age"].describe())



# Count suspicious purchase amounts
print(
    "\nNegative purchases:",
    (clean_df["Purchase_Amount"] < 0).sum()
)
print(
    "Purchases equal to 9,999,999:",
    (clean_df["Purchase_Amount"] == 9999999).sum()
)

# Flag unusually high purchases for investigation
clean_df["High_Purchase_Flag"] = (
    clean_df["Purchase_Amount"] > 100000
)
print(
    clean_df["High_Purchase_Flag"].value_counts()
)

# Inspect negative purchases separately
print(
    clean_df.loc[
        clean_df["Purchase_Amount"] < 0,
        ["Customer_ID", "Purchase_Amount"]
    ]
)


# Check impossible ages
print(
    "Ages below 0 or above 100:",
    (
        (clean_df["Age"] < 0)
        | (clean_df["Age"] > 100)
    ).sum()
)

# Check invalid feedback scores
print(
    "Feedback scores outside 1–10:",
    (
        (clean_df["Feedback_Score"] < 1)
        | (clean_df["Feedback_Score"] > 10)
    ).sum()
)

# Inspect suspicious purchase records
print("\nSuspicious high-value purchases:")
print(
    clean_df.loc[
        clean_df["Purchase_Amount"] > 100000,
        ["Customer_ID", "Purchase_Amount", "City"]
    ].head(10)
)

print("*" * 60)
print("*" * 60)



# Clean Age values such as "30.0 years"
age_text = (
    df["Age"]
    .astype("string")
    .str.strip()
    .str.lower()
)

# Remove the word "years", then convert to numeric
age_text = age_text.str.replace(
    r"\s*years?\s*$",
    "",
    regex=True
)

clean_df["Age"] = pd.to_numeric(
    age_text,
    errors="coerce"
)

# Ages outside the chosen valid range are treated as missing
invalid_age_mask = (
    (clean_df["Age"] < 0)
    | (clean_df["Age"] > 100)
)

clean_df.loc[invalid_age_mask, "Age"] = float("nan")

print("Missing ages after cleaning:", clean_df["Age"].isna().sum())
print("Age data type:", clean_df["Age"].dtype)
print(clean_df["Age"].describe())

print("*" * 60)
print("*" * 60)



# Create age groups
clean_df["Age_Group"] = pd.cut(
    clean_df["Age"],
    bins=[0, 25, 40, 60, 100],
    labels=["18–25", "26–40", "41–60", "61–100"],
    include_lowest=True
)

# Filter valid, non-negative purchases
valid_purchases = clean_df[
    clean_df["Purchase_Amount"].notna()
    & (clean_df["Purchase_Amount"] >= 0)
    & (~clean_df["High_Purchase_Flag"])
]

print("\nValid purchase records:", len(valid_purchases))

print("\nAverage purchase by city:")
print(
    valid_purchases.groupby("City")["Purchase_Amount"]
    .agg(["count", "mean", "median"])
    .round(2)
)

print("\nAverage purchase by age group:")
print(
    valid_purchases.groupby("Age_Group", observed=True)
    ["Purchase_Amount"]
    .agg(["count", "mean"])
    .round(2)
)




print("*" * 60)
print("*" * 60)





# Create a second dataset containing customer loyalty information
loyalty_df = pd.DataFrame({
    "Customer_ID": [
        "CUST4371",
        "CUST5957",
        "CUST3754",
        "CUST2934",
        "CUST5683"
    ],
    "Loyalty_Tier": [
        "Gold",
        "Silver",
        "Bronze",
        "Gold",
        "Silver"
    ],
    "Points": [1200, 650, 300, 1500, 800]
})

# Merge the datasets using Customer_ID
merged_df = clean_df.merge(
    loyalty_df,
    on="Customer_ID",
    how="left",
    indicator=True
)

print("\nMerged data:")
print(
    merged_df[
        ["Customer_ID", "Name", "Loyalty_Tier", "Points", "_merge"]
    ].head(10)
)

print("\nMerge status:")
print(merged_df["_merge"].value_counts())





CLEAR_PATH = BASE_DIR / "data" / "cleaned_customer_sales.csv"
clean_df.to_csv(CLEAR_PATH, index=False)

print(f"\nCleaned dataset saved to: {CLEAR_PATH}")
