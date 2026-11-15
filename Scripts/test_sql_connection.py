import pyodbc

connection_string = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=CYNIE\\SQLEXPRESS;"
    "DATABASE=dbt_household_data;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

try:
    connection = pyodbc.connect(connection_string)

    print("Connection successful!")

    cursor = connection.cursor()
    cursor.execute("SELECT DB_NAME()")

    print("Connected database:", cursor.fetchone()[0])

    connection.close()

except Exception as e:
    print("Connection failed:", e)

