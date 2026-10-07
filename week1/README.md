# Week 1 — Clean Functions and Structure

## Overview

This week focused on improving Python code structure by transforming a deliberately messy sales-reporting script into a clean, modular, typed, and maintainable Python application.

The main goal was to practice identifying responsibilities, creating small functions, using meaningful names, adding type hints, validating data, and organizing code into a proper Python package.

---

## Learning Objectives

By completing this week, I practiced:

- Breaking a large script into smaller functions
- Giving functions clear responsibilities
- Designing clear function inputs and outputs
- Validating CSV data
- Handling invalid records safely
- Using Python `dataclass`
- Applying meaningful variable and function names
- Adding type hints throughout the project
- Using `mypy` for static type checking
- Separating code into multiple modules
- Creating and using a Python package
- Using `__init__.py`
- Creating a small entry-point script
- Testing individual modules independently
- Verifying both static correctness and runtime behavior

---

# Project: Sales Report Refactoring

## Original Problem

The initial version was intentionally written as a messy, monolithic Python script.

It was responsible for:

1. Reading a CSV file
2. Parsing employee records
3. Validating data
4. Separating valid and invalid records
5. Calculating average order value
6. Finding the top-performing employee
7. Calculating department statistics
8. Printing the report
9. Writing the report to a text file

Having all of these responsibilities in one script made the code harder to understand, test, reuse, and extend.

---

# Input Data

The project uses `sales.csv` containing employee sales information.

Example:

```csv
101,Alice,Engineering,15000,120
102,Bob,Engineering,12000,100
103,Charlie,Sales,22000,150
104,Diana,Sales,18000,130
105,Ethan,HR,8000,70
106,Fiona,HR,9500,80
107,George,Sales,-5000,20
108,Helen,Engineering,abc,50
109,Ian,Sales,14000,90
110,Jane,Engineering,16000,110
```

Each record contains:

```text
Employee ID
Employee Name
Department
Sales
Orders
```

---

# Validation Rules

A record is considered valid when:

- It contains exactly 5 fields
- Sales can be converted to a `float`
- Orders can be converted to an `int`
- Sales are not negative
- Orders are not negative

Invalid records are preserved separately rather than being discarded.

For example:

```text
107,George,Sales,-5000,20
```

is invalid because sales are negative.

```text
108,Helen,Engineering,abc,50
```

is invalid because `"abc"` cannot be converted to a number.

---

# Refactored Project Structure

The final project is organized as:

```text
week1/
├── sales.csv
├── sales_report.txt
├── refactored/
│   ├── report.py
│   └── report_package/
│       ├── __init__.py
│       ├── models.py
│       ├── reader.py
│       ├── validator.py
│       ├── calculations.py
│       └── reporting.py
└── README.md
```

---

# Module Responsibilities

## `models.py`

Contains the data model used throughout the application.

```python
@dataclass
class EmployeeRecord:
    id: str
    name: str
    department: str
    sales: float
    orders: int
```

Using a dataclass makes employee records easier to create, access, and maintain compared with passing dictionaries throughout the application.

---

## `reader.py`

Responsible only for reading the CSV file.

Main function:

```python
read_sales_file()
```

Its responsibility is:

```text
CSV file
   ↓
Raw rows
```

It does not perform validation or calculations.

---

## `validator.py`

Responsible for validating raw CSV rows and converting valid data into `EmployeeRecord` objects.

Main function:

```python
validate_record()
```

Flow:

```text
Raw CSV row
      ↓
Validation
   ↙      ↘
Valid     Invalid
  ↓          ↓
Employee    None
Record
```

---

## `calculations.py`

Contains business calculations.

The module handles:

### Average Order Value

```text
sales / orders
```

with protection against division by zero.

### Top Sales Employee

Finds the employee with the highest sales amount.

### Department Statistics

Calculates statistics such as:

- Total sales
- Total orders
- Number of employees
- Average sales per employee

---

## `reporting.py`

Responsible for presenting and saving results.

It contains functions for:

- Displaying the report in the console
- Writing the report to `sales_report.txt`

This keeps output-related code separate from business logic.

---

## `report.py`

Acts as the application's entry point.

It coordinates all modules:

```text
             report.py
                 │
       ┌─────────┼─────────┐
       ↓         ↓         ↓
    reader   validator  calculations
       │         │         │
       └─────────┼─────────┘
                 ↓
             reporting
```

The entry point is responsible for orchestration rather than containing all business logic.

---

# Type Hinting

Type hints were added throughout the project.

Example:

```python
def calculate_average_order_value(
    sales: float,
    orders: int
) -> float:
```

Another example:

```python
def find_top_employee(
    employees: list[EmployeeRecord]
) -> EmployeeRecord | None:
```

This makes function contracts easier to understand and allows static analysis tools to identify type-related problems before runtime.

---

# Static Type Checking with mypy

`mypy` was used to verify the project's type correctness.

Command:

```powershell
mypy refactored/
```

Final result:

```text
Success: no issues found in 7 source files
```

This confirmed that all seven Python source files passed static type checking.

---

# Naming Practice

A dedicated naming exercise was performed to improve code readability.

Examples of naming improvements included:

```text
rows
→ raw_rows

row
→ raw_row

record
→ employee_record

valid_records
→ valid_employees

invalid_records
→ invalid_rows

department_data
→ department_statistics

filename
→ sales_file_path

orders
→ order_count

sales
→ sales_amount
```

