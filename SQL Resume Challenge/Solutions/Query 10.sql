with temp1 as (select dim_product.product_code, division, product, 
sum(sold_quantity) as total_sold_quantity from dim_product join fact_sales_monthly
on dim_product.product_code = fact_sales_monthly.product_code where fiscal_year = 2021 
group by dim_product.product_code, product, division 
), temp2 as (select *,row_number() over (partition by division 
order by total_sold_quantity desc) as rank_order from temp1)
select * from temp2 where rank_order<=3;
