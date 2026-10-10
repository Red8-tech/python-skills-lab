-- 1. Find all products whose price is greater than the average price of products in the Electronics category.
SELECT *
FROM products
WHERE price > (
    SELECT AVG(price)
    FROM products
    WHERE category = "Electronics"
)

-- 2. Find customers who have placed at least one order with a status of 'Pending'.
SELECT name
FROM customers
WHERE customer_id IN (
    SELECT COUNT(customer_id)
    FROM orders
    WHERE status = 'Pending'
)

-- 3. Find products that have never been ordered.
SELECT product_id, product_name
FROM products
WHERE product_id NOT IN (
    SELECT product_id
    FROM order_items
)

-- 4. Find customers whose total spending on completed orders is greater than the average total spending of customers who have completed orders.
SELECT c.name, SUM(oi.quantity * p.price) AS total_spending
FROM customers AS c
JOIN orders AS o
ON c.customer_id = o.customer_id
JOIN order_items AS oi
ON o.order_id = oi.order_id
JOIN products AS p
ON oi.product_id = p.product_id
WHERE o.status = 'Completed'
GROUP BY c.customer_id, c.name
HAVING SUM(oi.quantity * p.price) > (
    SELECT AVG(customer_total)
    FROM (
        SELECT o2.customer_id, SUM(oi2.quantity * p2.price) AS customer_total
        FROM orders AS o2
        JOIN order_items AS oi2
        ON o2.order_id = oi2.order_id
        JOIN products AS p2
        ON oi2.product_id = p2.product_id
        WHERE o2.status = 'Completed'
        GROUP BY o2.customer_id
    ) AS customer_totals
);
