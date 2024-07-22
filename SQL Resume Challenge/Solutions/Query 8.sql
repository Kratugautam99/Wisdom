select (floor((month(date)-1)/3) + 1) as quarter, sum(sold_quantity) 
from fact_sales_monthly where fiscal_year=2020 group by quarter;
select * from fact_sales_monthly;
