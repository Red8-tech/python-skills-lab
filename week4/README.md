# Week 4 — pandas and Messy Data

Week 4 focuses on practical data analysis and cleaning using **Python and pandas**. The objective was to learn how to take a messy CSV dataset, inspect its structure, identify data-quality issues, clean inconsistent values, perform analysis, and communicate the results in plain English.

A customer-sales dataset was used to simulate a real-world data-cleaning task. The dataset contained missing values, duplicate records, inconsistent text formats, incorrect data types, and suspicious purchase amounts.

The main goal was to develop a repeatable workflow for transforming raw data into a more consistent and analysis-ready dataset without blindly deleting potentially useful information.

## Learning Objectives

- Load and inspect CSV files using pandas.
- Understand dataset dimensions, data types, and statistical summaries.
- Identify missing values and duplicate records.
- Standardize inconsistent text and categorical values.
- Convert columns to appropriate data types.
- Investigate invalid values and suspicious outliers.
- Filter records using Boolean conditions.
- Create derived columns and categorical groups.
- Perform grouped analysis and statistical aggregation.
- Combine datasets using pandas merge operations.
- Export cleaned data to a new CSV file.
- Summarize findings and explain analytical limitations.

## Tools and Technologies

- **Python** — programming language used for data processing.
- **pandas** — data manipulation, cleaning, filtering, and analysis.
- **CSV** — input and output data format.
- **PowerShell** — project setup and script execution.
- **Visual Studio Code** — code editing and project management.

## Project Structure

```text
week4/
├── data/
│   ├── raw/
│   │   └── messy_customer_sales_data.csv
│   └── cleaned_customer_sales.csv
├── scripts/
│   └── explore_data.py
├── findings.md
└── README.md
```

### Folder Description

- `data/raw/` — stores the original dataset. The raw file is preserved so the cleaning process can be reproduced.
- `data/cleaned_customer_sales.csv` — contains the cleaned customer-sales dataset exported from pandas.
- `scripts/explore_data.py` — contains the code for loading, inspecting, cleaning, transforming, analysing, and exporting the data.
- `findings.md` — documents the main analytical results and their limitations.
- `README.md` — describes the project's purpose, workflow, techniques, and learning outcomes.

## Dataset Overview

The project uses a customer-sales dataset with **10,200 initial rows and 12 columns**.

| Column | Description |
|---|---|
| `Customer_ID` | Customer identifier |
| `Name` | Customer name |
| `Gender` | Customer gender |
| `Age` | Customer age |
| `City` | Customer's city |
| `Signup_Date` | Customer registration date |
| `Last_Purchase_Date` | Date of the most recent purchase |
| `Purchase_Amount` | Recorded purchase amount |
| `Feedback_Score` | Customer feedback score |
| `Email` | Customer email address |
| `Phone_Number` | Customer phone number |
| `Country` | Customer's country |

The initial inspection showed that several columns contained missing values. Some columns also used inconsistent representations, and certain numeric fields required further validation.

## 1. Loading and Inspecting Data

The dataset was loaded using `pandas.read_csv()`.

The following methods were used to understand its structure:

- `head()` — previewed the first five rows.
- `shape` — returned the number of rows and columns.
- `info()` — displayed column types and non-null counts.
- `describe()` — summarised numerical columns.
- `value_counts()` — examined the distribution of categorical values.
- `isna().sum()` — counted missing values in each column.
- `duplicated().sum()` — counted exact duplicate rows.

### Initial Observations

- The dataset contained 10,200 rows and 12 columns.
- Several columns had approximately 1,000 missing entries.
- The `Age` column was stored as an object rather than a numeric type.
- Gender, city, and country values used inconsistent capitalization and formatting.
- Purchase amounts included negative values and unusually large values.
- Fifteen exact duplicate rows were identified.

This initial inspection helped determine which cleaning operations were necessary.

## 2. Handling Missing Values

Missing values were investigated before deciding how to handle them.

The following method was used:

```python
df.isna().sum()
```

Missing values were present in columns such as `Customer_ID`, `Gender`, `Age`, `City`, `Last_Purchase_Date`, `Purchase_Amount`, `Feedback_Score`, and `Country`.

Instead of filling every missing value with zero or the mean, the project treated missingness according to the meaning of each field.

For example:

