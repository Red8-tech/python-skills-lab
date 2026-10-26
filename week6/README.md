# Week 6 — Testing, Debugging, and Continuous Integration

## Overview

Week 6 focused on improving Python code quality through automated testing, systematic debugging, API testing, and continuous integration.

The goal was to learn how to verify application behavior, identify bugs, handle errors, and automatically run tests whenever code is pushed to GitHub.

This week extended the practical Python skills developed in the previous weeks by introducing a more reliable software development workflow.

---

## Learning Objectives

By completing this week, I practiced:

- Writing unit tests with `pytest`
- Using fixtures to provide reusable test data
- Using parametrized tests to check multiple inputs
- Testing exception handling with `pytest.raises`
- Testing FastAPI endpoints with `TestClient`
- Mocking external API requests with `unittest.mock`
- Testing success and failure scenarios without depending on a live external service
- Debugging Python code with VS Code breakpoints
- Understanding test failures and stack traces
- Creating a GitHub Actions workflow
- Running automated tests through continuous integration

---

# Project Structure

```text
week6/
├── app/
│   ├── __init__.py
│   ├── calculator.py
│   ├── api.py
│   └── discount.py
├── tests/
│   ├── test_calculator.py
│   ├── test_api.py
│   └── test_discount.py
├── .github/
│   └── workflows/
│       └── tests.yml
├── debug_discount.py
├── requirements.txt
├── .gitignore
└── README.md
```

The GitHub Actions workflow must be placed at the repository root under `.github/workflows/` to be detected automatically by GitHub. If the workflow is stored inside the `week6` folder, it should be moved or copied to the repository-level workflow directory.

---

# 1. Unit Testing with pytest

## Calculator Module

File: `app/calculator.py`

The calculator module contains basic arithmetic functions.

### Functions

- `add(a, b)` — returns the sum of two numbers.
- `divide(a, b)` — divides two numbers and raises a `ValueError` when the divisor is zero.

### Testing concepts practiced

**Basic testing**

Verifies that a function returns the expected result for a normal input.

**Parametrization**

Uses `pytest.mark.parametrize` to test several input combinations without duplicating test functions.

Examples include:

- Adding positive numbers
- Adding negative numbers
- Adding zero
- Adding numbers with different signs

**Fixtures**

Uses a pytest fixture to provide reusable test data.

**Exception testing**

Uses `pytest.raises` to verify that division by zero raises the expected exception.

### Result

The calculator module has 11 tests covering arithmetic behavior, multiple inputs, fixtures, and error handling.

---

# 2. API Testing with FastAPI

File: `app/api.py`

The project includes a small FastAPI application that retrieves posts from the JSONPlaceholder external API.

### Endpoints

| Endpoint | Purpose |
|---|---|
| `GET /` | Returns a welcome message |
| `GET /posts/{post_id}` | Fetches a post from the external API |

### Testing with TestClient

FastAPI's `TestClient` allows endpoints to be tested without manually starting the development server.

The tests verify:

- The home endpoint returns the expected response.
- A successful external API request returns post data.
- A timeout from the external service is handled correctly.
- An HTTP error from the external service is handled correctly.

### Mocking external requests

The project uses `unittest.mock.patch` to replace `requests.get` during testing.

This means the tests can simulate external API responses without making actual network requests.

Benefits of mocking include:

- Faster tests
- More predictable results
- No dependence on external API availability
- Easier testing of failure scenarios

The API module converts external request failures into an HTTP `502 Bad Gateway` response.

### Result

The API test module contains four tests covering the home endpoint, successful retrieval, timeout handling, and HTTP errors.

---

# 3. Discount Calculation and Validation

File: `app/discount.py`

This module calculates the final price after applying a percentage discount.

### Function

```python
calculate_discount(price, discount_percent)
```

### Business rules

- The price must not be negative.
- The discount percentage must be between 0 and 100.
- A 0% discount leaves the original price unchanged.
- A 100% discount reduces the final price to zero.
- Invalid inputs raise `ValueError`.

### Formula

```text
Discount amount = Price × Discount percentage / 100

Final price = Price − Discount amount
```

### Example

For an original price of 100 and a discount of 20%:

```text
Original price: 100
Discount: 20%
Final price: 80.0
```

### Testing concepts practiced

The discount tests cover:

- Normal discount calculations
- A full 100% discount
- A zero-percent discount
- Negative prices
- Invalid discount percentages

### Result

The discount module contains five tests.

During debugging practice, the calculation was deliberately changed from subtraction to addition. The tests exposed the bug, the implementation was corrected, and the tests passed again.

This demonstrated how automated tests help catch regressions and incorrect business logic.

---

# 4. Debugging with VS Code

File: `debug_discount.py`

A small script was created to execute the discount calculation independently.

Example output:

```text
Original price: 100
Discount: 20%
Final price: 80.0
```

### Debugging skills practiced

- Setting breakpoints
- Starting the Python debugger
- Stepping through code with F10
- Continuing execution with F5
- Inspecting variables
- Checking intermediate calculation values
- Identifying incorrect logic
- Re-running tests after fixing a bug

