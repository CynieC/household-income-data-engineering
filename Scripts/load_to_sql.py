import pandas as pd
from sqlalchemy import create_engine, URL

# 1. Read prepared data
file_path = "data/processed/household_data_prepared.csv"

date_columns = [
    "first_trx_date_hh",
    "last_trx_date_hh",
    "int_date",
    "first_int_date",
    "first_trx_date_acc",
    "last_trx_date_acc",
    "trx_date"
]

id_columns = [
    "hh_ids",
    "account_ids",
    "m_ids_owner",
    "m_ids_trx",
    "trx_id"
]

string_columns = id_columns + [
    "account_startclose_balance",
    "trx_inkind_units"
]

df = pd.read_csv(
    file_path,
    low_memory=False,
    dtype={column: "string" for column in string_columns},
    parse_dates=date_columns
)

print("Records to load:", len(df))

# 2. Create SQL Server connection
connection_url = URL.create(
    "mssql+pyodbc",
    host=r"CYNIE\SQLEXPRESS",
    database="dbt_household_data",
    query={
        "driver": "ODBC Driver 18 for SQL Server",
        "trusted_connection": "yes",
        "TrustServerCertificate": "yes"
    }
)

engine = create_engine(
    connection_url,
    fast_executemany=True
)

# 3. Load data into SQL Server
df.to_sql(
    name="household_transactions",
    con=engine,
    schema="dbo",
    if_exists="replace",
    index=False,
    chunksize=5000
)

# 4. Validate the load
with engine.connect() as connection:
    result = connection.exec_driver_sql(
        "SELECT COUNT_BIG(*) FROM dbo.household_transactions"
    )

    sql_count = result.scalar_one()

print("Records loaded into SQL Server:", sql_count)

engine.dispose()