- A missing feedback score does not mean the customer gave a score of zero.
- A missing age does not automatically justify assigning the average age.
- A missing customer ID can make reliable customer-level matching difficult.

Invalid age strings such as `"nan years"` were also identified during conversion. These values were treated as missing rather than being interpreted as valid numeric ages.

## 3. Removing Duplicate Records

Exact duplicate rows were identified using:

```python
df.duplicated().sum()
```

Fifteen exact duplicates were removed with:

```python
clean_df = clean_df.drop_duplicates()
```

The cleaned DataFrame was created from a copy of the original:

```python
clean_df = df.copy()
```

This preserved the raw data for comparison and reproducibility.

After removing the 15 exact duplicates, the dataset contained **10,185 rows**.

Only exact duplicate rows were removed. Records sharing a customer ID were not automatically deleted because a customer may legitimately appear in multiple records.

## 4. Standardizing Inconsistent Text

Categorical values were inspected using `value_counts()`.

### Gender

The raw dataset contained variations such as:

- `M`, `m`, `MALE`, `male`
- `F`, `f`, `female`, `FEMALE`

These were standardized to `Male` and `Female`.

### City

City values included inconsistent capitalization and leading spaces. Text-cleaning methods were used to standardize the values.

```python
clean_df["City"] = (
    clean_df["City"]
    .astype("string")
    .str.strip()
    .str.title()
)
```

### Country

Country values such as `India`, `india`, `InDia`, and `IND` were mapped to the common label `India`.

These operations reduced inconsistent category labels and made grouped analysis more reliable.

## 5. Converting Data Types

The `Age` column was initially stored as an object, with values including strings such as `"30.0 years"`.

The text was cleaned before numeric conversion:

```python
age_text = (
    df["Age"]
    .astype("string")
    .str.strip()
    .str.lower()
)

age_text = age_text.str.replace(
    r"\s*years?\s*$",
    "",
    regex=True
)

clean_df["Age"] = pd.to_numeric(
    age_text,
    errors="coerce"
)
```

The `errors="coerce"` option converted values that could not be parsed into missing values rather than raising an exception.

A further validation step identified ages below zero or above 100. Those values were treated as invalid for this exercise.

This demonstrated why cleaning text and converting data types should be performed before numerical analysis.

## 6. Investigating Suspicious Purchase Amounts

The `Purchase_Amount` column contained several unusual values.

The analysis identified:

- Four negative purchase amounts of `-500`.
- Four extremely high purchase amounts of `9,999,999`.
- Some zero-value purchases.

Rather than immediately deleting these records, a flag was created for unusually high purchases:

```python
clean_df["High_Purchase_Flag"] = (
    clean_df["Purchase_Amount"] > 100000
)
```

This kept the original recorded values available for further investigation.

For the city and age-group analyses, negative purchases and flagged high-value purchases were excluded from the filtered dataset. These records were not removed from the cleaned DataFrame itself.

Negative values could represent refunds, while unusually large values could be errors or legitimate exceptional transactions. Their final treatment would require confirmation of the business rules.

## 7. Creating New Columns

A new categorical column, `Age_Group`, was created using `pd.cut()`.

The age groups were:

- 18–25
- 26–40
- 41–60
- 61–100

This made it possible to compare purchase amounts across age categories rather than analysing every individual age separately.

A `High_Purchase_Flag` column was also added to identify transactions above the chosen investigation threshold.

Derived columns help transform raw fields into features that are easier to analyse and interpret.

## 8. Filtering Records

Boolean conditions were used to create a filtered dataset for purchase analysis.

The analysis included records where:

- `Purchase_Amount` was not missing.
- `Purchase_Amount` was greater than or equal to zero.
- `High_Purchase_Flag` was false.

This resulted in **9,157 filtered purchase records**.

The filtered dataset was used only for the relevant analysis. The original cleaned DataFrame retained the flagged transactions so that potentially important records were not silently lost.

## 9. Grouping and Aggregation

The `groupby()` and `agg()` methods were used to compare purchase amounts across cities and age groups.

### Purchase Analysis by City

The analysis calculated:

- Record count
- Average purchase amount
- Median purchase amount

