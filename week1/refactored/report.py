from report_package.reader import read_sales_file
from report_package.validator import validate_record
from report_package.calculations import (
    calculate_avg_order_value,
    find_top_employee,
    calculate_department_statistics,
)
from report_package.reporting import display_report, write_report


def main() -> None:
    raw_rows = read_sales_file("sales.csv")

    valid_employees = []
    invalid_rows = []

    for raw_row in raw_rows:
        employee_record = validate_record(raw_row)

        if employee_record is None:
            invalid_rows.append(raw_row)
        else:
            valid_employees.append(employee_record)


    top_employee = find_top_employee(valid_employees)

    department_statistics = calculate_department_statistics(valid_employees)

    display_report(
        invalid_rows,
        top_employee,
        department_statistics
    )

    write_report(
        "Sales_report.txt",
        invalid_rows,
        top_employee,
        department_statistics
    )



if __name__ == "__main__":
    main()
