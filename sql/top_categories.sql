SELECT
    category,
    ROUND(AVG(rating), 2) AS avg_rating
FROM amazon_products
GROUP BY category
ORDER BY avg_rating DESC
LIMIT 10;