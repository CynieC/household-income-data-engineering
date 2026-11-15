import pandas as pd

# Load the original dataset
prepared_data = pd.read_csv(
    "data/raw/diaries_transactions_all.csv",
    low_memory=False
)

# Create a working copy
prepared_data_copy = prepared_data.copy()

# Inspect the working dataset
print("Original shape:", prepared_data.shape)
print("Prepared shape:", prepared_data_copy.shape)

print(prepared_data.dtypes)

# Convert date columns to datetime

date_columns = [
    "first_trx_date_hh",
    "last_trx_date_hh",
    "int_date",
    "first_int_date",
    "first_trx_date_acc",
    "last_trx_date_acc",
    "trx_date"
]

for column in date_columns:
    prepared_data[column] = pd.to_datetime(
        prepared_data[column],
        format="%d%b%Y",
        errors="coerce"
    )

# Check the converted columns
print(prepared_data[date_columns].dtypes)

# Check for dates that failed conversion
print(prepared_data[date_columns].isna().sum())
#confirm it has picked the correct dates for the columns
print(prepared_data.head())


# Columns that represent identifiers
id_columns = [
    "hh_ids",
    "account_ids",
    "m_ids_owner",
    "m_ids_trx",
    "trx_id"
]

# Convert identifiers to strings
for column in id_columns:
    prepared_data[column] = prepared_data[column].astype("string")

# Verify the changes
print(prepared_data[id_columns].dtypes)

print(prepared_data["account_startclose_balance"].dropna().value_counts().head(20))

print(prepared_data["trx_inkind_units"].dropna().value_counts().head(20))

prepared_data["account_startclose_balance"] = (
    prepared_data["account_startclose_balance"].astype("string")
)

print(prepared_data["account_startclose_balance"].dtype)

# Convert categorical columns to string
prepared_data["account_startclose_balance"] = (
    prepared_data["account_startclose_balance"].astype("string")
)

prepared_data["trx_inkind_units"] = (
    prepared_data["trx_inkind_units"].astype("string")
)

# Check data types
print(prepared_data[
    ["account_startclose_balance", "trx_inkind_units"]
].dtypes)

#save as csv
prepared_data.to_csv("data/processed/household_data_prepared.csv", index=False)
