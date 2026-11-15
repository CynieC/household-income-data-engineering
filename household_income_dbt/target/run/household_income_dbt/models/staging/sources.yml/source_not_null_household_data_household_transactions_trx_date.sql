
    
    -- Create target schema if it does not
  USE [dbt_household_data];
  IF NOT EXISTS (SELECT * FROM sys.schemas WHERE name = 'dbo')
  BEGIN
    EXEC('CREATE SCHEMA [dbo]')
  END

  

  
  EXEC('create view 
    [dbo].[testview_03b9c5a12360e04045d08b8ca6c0c808_1561]
   as 
    
    
    



select trx_date
from "dbt_household_data"."dbo"."household_transactions"
where trx_date is null



  ;')
  select
    
    count(*) as failures,
    case when count(*) != 0
      then 'true' else 'false' end as should_warn,
    case when count(*) != 0
      then 'true' else 'false' end as should_error
  from (
    select * from 
    [dbo].[testview_03b9c5a12360e04045d08b8ca6c0c808_1561]
  
  ) dbt_internal_test;

  EXEC('drop view 
    [dbo].[testview_03b9c5a12360e04045d08b8ca6c0c808_1561]
  ;')