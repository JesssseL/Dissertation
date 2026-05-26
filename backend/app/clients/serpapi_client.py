from app.config import settings
import serpapi

client = serpapi.Client(
    api_key=settings.serpapi_api_key
)

# Google shopping light used when possible due to speed
def search_google_shopping(query: str, include_shops: bool = False):
    return client.search({
        "engine": "google_shopping" if include_shops else "google_shopping_light",
        "google_domain": "google.co.uk",
        "q": query,
        "hl": "en",
        "gl": "uk",
        "location": "United Kingdom"
    })

def search_immersive_product(page_token: str):
    return client.search({
        "engine": "google_immersive_product",
        "page_token": page_token
    })