-- 1. Rank products by price
SELECT product_name, price, ROW_NUMBER() OVER (
    ORDER BY price DESC
) AS price_position
FROM products;

-- 2. Modify this query to number products from cheapest to most expensive.
SELECT product_name, price, ROW_NUMBER() OVER (
    ORDER BY price ASC
) AS price_position
FROM products;

-- 3. Imagine two products have the same price. ROW_NUMBER() still assigns them different positions, but RANK() gives tied products the same rank.
SELECT product_name, category, price, RANK() OVER (
    PARTITION BY category
    ORDER BY price DESC
) AS category_rank
FROM products;

-- 4. let's calculate cumulative product prices from cheapest to most expensive
SELECT product_name, price, SUM(price) OVER (
    ORDER BY price ASC
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
) AS running_total
FROM products;
