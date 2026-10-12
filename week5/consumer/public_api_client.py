from requests import post
import time
import requests


API_URL = "https://jsonplaceholder.typicode.com/posts/1"

MAX_RETRIES = 3
RETRY_DELAY = 1

headers = {
    "Accept": "application/json",
    "User-Agent": "python-skills-lab-week5"
}

RETRY_STATUS_CODES = {429, 500, 502, 503, 504}

def fetch_post():
    for attempt in range(MAX_RETRIES + 1):
        try:
            response = requests.get(
                API_URL,
                headers=headers,
                timeout=10
            )

            if response.status_code in RETRY_STATUS_CODES:
                if attempt < MAX_RETRIES:
                    delay = RETRY_DELAY * (2 ** attempt)

                    print(
                        f"Temporary HHP error {response.status_code}."
                        f"Retrying in {delay} seconds..."
                    )

                    time.sleep(delay)
                    continue

                response.raise_for_status()

            response.raise_for_status()

            post = response.json()

            return post

        except requests.exceptions.Timeout:
            error_message = "The API request timed out."

        except requests.exceptions.ConnectionError:
            error_message = "Could not connect to the API."

        except requests.exceptions.HTTPError as error:
            print(f"HTTP error: {error}")
            return None

        except requests.exceptions.RequestException as error:
            print(f"Request failed: {error}")
            return None

        if attempt < MAX_RETRIES:
            delay = RETRY_DELAY * (2 ** attempt)

            print(f"{error_message} Retrying in {delay} seconds...")
        else:
            print(f"{error_message} Maximum retries reached.")
            return None

    return None



def main():
    post = fetch_post()

    if post is None:
        print("Could not retrieve the post.")
        return

    print("Status: Request successful")

    print("\nParsed JSON:")
    print(post)

    print("\nPost details:")
    print("ID:", post["id"])
    print("Title:", post["title"])
    print("Body:", post["body"])



if __name__ == "__main__":
    main()
