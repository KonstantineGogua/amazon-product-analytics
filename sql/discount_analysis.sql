SELECT
    category,
    ROUND(AVG(discount_percentage), 2) AS avg_discount
FROM amazon_products
GROUP BY category
ORDER BY avg_discount DESC
LIMIT 10;