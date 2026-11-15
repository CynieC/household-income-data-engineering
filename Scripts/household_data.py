import pandas as pd
import numpy as np
ImportWarning

household_data=pd.read_csv("Scripts/diaries_transactions_all.csv")
import pandas as pd

print(household_data.shape)

print(household_data.head())

print(household_data.tail())

# 2. Inspect the columns
print(household_data.columns.tolist())

# 3. Check data types
print(household_data.dtypes)

# 4. Check missing values
print(household_data.isnull().sum())

# 5. Check duplicate transactions
print(household_data.duplicated().sum())

# 6. Inspect transaction directions
print(household_data['trx_direction'].value_counts(dropna=False))

# 7. Summary of transaction values
print(household_data['trx_value_kes'].describe())

print("Duplicate rows:",household_data.duplicated().sum())

print("Duplicate transaction IDs:",household_data["trx_id"].duplicated().sum())

# Check negative transaction values
print(household_data[household_data["trx_value_kes"] < 0].shape)

# Check transactions above KES 100,000
print(household_data[household_data["trx_value_kes"] > 100000].shape)

# Check transaction date range
print(household_data["trx_date"].min())
print(household_data["trx_date"].max())

# Count distinct duplicated transaction IDs
duplicate_ids = household_data[household_data["trx_id"].duplicated(keep=False)]

print("Distinct duplicated IDs:", duplicate_ids["trx_id"].nunique())

# Inspect the first 10 duplicated transaction IDs
print(duplicate_ids[[
    "trx_id",
    "hh_ids",
    "account_ids",
    "trx_date",
    "trx_value_kes",
    "trx_direction"
]].head(10))

negative_transactions = household_data[household_data["trx_value_kes"] < 0]

print(negative_transactions[[
    "trx_id",
    "trx_value_kes",
    "trx_direction",
    "trx_class_desc",
    "trx_type_desc"
]].head(20))

# Select one duplicated transaction ID
sample_id = household_data.loc[
    household_data["trx_id"].duplicated(),
    "trx_id"
].iloc[0]

# Display all records with that transaction ID
sample = household_data[household_data["trx_id"] == sample_id]

print(sample[[
    "trx_id",
    "hh_ids",
    "account_ids",
    "trx_date",
    "trx_value_kes",
    "trx_direction",
    "trx_type_desc"
]].to_string(index=False))

# Examine how many distinct values exist per transaction ID
duplicate_summary = (
    household_data.groupby("trx_id")
    .agg(
        row_count=("trx_id", "size"),
        households=("hh_ids", "nunique"),
        accounts=("account_ids", "nunique"),
        dates=("trx_date", "nunique"),
        amounts=("trx_value_kes", "nunique")
    )
    .query("row_count > 1")
)

print(duplicate_summary.head(10))

# Select a transaction ID that appears 15 times
sample_id = 34135725435400000

# Retrieve all records for this ID
sample_records = household_data[household_data["trx_id"] == sample_id]

# Display relevant transaction details
print(sample_records[[
    "trx_id",
    "hh_ids",
    "account_ids",
    "trx_date",
    "trx_month",
    "trx_year",
    "trx_dq_round",
    "trx_value_kes",
    "trx_direction",
    "trx_class_desc",
    "trx_family_desc",
    "trx_type_desc",
    "trx_stdtime_days_hh"
]].sort_values("trx_date").to_string(index=False))

same_day = (
    household_data.groupby(["trx_id", "trx_date"])
    .size()
    .reset_index(name="records")
)

print(same_day[same_day["records"] > 1].head(20))

sample_id = 34135887383800000

sample = household_data[household_data["trx_id"] == sample_id]

print(
    sample[
        [
            "trx_id",
            "hh_ids",
            "account_ids",
            "trx_date",
            "trx_value_kes",
            "trx_direction",
            "trx_class_desc",
            "trx_family_desc",
            "trx_type_desc",
            "trx_dq_round",
            "trx_stdtime_days_hh"
        ]
    ].sort_values("trx_date").to_string(index=False)
)

sample = household_data[household_data["trx_id"] == 34135887383800000]

print(sample.T.to_string())

duplicate_analysis = (
    household_data[household_data["trx_id"].duplicated(keep=False)]
    .groupby("trx_id")
    .agg(
        records=("trx_id", "size"),
        unique_amounts=("trx_value_kes", "nunique"),
        unique_dates=("trx_date", "nunique"),
        unique_households=("hh_ids", "nunique"),
        unique_accounts=("account_ids", "nunique"),
        unique_types=("trx_type_desc", "nunique"),
        unique_directions=("trx_direction", "nunique")
    )
    .reset_index()
)

print(duplicate_analysis.describe())
print(
    household_data.groupby("trx_direction", dropna=False)
    ["trx_value_kes"]
    .agg(["count", "sum", "mean"])
)

print("Missing household IDs:", household_data["hh_ids"].isna().sum())
print("Unique households:", household_data["hh_ids"].nunique())

print("Missing account IDs:", household_data["account_ids"].isna().sum())
print("Unique accounts:", household_data["account_ids"].nunique())

print("HH account records:", (household_data["account_ids"] == "HH").sum())

household_data["trx_date_clean"] = pd.to_datetime(
    household_data["trx_date"],
    format="%d%b%Y",
    errors="coerce"
)

print("Invalid dates:", household_data["trx_date_clean"].isna().sum())
print("Earliest date:", household_data["trx_date_clean"].min())
print("Latest date:", household_data["trx_date_clean"].max())

print("Missing amounts:", household_data["trx_value_kes"].isna().sum())
print("Zero amounts:", (household_data["trx_value_kes"] == 0).sum())
print("Negative amounts:", (household_data["trx_value_kes"] < 0).sum())
print("Amounts above 100,000:", (household_data["trx_value_kes"] > 100000).sum())