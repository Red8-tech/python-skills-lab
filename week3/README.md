# Week 3 — SQL and SQLite

This week focused on learning SQL using SQLite and a sample e-commerce database. I practised writing queries to retrieve, filter, sort, and analyse relational data, along with using Python's built-in `sqlite3` module to interact with the database.

## Topics Covered

### 1. SQL Fundamentals
- Retrieving data using `SELECT`.
- Filtering records using `WHERE` and comparison operators.
- Sorting results using `ORDER BY` and limiting rows using `LIMIT`.
- Using aggregate functions such as `COUNT()`, `AVG()`, and `SUM()`.
- Grouping records using `GROUP BY`.
- Filtering grouped results using `HAVING`.

### 2. Database Joins
- `INNER JOIN` — retrieving matching records from related tables.
- `LEFT JOIN` — retaining all records from the left table.
- `FULL OUTER JOIN` — including matching and unmatched records from both tables.
- `CROSS JOIN` — generating every possible combination of rows.
- Self joins — joining a table to itself.
- Multi-table joins across customers, orders, order items, and products.

### 3. Subqueries
- Using nested queries to solve problems in multiple steps.
- Comparing product prices against an average price.
- Using `IN` to find customers with pending orders.
- Using `NOT IN` and `NOT EXISTS` to identify products that have never been ordered.
- Comparing customer spending with average customer spending.

### 4. Common Table Expressions (CTEs)
- Defining temporary named result sets using `WITH`.
- Calculating customer spending on completed orders.
- Filtering aggregated results using an outer query.
- Using multiple CTEs to organise complex queries.
- Identifying high-value completed orders.

### 5. Window Functions
- `ROW_NUMBER()` — assigning sequential numbers to rows.
- `RANK()` — ranking rows while handling ties.
- `PARTITION BY` — restarting rankings for each category.
- Running totals using `SUM() OVER (...)`.

### 6. Python and SQLite
- Connecting to a SQLite database using Python's `sqlite3` module.
- Using `pathlib` to construct file paths relative to the script.
- Executing a SQL setup script to initialise the database.
- Listing database tables and checking row counts.
- Making the database setup script skip initialisation when the database already exists.

## Database Structure

The project uses a sample e-commerce database with four related tables:

| Table | Description |
|---|---|
| `customers` | Customer information and cities |
| `products` | Product names, categories, and prices |
| `orders` | Order dates, customer IDs, and statuses |
| `order_items` | Products and quantities associated with orders |

### Verified Database Counts

- Customers: 5
- Products: 6
- Orders: 8
- Order items: 15

## Project Structure

```text
week3/
├── database/
│   ├── ecommerce.db
│   └── setup.sql
├── queries/
│   ├── basics.sql
│   └── joins.sql
├── python/
│   └── database_demo.py
└── README.md
```

## Key Learnings

- How relational tables are connected through primary and foreign keys.
- The difference between filtering individual rows with `WHERE` and filtering grouped results with `HAVING`.
- How joins combine data from multiple tables.
- How subqueries and CTEs simplify multi-step SQL problems.
- How window functions calculate rankings and running totals without collapsing rows into groups.
- How Python can connect to and inspect a SQLite database without requiring a separate database server.

## Still to Practise

- Executing SQL queries from Python and loading results into Python data structures.
- Completing additional window-function exercises.
- Solving a business problem involving multiple joined tables without relying on a query template.
- Completing the remaining planned SQL practice questions.