The important lesson was that good naming should communicate intent.

Names should be:

- Specific
- Readable
- Consistent
- Meaningful
- Not unnecessarily abbreviated

For example:

```python
rows
```

does not tell the reader what the rows contain.

Whereas:

```python
raw_rows
```

immediately communicates that the data came directly from the CSV and has not yet been processed.

---

# Problems Identified in the Original Script

The original implementation had several structural problems:

1. Everything was contained in one script.
2. Functions were difficult to reuse.
3. Individual calculations were difficult to test.
4. Error handling was mixed with business logic.
5. A small change could affect unrelated functionality.
6. Adding new report formats would be difficult.
7. Dictionaries were used extensively for employee data.
8. Shared state could easily be modified unexpectedly.
9. Several behaviors were hard-coded.
10. Calculations could not easily be tested independently.

The refactoring addressed these problems by separating responsibilities.

---

# Key Python Concepts Practiced

## 1. Functions

Functions were created around individual responsibilities.

Instead of:

```text
One large script
```

the application became:

```text
Many small focused functions
```

---

## 2. Dataclasses

Instead of passing employee dictionaries everywhere:

```python
employee["sales"]
```

the project uses:

```python
employee.sales
```

This makes the structure of employee data explicit.

---

## 3. Type Hints

Functions now clearly describe their expected inputs and outputs.

This improves:

- Readability
- IDE support
- Static analysis
- Maintainability

---

## 4. Exception Handling

Invalid numeric values are handled using `try/except`:

```python
try:
    sales = float(sales_text)
    orders = int(orders_text)
except ValueError:
    return None
```

This prevents invalid CSV data from crashing the entire program.

---

## 5. Package Structure

The project uses:

```text
report_package/
└── __init__.py
```

and modules such as:

```text
models.py
reader.py
validator.py
calculations.py
reporting.py
```

This is closer to how larger Python applications are structured.

---

# Testing and Verification

Each major module was tested independently before integrating everything.

Examples:

### Model Test

```powershell
python -c "from refactored.report_package.models import EmployeeRecord; print(EmployeeRecord('1', 'Test', 'IT', 1000.0, 10))"
```

### Reader Test

```powershell
python -c "from refactored.report_package.reader import read_sales_file; print(read_sales_file('sales.csv'))"
```

### Validator Test

```powershell
python -c "from refactored.report_package.validator import validate_record; print(validate_record(['103', 'Charlie', 'Sales', '22000', '150']))"
```

Invalid record:

```powershell
python -c "from refactored.report_package.validator import validate_record; print(validate_record(['107', 'George', 'Sales', '-5000', '20']))"
```

### Type Checking

```powershell
mypy refactored/
```

### Full Application

```powershell
python refactored/report.py
```

---

# Final Output

The completed application correctly identifies:

```text
Invalid records:
107 - George
108 - Helen
```

Top-performing employee:

```text
Charlie
Sales: 22000.0
Orders: 150
```

Department statistics are also calculated for:

```text
Engineering
Sales
HR
```

The application also generates:

```text
sales_report.txt
```

---

# Before vs After

## Before

```text
messy_report.py
       │
       ├── Read CSV
       ├── Validate
       ├── Calculate
       ├── Find employee
       ├── Department statistics
       ├── Print
       └── Write file
```

Everything was tightly coupled.

## After

```text
                    report.py
                       │
       ┌───────────────┼────────────────┐
       ↓               ↓                ↓
    reader         validator       calculations
       │               │                │
       ↓               ↓                ↓
     CSV          EmployeeRecord     Statistics
                       │
                       ↓
                  reporting.py
                       │
                 ┌─────┴─────┐
                 ↓           ↓
              Console      File
```

The application is now easier to understand, test, modify, and extend.

---

# Week 1 Checklist

- [x] Create deliberately messy script
- [x] Identify individual responsibilities
- [x] Refactor into small functions
- [x] Define clear function inputs and outputs
- [x] Add error handling
- [x] Introduce a dataclass
- [x] Add type hints
- [x] Install and use `mypy`
- [x] Fix all mypy errors
- [x] Practice 20 meaningful naming improvements
- [x] Split the application into modules
- [x] Create a Python package
- [x] Add `__init__.py`
- [x] Test individual modules
- [x] Integrate all modules
- [x] Verify the complete application
- [ ] Repeat the refactoring exercise under one hour

---

# Key Takeaways

The biggest lesson from Week 1 was:

> **Working code is not necessarily good code.**

A script can produce the correct output while still being difficult to maintain.

Good Python structure means:

```text
Small functions
      +
Clear names
      +
Clear responsibilities
      +
Type hints
      +
Validation
      +
Independent modules
      +
Simple entry point
      =
Maintainable code
```

The goal is not to make code unnecessarily complicated. The goal is to make each part of the program easy to understand, test, change, and reuse.

---

# Next Challenge

The final Week 1 challenge is to repeat the same process under a time limit.

### Target

Take another messy Python script and transform it into:

```text
Small functions
      ↓
Typed functions
      ↓
Meaningful names
      ↓
Separate modules
      ↓
Python package
      ↓
mypy passes
```

### Time target

**Complete the refactoring in under 1 hour.**

This will test whether the concepts learned during Week 1 have become practical coding skills rather than just a one-time exercise.
