from sqlite3 import Cursor
import sqlite3
from pathlib import Path


# Get the week3 folder, regardless of the terminal's working directory
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "ecommerce.db"
SQL_PATH = BASE_DIR / "database" / "setup.sql"


connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

# Enable foreign key enforcement
cursor.execute("PRAGMA foreign_keys = ON;")

# Initialize tables only if this is a new database
cursor.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type = 'table' AND name = 'customers';
""")

if cursor.fetchone() is None:
    with open(SQL_PATH, "r", encoding="utf-8") as file:
        sql_script = file.read()

    cursor.executescript(sql_script)
    print("Database setup completed.")
else:
    print("Database already exists. Skipping setup.")


# Display tables
cursor.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type = 'table'
    ORDER BY name;
""")

print("\nTables:")
for table in cursor.fetchall():
    print(table[0])


# Verify row counts
print("\nRow counts:")
for table_name in ("customers", "products", "orders", "order_items"):
    cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
    print(f"{table_name}: {cursor.fetchone()[0]}")


# Find customers from Kolkata
print("\nCustomers from Kolkata:")
cursor.execute("""
    SELECT name, city
    FROM customers
    WHERE city = 'Kolkata';
""")

results = cursor.fetchall()

for row in results:
    print(row)


connection.close()
