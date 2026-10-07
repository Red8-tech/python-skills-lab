from .models import EmployeeRecord


# Given sales and number of orders, calculate the average order value.
def calculate_avg_order_value(
    sales: float,
    orders: int
) -> float:
    if orders == 0:
        return 0.0

    return sales / orders


# the top employee
def find_top_employee(
    records: list[EmployeeRecord]
) -> EmployeeRecord | None:
    if not records:
        return None

    return max(records, key=lambda employee: employee.sales)


# Extract department statistics
def calculate_department_statistics(
    records: list[EmployeeRecord]
) -> dict:
    department_statistics = {}

    for employee in records:
        department_name = employee.department

        if department_name not in department_statistics:
            department_statistics[department_name] = {
                "sales": 0.0,
                "orders": 0,
                "employees": 0,
            }

        department_statistics[department_name]["sales"] += employee.sales
        department_statistics[department_name]["orders"] += employee.orders
        department_statistics[department_name]["employees"] += 1

    for department_name in department_statistics:
        department_statistics[department_name]["average_sales"] = (
            department_statistics[department_name]["sales"]
            / department_statistics[department_name]["employees"]
        )

    return department_statistics
