
    
    -- Create target schema if it does not
  USE [dbt_household_data];
  IF NOT EXISTS (SELECT * FROM sys.schemas WHERE name = 'dbo')
  BEGIN
    EXEC('CREATE SCHEMA [dbo]')
  END

  

  
  EXEC('create view 
    [dbo].[testview_1fb327a8e7fb6aa270165f81fc3c992e_2925]
   as 
    
    
    



select hh_ids
from "dbt_household_data"."dbo"."household_transactions"
where hh_ids is null



  ;')
  select
    
    count(*) as failures,
    case when count(*) != 0
      then 'true' else 'false' end as should_warn,
    case when count(*) != 0
      then 'true' else 'false' end as should_error
  from (
    select * from 
    [dbo].[testview_1fb327a8e7fb6aa270165f81fc3c992e_2925]
  
  ) dbt_internal_test;

  EXEC('drop view 
    [dbo].[testview_1fb327a8e7fb6aa270165f81fc3c992e_2925]
  ;')