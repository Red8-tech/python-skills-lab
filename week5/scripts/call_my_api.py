import os

import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "http://127.0.0.1:8000"
TASKS_URL = f"{BASE_URL}/tasks"
API_TOKEN = os.getenv("API_TOKEN")

if not API_TOKEN:
    raise RuntimeError("API_TOKEN is missing from .env")


HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Accept": "application/json",
}


def main():
    # 1. CREATE a task
    print("\n--- CREATE TASK ---")

    task_data = {
        "title": "Learn API Authentication",
        "description": "Use a bearer token with FastAPI",
        "completed": False,
    }

    response = requests.post(
        TASKS_URL,
        json=task_data,
        headers=HEADERS,
        timeout=10,
    )

    response.raise_for_status()

    task = response.json()
    task_id = task["id"]

    print("Created task:", task)
    print("Status code:", response.status_code)


    # 2. READ the created task
    print("\n--- GET TASK ---")

    response = requests.get(
        f"{TASKS_URL}/{task_id}",
        headers=HEADERS,
        timeout=10,
    )

    response.raise_for_status()

    print("Retrieved task:", response.json())
    print("Status code:", response.status_code)


    # 3. READ all tasks
    print("\n--- GET ALL TASKS ---")

    response = requests.get(
        TASKS_URL,
        headers=HEADERS,
        timeout=10,
    )

    response.raise_for_status()

    print("All tasks:", response.json())


    # 4. UPDATE the created task
    print("\n--- UPDATE TASK ---")

    updated_data = {
        "title": "Master Authentication",
        "description": "CRUD operations secured with a bearer token",
        "completed": True,
    }

    response = requests.put(
        f"{TASKS_URL}/{task_id}",
        json=updated_data,
        headers=HEADERS,
        timeout=10,
    )

    response.raise_for_status()

    print("Updated task:", response.json())
    print("Status code:", response.status_code)


    # 5. DELETE the created task
    print("\n--- DELETE TASK ---")

    response = requests.delete(
        f"{TASKS_URL}/{task_id}",
        headers=HEADERS,
        timeout=10,
    )

    response.raise_for_status()

    print("Task deleted successfully.")
    print("Status code:", response.status_code)


    # 6. VERIFY deletion
    print("\n--- VERIFY DELETION ---")

    response = requests.get(
        f"{TASKS_URL}/{task_id}",
        headers=HEADERS,
        timeout=10,
    )

    if response.status_code == 404:
        print("Verified: task no longer exists.")
    else:
        response.raise_for_status()
        print("Task still exists:", response.json())



if __name__ == "__main__":
    main()
