-- 1. Display all customers
SELECT *
FROM customers;

-- 2. Display only customer names and cities
SELECT name, city
FROM customers;

-- 3. Find customers from Kolkata
SELECT * 
FROM customers
WHERE city = 'Kolkata';

-- 4. Find products costing more than 2000
SELECT product_name, price
FROM products
WHERE price > 2000;

-- 5. Find completed orders
SELECT *
FROM orders
WHERE status = 'Completed';

-- 6. Display the names and email addresses of all customers.
SELECT name, email
FROM customers;

-- 7. Find all products priced below 5000.
SELECT product_name, price
FROM products
WHERE price < 5000;

-- 8. Find all orders whose status is Pending.
SELECT *
FROM orders
WHERE status = 'Pending';

-- 9. Find all customers who do not live in Kolkata.
SELECT * 
FROM customers
WHERE city != 'Kolkata';

-- 10. Find products in the Electronics category costing at least 10000.
SELECT product_name, price
FROM products
WHERE category = 'Electronics'
AND price >= 10000;

-- 11. Display all products sorted by price from lowest to highest.
SELECT product_name, price
FROM products
ORDER BY price ASC

-- 12. Display the three most expensive products.
SELECT product_name, price
FROM products
ORDER BY price DESC
LIMIT 3

-- 13. Find all customers from Kolkata or Delhi, sorted alphabetically by name.
SELECT * 
FROM customers
WHERE city = 'Kolkata'
OR city = 'Delhi'
ORDER BY name;

-- 14. Count how many orders have each status.
SELECT COUNT(*)
FROM orders
GROUP BY status;

-- 15. Calculate the average price of products in each category.
SELECT AVG(price)
FROM products
GROUP BY category;

-- 16. Display cities that have more than one customer.
SELECT city, COUNT(*) AS total_customers
FROM customers
GROUP BY city
HAVING COUNT(*) > 1
