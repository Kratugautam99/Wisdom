select * from fact_gross_price order by fiscal_year asc;
with temp as (select month(fact_sales_monthly.date) as month, 
fiscal_year as year, dim_customer.customer_code,fact_sales_monthly.product_code 
from fact_sales_monthly join dim_customer on fact_sales_monthly.customer_code = dim_customer.customer_code 
where dim_customer.customer like 'Atliq Exclusive'),
temp1 as (select month,year,fact_gross_price.gross_price from temp join fact_gross_price 
on fact_gross_price.product_code = temp.product_code)
select * from temp1 order by year,month asc;