| City | Records | Average Purchase | Median Purchase |
|---|---:|---:|---:|
| Bangalore | 1,372 | ₹25,383.10 | ₹25,267.50 |
| Chennai | 1,361 | ₹23,962.89 | ₹22,973.00 |
| Delhi | 1,368 | ₹25,170.40 | ₹24,346.50 |
| Hyderabad | 1,357 | ₹25,152.82 | ₹24,505.00 |
| Kolkata | 1,386 | ₹24,199.75 | ₹23,781.00 |
| Mumbai | 1,403 | ₹24,779.39 | ₹25,387.00 |

**Finding:** Bangalore had the highest average purchase amount at ₹25,383.10, while Chennai had the lowest at ₹23,962.89.

The median was also calculated because extreme values can affect the mean differently from the median.

### Purchase Analysis by Age Group

| Age Group | Records | Average Purchase |
|---|---:|---:|
| 18–25 | 1,240 | ₹24,299.33 |
| 26–40 | 2,388 | ₹24,972.10 |
| 41–60 | 3,135 | ₹24,692.84 |
| 61–100 | 1,470 | ₹24,858.59 |

**Finding:** The 26–40 age group had the highest average purchase amount at ₹24,972.10.

The average purchase amounts were relatively close across the four age groups. These results alone do not demonstrate that age causes differences in purchasing behaviour.

## 10. Merging Datasets

A small simulated loyalty dataset was created with three columns:

- `Customer_ID`
- `Loyalty_Tier`
- `Points`

The customer-sales DataFrame and loyalty DataFrame were merged using `Customer_ID`.

```python
merged_df = clean_df.merge(
    loyalty_df,
    on="Customer_ID",
    how="left",
    indicator=True
)
```

A left join was used to preserve the rows from `clean_df`, including those without a matching loyalty record.

The `indicator=True` argument created a `_merge` column to identify whether a record matched.

### Merge Results

| Merge Status | Rows |
|---|---:|
| `both` | 5 |
| `left_only` | 10,180 |
| `right_only` | 0 |
| **Total** | **10,185** |

**Finding:** Five rows matched the simulated loyalty dataset, while 10,180 rows had no matching loyalty record.

This exercise demonstrated how to combine datasets and inspect unmatched records. Because the loyalty dataset was simulated and contained only five customer IDs, these figures should not be interpreted as actual customer loyalty coverage.

## 11. Exporting the Cleaned Dataset

The cleaned data was exported to a separate CSV file:

```python
CLEAN_PATH = (
    BASE_DIR
    / "data"
    / "cleaned_customer_sales.csv"
)

clean_df.to_csv(CLEAN_PATH, index=False)
```

The `index=False` argument prevented pandas from adding its DataFrame index as an extra CSV column.

The exported file was saved at:

```text
data/cleaned_customer_sales.csv
```

The original CSV remained in the raw data folder, allowing the cleaning process to be repeated without losing the original records.

## Key Learnings

By completing this project, I practised:

- Inspecting unfamiliar datasets before making changes.
- Identifying missing values, duplicates, and inconsistent categories.
- Standardizing text with pandas string methods.
- Converting text-based numeric fields into numeric types.
- Distinguishing invalid data from suspicious but potentially meaningful values.
- Creating derived columns and categorical age groups.
- Filtering records using multiple Boolean conditions.
- Calculating grouped statistics using `groupby()` and `agg()`.
- Combining DataFrames using a common key and a left join.
- Exporting a cleaned dataset to CSV.
- Explaining analytical results and limitations in plain English.

## Limitations and Considerations

- The loyalty dataset was simulated and was not a real business dataset.
- The merge results reflect a deliberately small lookup dataset, not real customer loyalty coverage.
- Negative and unusually high purchase amounts were excluded from the filtered purchase analyses, so the reported averages do not represent every recorded purchase.
- The dataset may contain repeated customer IDs, meaning row counts should not automatically be interpreted as unique customer counts.
- Some missing information was retained rather than imputed.
- The analysis describes patterns in the available data; it does not establish causation.
- The threshold of ₹100,000 for flagging high purchases was selected for this exercise and would need business validation in a production setting.

## Conclusion

Week 4 provided hands-on experience in taking a messy CSV through inspection, cleaning, validation, transformation, analysis, merging, and export.

The project demonstrated that effective data analysis requires more than applying pandas functions. It also requires understanding the meaning of the data, making defensible cleaning decisions, preserving potentially useful records, and communicating findings with appropriate limitations.

The completed exercises provide a foundation for more advanced pandas work, exploratory data analysis, and real-world data-processing projects.
