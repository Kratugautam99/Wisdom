with pro2020 as (select distinct segment, count(product) as product_count_2020 from dim_product t1 join fact_sales_monthly t2 on t1.product_code = t2.product_code where fiscal_year = 2020 group by segment),
pro2021 as (select distinct segment, count(product) as product_count_2021 from dim_product t3 join fact_sales_monthly t4 on t3.product_code = t4.product_code where fiscal_year group by segment)
select t1.segment, product_count_2021, product_count_2020, (product_count_2021-product_count_2020) 
as difference from pro2020 t1 join pro2021 t2 
on t1.segment = t2.segment order by difference desc;
