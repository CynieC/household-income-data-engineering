
  
    USE [dbt_household_data];
    USE [dbt_household_data];
    
    

    

    
    USE [dbt_household_data];
    EXEC('
        CREATE OR ALTER VIEW "dbo"."mart_household_monthly_cashflow__dbt_tmp__dbt_tmp_vw" AS SELECT
    hh_ids,

    DATEFROMPARTS(
        YEAR(trx_date),
        MONTH(trx_date),
        1
    ) AS month_start,

    SUM(
        CASE
            WHEN trx_direction = ''Inflow''
            THEN trx_value_kes
            ELSE 0
        END
    ) AS total_inflows_kes,

    SUM(
        CASE
            WHEN trx_direction = ''Outflow''
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
    );
    ')

EXEC('
            SELECT * INTO "dbt_household_data"."dbo"."mart_household_monthly_cashflow__dbt_tmp" FROM "dbt_household_data"."dbo"."mart_household_monthly_cashflow__dbt_tmp__dbt_tmp_vw" 
    OPTION (LABEL = ''dbt-sqlserver'');

        ')

    
    EXEC('DROP VIEW IF EXISTS "dbo"."mart_household_monthly_cashflow__dbt_tmp__dbt_tmp_vw"')



    
    use [dbt_household_data];
    if EXISTS (
        SELECT *
        FROM sys.indexes with (nolock)
        WHERE name = 'dbo_mart_household_monthly_cashflow__dbt_tmp_cci'
        AND object_id=object_id('dbo_mart_household_monthly_cashflow__dbt_tmp')
    )
    DROP index "dbo"."mart_household_monthly_cashflow__dbt_tmp".dbo_mart_household_monthly_cashflow__dbt_tmp_cci
    CREATE CLUSTERED COLUMNSTORE INDEX dbo_mart_household_monthly_cashflow__dbt_tmp_cci
    ON "dbo"."mart_household_monthly_cashflow__dbt_tmp"

   


  