create table product2020 as (select product_code, gross_price as price2020 from fact_gross_price where fiscal_year=2020);
create table product2021 as (select product_code, gross_price as price2021 from fact_gross_price where fiscal_year=2021);
alter table product2020 modify column price2020 decimal(10,5) signed;
alter table product2021 modify column price2021 decimal(10,5) signed;
select product2020.product_code,price2021 
as unique_product_2021,price2020 
as unique_product_2020,(abs(price2021-price2020)*100/price2020) 
as percentage_chg from product2020 
join product2021 on product2020.product_code = product2021.product_code;


