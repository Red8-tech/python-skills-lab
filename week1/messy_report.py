import csv
from datetime import datetime

employees = []
valid_records = []
invalid_records = []
total_sales = 0
total_orders = 0

with open("sales.csv", "r") as f:
    reader = csv.reader(f)

    for row in reader:
        if len(row) != 5:
            invalid_records.append(row)
            continue

        employee_id = row[0]
        employee_name = row[1]
        department = row[2]
        sales = row[3]
        orders = row[4]

        try:
            sales = float(sales)
            orders = int(orders)

            if sales < 0 or orders < 0:
                invalid_records.append(row)
                continue

            valid_records.append(
                {
                    "id": employee_id,
                    "name": employee_name,
                    "department": department,
                    "sales": sales,
                    "orders": orders,
                }
            )

            total_sales += sales
            total_orders += orders

        except ValueError:
            invalid_records.append(row)

for employee in valid_records:
    employee["average_order_value"] = (
        employee["sales"] / employee["orders"]
        if employee["orders"] > 0
        else 0
    )

valid_records.sort(
    key=lambda employee: employee["sales"],
    reverse=True
)

top_employee = valid_records[0] if valid_records else None

department_data = {}

for employee in valid_records:
    department = employee["department"]

    if department not in department_data:
        department_data[department] = {
            "sales": 0,
            "orders": 0,
            "employees": 0,
        }

    department_data[department]["sales"] += employee["sales"]
    department_data[department]["orders"] += employee["orders"]
    department_data[department]["employees"] += 1

for department in department_data:
    department_data[department]["average_sales"] = (
        department_data[department]["sales"]
        / department_data[department]["employees"]
    )

print("=" * 60)
print("EMPLOYEE SALES REPORT")
print("=" * 60)

print("\nTotal valid employees:", len(valid_records))
print("Total invalid records:", len(invalid_records))
print("Total sales:", round(total_sales, 2))
print("Total orders:", total_orders)

if total_orders > 0:
    print(
        "Overall average order value:",
        round(total_sales / total_orders, 2)
    )

if top_employee:
    print("\nTOP PERFORMER")
    print("-" * 30)
    print("Name:", top_employee["name"])
    print("Department:", top_employee["department"])
    print("Sales:", round(top_employee["sales"], 2))
    print("Orders:", top_employee["orders"])

print("\nDEPARTMENT REPORT")
print("-" * 30)

for department, data in department_data.items():
    print(department)
    print("  Employees:", data["employees"])
    print("  Sales:", round(data["sales"], 2))
    print("  Orders:", data["orders"])
    print("  Average sales:", round(data["average_sales"], 2))

print("\nEMPLOYEE DETAILS")
print("-" * 30)

for employee in valid_records:
    print(
        employee["name"],
        "|",
        employee["department"],
        "| Sales:",
        round(employee["sales"], 2),
        "| Orders:",
        employee["orders"],
        "| AOV:",
        round(employee["average_order_value"], 2),
    )

print("\nREPORT GENERATED:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

if invalid_records:
    print("\nINVALID RECORDS")
    print("-" * 30)

    for record in invalid_records:
        print(record)

with open("sales_report.txt", "w") as report:
    report.write("EMPLOYEE SALES REPORT\n")
    report.write("=" * 60 + "\n")
    report.write(f"Total employees: {len(valid_records)}\n")
    report.write(f"Invalid records: {len(invalid_records)}\n")
    report.write(f"Total sales: {round(total_sales, 2)}\n")
    report.write(f"Total orders: {total_orders}\n")

    if top_employee:
        report.write(
            f"Top performer: {top_employee['name']} "
            f"({round(top_employee['sales'], 2)})\n"
        )

    report.write("\nDEPARTMENT REPORT\n")

    for department, data in department_data.items():
        report.write(
            f"{department}: "
            f"{round(data['sales'], 2)} sales, "
            f"{data['employees']} employees\n"
        )
