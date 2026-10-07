import csv


# Read the CSV and return the records.
def read_sales_file(sales_file_path: str) -> list[list[str]]:
    with open(sales_file_path, "r") as file:
        reader = csv.reader(file)
        rows = []

        for row in reader:
            rows.append(row)

    return rows
