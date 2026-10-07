from .models import EmployeeRecord


def display_report(
    invalid_rows: list[list[str]],
    top_employee: EmployeeRecord | None,
    department_statistics: dict[str, dict[str, float | int]] 
) -> None:
    print("Invalid records:", invalid_rows)
    print("Top employee:", top_employee)
    print("Department statistics:", department_statistics)


def write_report(
    filename: str,
    invalid_rows: list[list[str]],
    top_employee: EmployeeRecord | None,
    department_statistics: dict[str, dict[str, float | int]]
) -> None:
    with open(filename, "w") as file:
        file.write(f"Invalid records: {invalid_rows}\n")
        file.write(f"Top employee: {top_employee}\n")
        file.write(f"Department statistics: {department_statistics}\n")
