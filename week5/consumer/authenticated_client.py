import os
import requests
from dotenv import load_dotenv

load_dotenv()


API_URL = "https://api.example.com/data"
API_TOKEN = os.getenv("API_TOKEN")

if not API_TOKEN:
    raise RuntimeError("API_TOKEN is missing from the environment.")

headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {API_TOKEN}"
}

try:
    response = requests.get(
        API_URL,
        headers=headers,
        timeout=10,
    )

    response.raise_for_status()
    print(response.json())

except requests.exceptions.HTTPError as error:
    print("HTTP error:", error)

except requests.exceptions.RequestException as error:
    print("Request failed:", error)
