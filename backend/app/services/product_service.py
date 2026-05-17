from app.config import settings
import random
import serpapi

serpapi_client = serpapi.Client(
    api_key=settings.serpapi_api_key
)

def fallback_ranges(query: str, min_price: float, max_price: float):
    return [
        {
            "name": f"Everyday {query} XV",
            "image": "https://picsum.photos/200/300?random=1",
            "features": ["Eco-Friendly Packaging", "Portable", "Weather-Resistant"],
            "additionalFeatures": ["Extended Warranty", "Lifetime Support", "Free Shipping"],
            "webUrl": "https://www.amazon.com/",
            "price": round(random.uniform(minPrice, maxPrice), 2)
        },
        {
            "name": f"{query} Afterglow",
            "image": "https://picsum.photos/200/300?random=1",
            "features": ["Eco-Friendly Packaging", "Portable", "Weather-Resistant"],
            "additionalFeatures": ["Instant-Setup", "BPA-Free", "Scratch-Resistant"],
            "webUrl": "https://www.amazon.com/",
            "price": round(random.uniform(minPrice, maxPrice), 2)
        },
        {
            "name": f"Artisan's Choice {query}",
            "image": "https://picsum.photos/200/300?random=1",
            "features": ["Eco-Friendly Packaging", "Portable", "Weather-Resistant"],
            "additionalFeatures": ["Reinforced Stitching", "Fair-trade", "Hand-painted"],
            "webUrl": "https://www.amazon.com/",
            "price": round(random.uniform(minPrice, maxPrice), 2)
        },
    ]

def extract_filter_by_type(input_type: str, filters: list[dict]):
    options = []

    for filter_option in filters:
        if filter_option.get("input_type") == input_type:
            options.extend([
                option["text"]
                for option in filter_option.get("options", [])
            ])

    return options

def get_product_feature_list(query: str):
    results = serpapi_client.search({
      "engine": "google_shopping_light",
      "google_domain": "google.co.uk",
      "q": query,
      "hl": "en",
      "gl": "uk",
      "location": "United Kingdom"
    })
    filters = results.get("filters", [])

    return extract_filter_by_type("checkbox", filters)

def get_product_budget_ranges(query: str):
    results = serpapi_client.search({
      "engine": "google_shopping_light",
      "google_domain": "google.co.uk",
      "q": query,
      "hl": "en",
      "gl": "uk",
      "location": "United Kingdom"
    })
    filters = results.get("filters", [])
    price_ranges = extract_filter_by_type("price_range", filters)
    print("Prices:", price_ranges)
    return price_ranges 

def get_product_list(query: str, min_price: float, max_price: float):
    results = serpapi_client.search({
      "engine": "google_shopping_light",
      "google_domain": "google.co.uk",
      "q": query,
      "hl": "en",
      "gl": "uk",
      "location": "United Kingdom"
    })
    shopping_results = results.get("shopping_results", [])
    print("shopping_results:", shopping_results)
    filtered_products = []
    for item in shopping_results:
        price = item.get("extracted_price")
        if price is None:
            continue
        if price < min_price or price > max_price:
            continue

        title = item.get("title")
        if title is None:
            continue

        filtered_products.append({
            "name": title,
            "brand": item.get("source", "Online retailer"),
            "rating": item.get('rating', 0),
            "image": item.get("thumbnail", ""),
            "features": [
                item.get("delivery", "Delivery information unavailable"),
                item.get("snippet", "Snippet unavailable"),
                item.get("snippet_highlighted_words", "snippet_highlighted_words unavailable"),
                item.get("tagline", "tagline unavailable")
            ],
            "additionalFeatures": item.get("extensions", []),
            "webUrl": item.get("product_link", ""),
            "price": price
        })

    return filtered_products