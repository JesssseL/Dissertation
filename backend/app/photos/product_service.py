from app.config import settings
import serpapi

serpapi_client = serpapi.Client(
    api_key=settings.serpapi_api_key
)

def format_product(item: dict):
    title = item.get("title")
    thumbnail = item.get("thumbnail")
    page_token = item.get("immersive_product_page_token")
    if not title or not thumbnail or not page_token:
        return None

    return {
        "name": title,
        "image": thumbnail,
        "productPageToken": page_token,
    }

def get_product_photos(query: str):
    print("PHOTO QUERY RECEIVED INSIDE FUNCTION:", query)
    results = serpapi_client.search({
      "engine": "google_shopping_light",
      "google_domain": "google.co.uk",
      "q": query,
      "hl": "en",
      "gl": "uk",
      "location": "United Kingdom"
    })
    shopping_results = results.get("shopping_results", [])

    formatted_products = []
    for item in shopping_results:
        product = format_product(item)
        if product:
            formatted_products.append(product)

        if len(formatted_products) >= 9:
            break

    return formatted_products