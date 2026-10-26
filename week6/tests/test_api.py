from unittest.mock import Mock, patch

import requests
from fastapi.testclient import TestClient

from app.api import app

client = TestClient(app)


def test_home_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Week 6 Testing API"}


@patch("app.api.requests.get")
def test_get_post_success(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {
        "userId": 1,
        "id": 1,
        "title": "Test post",
        "body": "This response is mocked.",
    }
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    response = client.get("/posts/1")

    assert response.status_code == 200
    assert response.json()["title"] == "Test post"

    mock_get.assert_called_once_with(
        "https://jsonplaceholder.typicode.com/posts/1",
        timeout=5,
    )


@patch("app.api.requests.get")
def test_get_post_upstream_failure(mock_get):
    mock_get.side_effect = requests.Timeout("Request timed out")

    response = client.get("/posts/1")

    assert response.status_code == 502
    assert response.json() == {
        "detail": "Failed to fetch post from external API"
    }


@patch("app.api.requests.get")
def test_get_post_http_error(mock_get):
    mock_response = Mock()
    mock_response.raise_for_status.side_effect = requests.HTTPError(
        "404 Not Found"
    )
    mock_get.return_value = mock_response

    response = client.get("/posts/999")

    assert response.status_code == 502
    assert response.json()["detail"] == (
        "Failed to fetch post from external API"
    )
