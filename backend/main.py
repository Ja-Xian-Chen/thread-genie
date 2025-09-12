from fastapi import FastAPI
import requests

app = FastAPI()

API_KEY = "a757f9399b2644b2ad8776d04eddb3a5"
BASE_URL = "https://scrape.abstractapi.com/v1/"

@app.get("/")
def read_root():
    return {"Server Connected"}


@app.get("/scrape")
def scrape_site(url: str):
    """
    Scrape a website by passing the URL as a query parameter.
    Example: /scrape?url=https://news.ycombinator.com
    """
    params = {
        "api_key": API_KEY,
        "url": url
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        return {"status": "success", "data": response.text}
    else:
        return {"status": "error", "code": response.status_code, "message": response.text}
