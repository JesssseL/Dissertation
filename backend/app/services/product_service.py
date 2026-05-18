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
    return price_ranges 

def format_product(item: dict, min_price: float, max_price: float):
    price = item.get("extracted_price")
    if price is None:
        return None
    if price < min_price or price > max_price:
        return None

    title = item.get("title")
    if title is None:
        return None

    brand = item.get("source", "Online retailer")
    if "Amazon" in brand:
        brand = "Amazon"

    # Simple product quality score
    rating = item.get("rating", 0)
    reviews = item.get("reviews", 0)
    additional_features = item.get("extensions", [])
    score = (
        rating * 10 +
        min(reviews, 200) +
        len(additional_features)
    )

    return {
        "name": title,
        "brand": brand,
        "rating": rating,
        "image": item.get("thumbnail", ""),
        "features": [
            feature for feature in [
                item.get("delivery"),
                item.get("snippet"),
                item.get("snippet_highlighted_words"),
                item.get("tagline")
            ]
            if feature
        ],
        "additionalFeatures": item.get("extensions", []),
        "webUrl": item.get("product_link", ""),
        "price": price,
        "PRODUCT_PAGE_TOKEN": item.get("immersive_product_page_token", ""),
        "RANKING_SCORE": score
    }

def extract_immersive_features(page_token: str):
    if not page_token:
        return []
    results = serpapi_client.search({
        "engine": "google_immersive_product",
        "page_token": page_token
    })

    feature_data = (
        results
            .get("product_results", {})
            .get("about_the_product", {})
            .get("features", [])
    )

    extracted_features = []

    for feature in feature_data:
        title = feature.get("title")
        value = feature.get("value")
        
        if value.lower() in ["no", "false", "none"]:
            continue
        if value.lower() in ["yes", "true"]:
            extracted_features.append(title)
            continue
        if value.replace(".", "", 1).isdigit():
            extracted_features.append(f"{title}: {value}")
            continue
        if "," in value:
            values = [part.strip() for part in value.split(",") if part.strip()]
            extracted_features.extend(values)
            continue
        extracted_features.append(value)

    return extracted_features

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

    filtered_products = []
    for item in shopping_results:
        product = format_product(item, min_price, max_price)
        if product:
            filtered_products.append(product)

    filtered_products.sort(
        key=lambda product: product["RANKING_SCORE"],
        reverse=True
    )
    top_products = filtered_products[:3]
    # Top 3 Products get further information

    for item in top_products:
        immersive_features = extract_immersive_features(item["PRODUCT_PAGE_TOKEN"])
        item["additionalFeatures"].extend(immersive_features)

    return top_products