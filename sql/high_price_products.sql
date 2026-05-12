SELECT
    product_name,
    actual_price,
    rating
FROM amazon_products
WHERE actual_price > 50000
ORDER BY rating DESC;