The discount calculation was used to understand how an incorrect implementation can produce a result that contradicts the expected business rule.

The debugging exercise reinforced the importance of examining intermediate values instead of relying only on printed output.

---

# 5. Test Results

The complete local test suite was executed using:

```powershell
python -m pytest tests -v
```

The test run used the Week 6 virtual environment.

### Final test summary

| Test module | Tests | Result |
|---|---:|---|
| `test_api.py` | 4 | Passed |
| `test_calculator.py` | 11 | Passed |
| `test_discount.py` | 5 | Passed |
| **Total** | **20** | **All passed** |

Final result:

```text
20 passed, 1 warning
```

The warning concerned the deprecation of using `httpx` with the installed Starlette test client. It did not cause any test failures.

---

# 6. GitHub Actions and Continuous Integration

The project includes a GitHub Actions workflow intended to run the test suite automatically on pushes and pull requests.

Workflow file:

```text
.github/workflows/tests.yml
```

### Workflow responsibilities

1. Check out the repository.
2. Set up Python 3.10.
3. Install the required dependencies.
4. Run the pytest suite.
5. Report whether the workflow succeeded or failed.

### Example workflow

The following configuration assumes the workflow is stored at the repository root:

```yaml
name: Python Tests

on:
  push:
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Check out repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.10"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r week6/requirements.txt

      - name: Run tests
        run: python -m pytest week6/tests -v
```

### Why continuous integration matters

Automated testing on GitHub helps detect problems whenever code changes.

It provides a repeatable way to verify that previously working features continue to work after modifications.

**Note:** The 20 local tests passed. GitHub Actions should only be marked as verified after the workflow has run successfully in the repository.

---

# 7. Dependencies

File: `requirements.txt`

The project requires the following Python packages:

```text
pytest
fastapi
httpx
requests
```

Install them using:

```powershell
python -m pip install -r requirements.txt
```

---

# 8. Setup and Execution

## Step 1: Navigate to Week 6

```powershell
cd C:\Users\arpan\Documents\python-skills-lab\week6
```

## Step 2: Create a virtual environment

```powershell
python -m venv .venv
```

## Step 3: Activate the environment

```powershell
.\.venv\Scripts\Activate.ps1
```

## Step 4: Install dependencies

```powershell
python -m pip install -r requirements.txt
```

## Step 5: Run all tests

```powershell
python -m pytest tests -v
```

## Step 6: Run the debugging example

```powershell
python debug_discount.py
```

## Step 7: Run the FastAPI application

```powershell
python -m uvicorn app.api:app --reload
```

Open the following address in a browser:

```text
http://127.0.0.1:8000
```

Interactive API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

If Uvicorn is not installed in the environment, install it before running the server:

```powershell
python -m pip install uvicorn
```

---

# Key Lessons Learned

## 1. Tests verify expected behavior

A function can run without raising an error and still return an incorrect result. Assertions verify whether the output matches the expected behavior.

## 2. Parametrization reduces duplication

A single parametrized test can verify many input combinations, making test suites easier to maintain.

## 3. Fixtures improve reuse

Fixtures provide reusable setup data and reduce repeated code across tests.

## 4. Exceptions are part of the contract

Invalid input should produce a deliberate and predictable error rather than silently generating incorrect results.

## 5. Mocking makes API tests reliable

External services can be unavailable, slow, or inconsistent. Mocking makes it possible to test both successful responses and failures independently.

## 6. Debugging complements testing

Tests identify unexpected behavior; a debugger helps investigate why it happens.

## 7. CI automates verification

GitHub Actions can run tests consistently after code is pushed, reducing the need to rely only on manual checks.

---

# Week 6 Checklist

- [x] Create calculator functions
- [x] Write unit tests using pytest
- [x] Practice parametrized tests
- [x] Use pytest fixtures
- [x] Test exception handling
- [x] Create a FastAPI testing example
- [x] Test endpoints using TestClient
- [x] Mock external HTTP requests
- [x] Test API success and failure cases
- [x] Implement discount calculation and input validation
- [x] Deliberately introduce and fix a logic bug
- [x] Practice debugging with VS Code
- [x] Run the complete local test suite
- [x] Confirm 20 local tests pass
- [x] Upload Week 6 files to GitHub
- [ ] Confirm GitHub Actions workflow passes successfully

---

# Final Takeaways

Week 6 focused on moving beyond writing code that simply works toward writing code whose behavior can be verified consistently.

The key workflow practiced was:

```text
Write code
    ↓
Create tests
    ↓
Run tests
    ↓
Investigate failures
    ↓
Fix bugs
    ↓
Run tests again
    ↓
Automate verification with CI
```

These practices form an important foundation for developing reliable Python applications and preparing for real-world software development work.

## Next Challenge

Repeat the process with a new Python module, write tests before implementing the logic, introduce an intentional bug, diagnose it with the debugger, and verify that the complete test suite catches the problem.

