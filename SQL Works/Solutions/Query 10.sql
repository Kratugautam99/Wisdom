WITH ranked_products AS (
    SELECT 
        p.product_code, 
        p.division, 
        p.product, 
        SUM(s.sold_quantity) AS total_sold_quantity,
        ROW_NUMBER() OVER (
            PARTITION BY p.division 
            ORDER BY SUM(s.sold_quantity) DESC
        ) AS rank_order
    FROM dim_product p
    JOIN fact_sales_monthly s ON p.product_code = s.product_code
    WHERE s.fiscal_year = 2021
    GROUP BY p.product_code, p.division, p.product
)
SELECT * FROM ranked_products 
WHERE rank_order <= 3;
