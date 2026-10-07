from .models import EmployeeRecord


# extract the validation + parsing responsibility.
def validate_record(row: list[str]) -> EmployeeRecord | None:
    if len(row) != 5:
        return None

    employee_id = row[0]
    employee_name = row[1]
    department = row[2]
    sales_text = row[3]
    orders_text = row[4]

    try:
        sales = float(sales_text)
        orders = int(orders_text)
    except ValueError:
        return None

    if sales < 0 or orders < 0:
        return None

    return EmployeeRecord(
        id=employee_id,
        name=employee_name,
        department=department,
        sales=sales,
        orders=orders
    )
