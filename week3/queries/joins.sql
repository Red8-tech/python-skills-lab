-- 1. Display each order's ID, date, status, and the name of the customer who placed it.
SELECT o.orders_id, o.order_date, o.status, c.name
FROM orders AS o
LEFT JOIN customers AS c
ON o.customer_id = c.customer_id

-- 2. Display each order's ID, customer name, product name, and quantity.
SELECT o.order_id, c.name, p.product_name, oi.quantity
FROM orders AS o
LEFT JOIN customers AS c
ON o.customer_id = c.customer_id
LEFT JOIN order_items AS oi
ON o.order_id = oi.order_id
LEFT JOIN products AS p
ON oi.product_id = p.product_id;

-- 3. Display every customer’s name and their order ID, including customers who have never placed an order.
SELECT c.name, o.order_id
FROM customers AS c
LEFT JOIN orders AS o
ON c.customer_id = o.customer_id

-- 4. Display all products and any order items that reference them, including products that have never been ordered.
SELECT p.product_name, oi.order_id, oi.quantity
FROM products AS p
LEFT JOIN order_items AS oi
on p.product_id = oi.product_id;

-- 5. Display all customers and all orders, including:
-- Customers who have never placed an order.
-- Orders that don't match any customer.
SELECT c.name, o.order_id
FROM customers AS c
FULL OUTER JOIN orders AS o
ON c.customer_id = o.customer_id;

-- 6. Display every possible combination of customers and products. Show each customer's name alongside each product's name.
SELECT c.name, p.product_name
FROM customers AS c
CROSS JOIN products AS p;

-- 7. Write a query that displays:
-- customer1 — the first customer's name
-- customer2 — the second customer's name
-- city — their shared city
SELECT c1.name AS customer1, c2.name AS customer2, c1.city
FROM customers AS c1
JOIN customers AS c2
on c1.city = c2.city
AND c1.customer_id < c2.customer_id;

-- 8. Display each completed order with:
-- Order ID
-- Customer name
-- Product name
-- Quantity
-- Product price
SELECT o.order_id, c.name, p.product_name, oi.quantity, p.price
FROM orders AS o
LEFT JOIN customers AS c
ON o.customer_id = c.customer_id
LEFT JOIN order_items AS oi
ON o.order_id = oi.order_id
LEFT JOIN products AS p
ON oi.product_id = p.product_id
WHERE o.status = 'Completed'

-- 9. Calculate order item totals
SELECT o.order_id, c.name, p.product_name, oi.quantity, p.price, oi.quantity*p.price AS line_total
FROM orders AS o
LEFT JOIN customers AS c
ON o.customer_id = c.customer_id
LEFT JOIN order_items AS oi
ON o.order_id = oi.order_id
LEFT JOIN products AS p
ON oi.product_id = p.product_id
WHERE o.status = 'Completed'

-- 10. Business challenge
SELECT o.order_id, c.name, SUM(oi.quantity * p.price) AS order_total
FROM orders AS o
LEFT JOIN customers AS c
ON o.customer_id = c.customer_id
LEFT JOIN order_items AS oi
ON o.order_id = oi.order_id
LEFT JOIN products AS p
ON oi.product_id = p.product_id
WHERE o.status = 'Completed'
GROUP BY o.order_id, c.name;
