-- 1. Calculate the total spending for each customer on completed orders, then display only customers whose spending exceeds ₹10,000.
WITH customer_spending AS (
    -- Calculate each customer's completed-order spending
    SELECT c.customer_id, c.name, SUM(oi.quantity*p.price) total_spending
    FROM customers AS c
    JOIN orders AS o
    ON c.customer_id = o.customer_id
    JOIN order_items AS oi
    ON o.order_id = oi.order_id
    JOIN products AS p
    ON oi.product_id = p.product_id
    WHERE o.status = 'Completed'
    GROUP BY c.customer_id, c.name
)
-- Select customers spending more than 10000
SELECT name, total_spending
FROM customer_spending
WHERE total_spending > 10000
ORDER BY total_spending DESC;


-- 2. Find high-value completed orders
WITH order_totals AS(
    -- Calculates the total value of each completed order.
    SELECT o.order_id, o.customer_id, SUM(oi.quantity * p.price) AS order_total
    FROM orders AS o
    JOIN order_items AS oi
    ON o.order_id = oi.order_id
    JOIN products AS p
    ON oi.product_id = p.product_id
    WHERE o.status = 'Completed'
    GROUP BY o.order_id, o.customer_id
),
customer_details AS (
    -- Provides customer IDs and names.
    SELECT customer_id, name
    FROM customers
)
-- Joins the results and returns orders worth more than ₹5,000
SELECT cd.name, ot.order_id, ot.order_total
ON order_totals AS ot
JOIN customer_details AS cd
ON ot.customer_id = cd.customer_id
WHERE ot.order_total > 5000
ORDER BY ot.order_total DESC;
