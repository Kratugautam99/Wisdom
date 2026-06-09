update fact_sales_monthly set date = replace(date,'2019','2020');
update fact_sales_monthly set fiscal_year = 2021 where date like '2021%';
select * from fact_sales_monthly;