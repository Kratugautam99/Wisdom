drop table temp;
select distinct dim_customer.customer_code,customer,
avg(pre_invoice_discount_pct) as avg_discount 
from fact_pre_invoice_deductions join dim_customer 
on dim_customer.customer_code = fact_pre_invoice_deductions.customer_code 
where market like '%India%' group by customer_code,customer;
