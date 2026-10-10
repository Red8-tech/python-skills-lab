CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    city TEXT NOT NULL
);


CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL
);


CREATE TABLE orders (
    order_id INTEGER PRIMART KEY,
    customer_id INTEGER NOT NULL,
    order_date TEXT NOT NULL,
    status TEXT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);


CREATE TABLE order_items(
    order_item_id INTEGER PRIMARY KEY,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)   
);




-- =========================
-- CUSTOMERS
-- =========================

INSERT INTO customers (customer_id, name, email, city) VALUES
(1, 'Arjun', 'arjun@example.com', 'Kolkata'),
(2, 'Priya', 'priya@example.com', 'Delhi'),
(3, 'Rahul', 'rahul@example.com', 'Mumbai'),
(4, 'Sneha', 'sneha@example.com', 'Bangalore'),
(5, 'Amit', 'amit@example.com', 'Kolkata');


-- =========================
-- PRODUCTS
-- =========================

INSERT INTO products (product_id, product_name, category, price) VALUES
(1, 'Laptop', 'Electronics', 65000),
(2, 'Mouse', 'Electronics', 1200),
(3, 'Keyboard', 'Electronics', 2500),
(4, 'Headphones', 'Electronics', 4500),
(5, 'Backpack', 'Accessories', 1800),
(6, 'Monitor', 'Electronics', 15000);


-- =========================
-- ORDERS
-- =========================

INSERT INTO orders (order_id, customer_id, order_date, status) VALUES
(101, 1, '2026-09-01', 'Completed'),
(102, 2, '2026-09-02', 'Completed'),
(103, 1, '2026-09-05', 'Pending'),
(104, 3, '2026-09-07', 'Completed'),
(105, 4, '2026-09-10', 'Cancelled'),
(106, 5, '2026-09-12', 'Completed'),
(107, 2, '2026-09-15', 'Completed'),
(108, 3, '2026-09-18', 'Pending');


-- =========================
-- ORDER ITEMS
-- =========================

INSERT INTO order_items
(order_item_id, order_id, product_id, quantity) VALUES
(1, 101, 1, 1),
(2, 101, 2, 2),
(3, 102, 3, 1),
(4, 102, 4, 1),
(5, 103, 5, 1),
(6, 103, 2, 1),
(7, 104, 1, 1),
(8, 104, 6, 1),
(9, 105, 4, 2),
(10, 106, 5, 2),
(11, 106, 3, 1),
(12, 107, 6, 1),
(13, 107, 2, 1),
(14, 108, 4, 1),
(15, 108, 5, 1);
