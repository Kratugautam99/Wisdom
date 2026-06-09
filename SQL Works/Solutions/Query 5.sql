create table temp as (select product_code,manufacturing_cost from fact_manufacturing_cost 
where manufacturing_cost = (select min(manufacturing_cost) from fact_manufacturing_cost) 
or manufacturing_cost = (select max(manufacturing_cost) from fact_manufacturing_cost));
select dim_product.product,temp.product_code,temp.manufacturing_cost from temp 
join dim_product on dim_product.product_code = temp.product_code;
