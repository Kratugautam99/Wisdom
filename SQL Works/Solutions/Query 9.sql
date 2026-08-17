SELECT 
    c.channel,
    SUM(s.sold_quantity * g.gross_price) AS gross_price_mln,
    SUM(s.sold_quantity * g.gross_price) * 100 / 3177769991.4 AS percentage
FROM fact_sales_monthly s
JOIN fact_gross_price g ON s.product_code = g.product_code
JOIN dim_customer c     ON s.customer_code = c.customer_code
WHERE s.fiscal_year = 2021
GROUP BY c.channel;
