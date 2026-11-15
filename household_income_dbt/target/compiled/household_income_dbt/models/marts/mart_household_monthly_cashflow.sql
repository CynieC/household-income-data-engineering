SELECT
    hh_ids,

    DATEFROMPARTS(
        YEAR(trx_date),
        MONTH(trx_date),
        1
    ) AS month_start,

    SUM(
        CASE
            WHEN trx_direction = 'Inflow'
            THEN trx_value_kes
            ELSE 0
        END
    ) AS total_inflows_kes,

    SUM(
        CASE
            WHEN trx_direction = 'Outflow'
            THEN trx_value_kes
            ELSE 0
        END
    ) AS total_outflows_kes,

    SUM(
        CASE
            WHEN trx_direction IS NULL
            THEN trx_value_kes
            ELSE 0
        END
    ) AS unknown_direction_amount_kes,

    COUNT(*) AS transaction_count

FROM "dbt_household_data"."dbo"."stg_household_transactions"

GROUP BY
    hh_ids,
    DATEFROMPARTS(
        YEAR(trx_date),
        MONTH(trx_date),
        1
    )