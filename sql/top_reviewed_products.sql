SELECT
    product_name,
    rating_count
FROM amazon_products
ORDER BY rating_count DESC
LIMIT 10;