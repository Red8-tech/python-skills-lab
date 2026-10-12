# Week 5 — REST API Development and Integration

## Overview

Week 5 focuses on practical API development and integration using Python. The project covers consuming external REST APIs, building a Task Management REST API using FastAPI, implementing bearer-token authentication, handling HTTP errors, and writing automated tests with pytest.

The goal is to understand how Python applications communicate through HTTP, how APIs validate and protect requests, and how to test API functionality reliably.

## Learning Objectives

- Understand REST APIs, HTTP methods, status codes, and JSON responses.
- Consume external APIs using the `requests` library.
- Implement timeout handling, error handling, and retry logic.
- Build REST endpoints using FastAPI.
- Validate request data using Pydantic models.
- Implement bearer-token authentication using environment variables.
- Perform Create, Read, Update, and Delete (CRUD) operations.
- Write automated API tests using pytest and FastAPI's test client.
- Manage dependencies and protect sensitive configuration using `.env` and `.gitignore`.

## Project Structure

```text
week5/
├── api/
│   └── main.py
├── consumer/
│   ├── public_api_client.py
│   └── authenticated_client.py
├── scripts/
│   └── call_my_api.py
├── tests/
│   └── test_api.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

### Directory and File Description

- **`api/main.py`** — Contains the FastAPI application, task data models, authentication dependency, and CRUD endpoints.
- **`consumer/public_api_client.py`** — Demonstrates consuming a public REST API using `requests`, including timeout handling and retries for selected HTTP failures.
- **`consumer/authenticated_client.py`** — Intended as an example of making authenticated requests to an external API. Replace any placeholder URL with a real endpoint before using it.
- **`scripts/call_my_api.py`** — Sends authenticated requests to the Task Management API to demonstrate task creation, retrieval, listing, updating, and deletion.
- **`tests/test_api.py`** — Contains automated tests for public access, authentication, task creation, input validation, and missing-resource errors.
- **`.env`** — Stores local configuration, including the API token. This file must not be committed to Git.
- **`.gitignore`** — Excludes environment files, virtual environments, and generated Python and pytest cache files.
- **`requirements.txt`** — Lists the Python packages required to run the project.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| FastAPI | Building REST API endpoints |
| Pydantic | Request-data validation |
| Requests | Sending HTTP requests to APIs |
| Uvicorn | Running the FastAPI application |
| python-dotenv | Loading environment variables |
| pytest | Automated testing |
| HTTPX | Supporting the FastAPI test client |

## Setup and Installation

### 1. Navigate to the project directory

```powershell
cd C:\Users\arpan\Documents\python-skills-lab\week5
```

### 2. Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

## Environment Configuration

Create a `.env` file in the project root and configure the API token:

```text
API_TOKEN=your_generated_secret_token
```

Generate a secure random token using Python:

```powershell
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

Copy the generated value into the `.env` file.

The application loads the token through environment variables and uses it to authenticate protected task endpoints.

**Security note:** Never commit `.env` to a public repository or share your real API token. The token used in automated tests is a separate test value.

## Running the FastAPI Application

Start the development server from the `week5` directory:

```powershell
python -m uvicorn api.main:app --reload
```

The API will be available at:

- **Base URL:** `http://127.0.0.1:8000`
- **Interactive API documentation:** `http://127.0.0.1:8000/docs`
- **Alternative API documentation:** `http://127.0.0.1:8000/redoc`

The interactive documentation allows you to inspect endpoints, review request schemas, and send test requests.

## API Endpoints

The Task Management API supports the following endpoints:

| HTTP Method | Endpoint | Description | Expected Success Status |
|---|---|---|---|
| GET | `/` | Returns a welcome message | `200 OK` |
| POST | `/tasks` | Creates a new task | `201 Created` |
| GET | `/tasks` | Lists tasks with pagination | `200 OK` |
| GET | `/tasks/{task_id}` | Retrieves a task by ID | `200 OK` |
| PUT | `/tasks/{task_id}` | Replaces an existing task | `200 OK` |
| DELETE | `/tasks/{task_id}` | Deletes a task | `204 No Content` |

