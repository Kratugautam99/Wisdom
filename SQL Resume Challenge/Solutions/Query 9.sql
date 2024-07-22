with temp1 as (select fact_sales_monthly.product_code, fact_sales_monthly.customer_code, fact_sales_monthly.fiscal_year, 
fact_sales_monthly.sold_quantity, fact_gross_price.gross_price from fact_sales_monthly 
join fact_gross_price on fact_sales_monthly.product_code = fact_gross_price.product_code),
temp2 as (select dim_customer.channel, sum(gross_price*sold_quantity) as gross_price_mln 
from temp1 join dim_customer on dim_customer.customer_code = temp1.customer_code 
where fiscal_year = 2021 group by dim_customer.channel)
select channel, gross_price_mln, (gross_price_mln*100/3177769991.4) as percentage from temp2;
