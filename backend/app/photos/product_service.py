from app.clients.serpapi_client import (
    search_google_shopping,
    search_immersive_product
)

# COPIED FROM MAIN PRODUCT SERVICE
def extract_immersive_features(page_token: str):
    if not page_token:
        return []
    results = search_immersive_product(page_token)

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
            value = title
            continue
        if value.replace(".", "", 1).isdigit():
            extracted_features.append(f"{title}: {value}")
            continue
        if "," in value:
            values = [part.strip() for part in value.split(",") if part.strip()]
            extracted_features.extend(values)
            continue
        if value.lower() in extracted_features:
            continue
        extracted_features.append(value)

    return extracted_features
# COPIED FROM MAIN PRODUCT SERVICE

def extract_product_description(page_token: str):
    if not page_token:
        return ""

    results = search_immersive_product(page_token)

    return (
        results
        .get("product_results", {})
        .get("about_the_product", {})
        .get("description", "")
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

# Extracts any repeated features and the products descriptions
def get_product_features(products):
    product_names = []
    all_features = []
    all_descriptions = []

    for product in products:
        product_names.append(product.name)
        features = extract_immersive_features(product.productPageToken)
        all_features.extend([
            feature.strip().lower()
            for feature in features
        ])
        all_descriptions.append(
            extract_product_description(product.productPageToken)
        )

    repeated_features = []
    for feature in all_features:
        if (
            all_features.count(feature) > 1
            and feature not in repeated_features
        ):
            repeated_features.append(feature)

    return {
        "productNames": product_names,
        "commonFeatures": repeated_features,
        "descriptions": all_descriptions
    }