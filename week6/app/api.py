import requests
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Week 6 Testing API")

EXTERNAL_API_URL = "https://jsonplaceholder.typicode.com/posts"


@app.get("/")
def home():
    return {"message": "Week 6 Testing API"}


@app.get("/posts/{post_id}")
def get_post(post_id: int):
    try:
        response = requests.get(
            f"{EXTERNAL_API_URL}/{post_id}",
            timeout=5,
        )
        response.raise_for_status()
        return response.json()

    except requests.RequestException as exc:
        raise HTTPException(
            status_code=502,
            detail="Failed to fetch post from external API",
        ) from exc
