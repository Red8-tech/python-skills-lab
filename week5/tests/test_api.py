from urllib import response
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)


def test_home_is_public():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == (
        "Welcome to the Task Management API"
    )


def test_tasks_without_token_are_rejected():
    response = client.get("/tasks")

    assert response.status_code == 401


def test_tasks_with_invalid_token_are_rejected():
    response = client.get(
        "/tasks",
        headers={"Authorization": "Bearer wrong-token"},
    )

    assert response.status_code == 401


def test_tasks_with_valid_token_are_allowed(monkeypatch):
    from api import main

    monkeypatch.setattr(main, "API_TOKEN", "test-token")

    response = client.get(
        "/tasks",
        headers={"Authorization": "Bearer test-token"},
    )

    assert response.status_code == 200


def test_create_task_with_valid_token(monkeypatch):
    from api import main

    monkeypatch.setattr(main, "API_TOKEN", "test-token")

    response = client.post(
        "/tasks",
        headers={"Authorization": "Bearer test-token"},
        json={
            "title": "Learn API testing",
            "description": "Practice FastAPI and pytest",
            "completed": False
        }
    )

    assert response.status_code == 201
    assert response.json()["title"] == "Learn API testing"
    assert response.json()["description"] == "Practice FastAPI and pytest"
    assert "id" in response.json()


def test_get_nonexistent_task_returns_404(monkeypatch):
    from api import main

    monkeypatch.setattr(main, "API_TOKEN", "test-token")

    response = client.get(
        "/tasks/999999",
        headers={"Authorization": "Bearer test-token"}
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"


def test_create_task_with_empty_title_returns_422(monkeypatch):
    from api import main

    monkeypatch.setattr(main, "API_TOKEN", "test-token")

    response = client.post(
        "/tasks",
        headers={"Authorization": "Bearer test-token"},
        json={
            "title": "",
            "description": "This should be rejected",
            "completed": False
        }
    )

    assert response.status_code == 422


def test_delete_nonexistent_task_returns_404(monkeypatch):
    from api import main

    monkeypatch.setattr(main, "API_TOKEN", "test-token")

    response = client.delete(
        "/tasks/999999",
        headers={"Authorization": "Bearer test-token"}
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"
