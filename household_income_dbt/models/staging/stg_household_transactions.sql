SELECT *
FROM {{ source('household_data', 'household_transactions') }}