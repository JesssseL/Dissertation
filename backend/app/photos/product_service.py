from app.clients.serpapi_client import search_google_shopping

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
    results = search_google_shopping(query)
    shopping_results = results.get("shopping_results", [])

    formatted_products = []
    for item in shopping_results:
        product = format_product(item)
        if product:
            formatted_products.append(product)

        if len(formatted_products) >= 9:
            break

    return formatted_products