The root endpoint is public. The task endpoints require a valid bearer token.

### Task Data Model

A task contains the following fields:

- **`id`** — Unique integer identifier generated by the API.
- **`title`** — Required task title, with a maximum length of 100 characters.
- **`description`** — Optional description represented by an empty string when omitted, with a maximum length of 500 characters.
- **`completed`** — Boolean field indicating whether the task is complete; defaults to `False`.

Pydantic validates incoming request data and rejects invalid input.

## Authentication

The task endpoints use HTTP bearer-token authentication.

For protected requests, the client sends the token in the `Authorization` header:

```http
Authorization: Bearer your_generated_secret_token
```

The authentication dependency compares the supplied token with the configured API token.

Requests with a missing or invalid token are rejected with an HTTP `401 Unauthorized` response. A valid token allows the request to proceed to the endpoint.

This is a learning implementation using a shared token. It does not provide individual user accounts, roles, token expiration, or a complete production authentication system.

## External API Integration

The public API client demonstrates how to send HTTP requests and process JSON responses using `requests`.

The implementation covers:

- Sending requests to an external API.
- Configuring request timeouts.
- Checking HTTP response status codes.
- Parsing JSON responses.
- Handling common request failures.
- Retrying selected transient failures, such as HTTP `429` and `5xx` responses, using exponential backoff.

The public API example uses JSONPlaceholder, a service commonly used for API practice.

The authenticated external API client is an example structure and requires a real API URL and the appropriate authentication configuration before it can be used.

## Testing the API Client

Keep the FastAPI server running in one terminal. Open a second PowerShell terminal, navigate to the `week5` directory, and activate the virtual environment.

Run the client script:

```powershell
python scripts/call_my_api.py
```

The script demonstrates the main CRUD workflow:

1. Create a task.
2. Retrieve the created task.
3. List available tasks.
4. Update the task.
5. Delete the task.
6. Verify that the deleted task can no longer be retrieved.

The script uses the API token loaded from `.env` and checks HTTP responses for errors.

## Automated Testing with pytest

Run the automated tests from the project root:

```powershell
python -m pytest tests -v
```

The current test suite contains **8 passing tests** covering:

1. Public access to the root endpoint.
2. Rejection of requests without a token.
3. Rejection of requests with an invalid token.
4. Successful access with a valid token.
5. Successful task creation.
6. A `404 Not Found` response for a nonexistent task.
7. Rejection of an empty task title with a `422 Unprocessable Entity` response.
8. A `404 Not Found` response when deleting a nonexistent task.

The tests use FastAPI's test client, allowing endpoint behavior to be checked without manually sending every request through a browser.

## Error Handling and HTTP Status Codes

The project demonstrates common HTTP status codes:

- **`200 OK`** — A request completed successfully.
- **`201 Created`** — A new task was created.
- **`204 No Content`** — A task was deleted successfully.
- **`401 Unauthorized`** — Authentication is missing or invalid.
- **`404 Not Found`** — The requested task does not exist.
- **`422 Unprocessable Entity`** — Request data failed validation.

The external API client also demonstrates exception handling and retry behavior for selected request failures.

## Current Limitations

- Task records are stored in memory, so they are lost when the application restarts.
- Authentication relies on a single shared bearer token rather than individual user identities.
- The retry implementation is a learning example and can be improved to handle server-provided retry delays and other production concerns.
- The authenticated external API client requires a real endpoint and may need provider-specific authentication logic.

## Future Improvements

Potential improvements include:

- Integrating SQLite or PostgreSQL for persistent task storage.
- Adding tests for task updates, successful deletion, pagination, and malformed requests.
- Improving logging and exception handling.
- Enhancing retry logic with support for `Retry-After` headers.
- Adding individual user authentication and authorization.
- Pinning dependency versions for reproducible installations.
- Adding API integration tests and automated code-quality checks.

## Key Takeaways

By completing this project, I practiced building and consuming REST APIs, working with HTTP requests and JSON data, validating inputs, protecting endpoints with bearer-token authentication, handling request failures, and writing automated tests.

The project connects core Python programming skills with practical backend development concepts that are useful for entry-level software development and QA automation roles.
