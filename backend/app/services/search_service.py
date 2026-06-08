from pyexpat import features
from app.services.ai_service import (
    generate_ai_budget_ranges,
    generate_ai_search_term,
    generate_ai_relevant_features,
    generate_next_ai_message,
    generate_ai_questions,
    generate_ai_search_term_from_questions
)
from app.services.product_service import (
    get_product_budget_ranges,
    get_product_list,
)

def generate_budget_ranges(request):
    google_budgets = get_product_budget_ranges(request.query)
    return generate_ai_budget_ranges(request.query, google_budgets)

def generate_recommendations(request):
    # AI used to turn features and query into a new search term when needed
    if request.features:
        search_term = generate_ai_search_term(request.query, request.features)
    else:
        search_term = request.query
    # Products are returned
    search_products = get_product_list(
        f"{search_term} between £{request.minPrice} and £{request.maxPrice}", 
        request.minPrice, 
        request.maxPrice)

    all_features = []
    for product in search_products:
        all_features.extend(product.get("additionalFeatures", []))

    relevant_features = generate_ai_relevant_features(search_term, all_features)
    lower_relevant_features = { feature.lower() for feature in relevant_features}

    # Move relevant features from additionalFeatures into features
    for product in search_products:
        product_features = product.get("additionalFeatures", [])
        relevant = []
        additional = []

        for feature in product_features:
            feature_lower = feature.lower()
            matched = any(relevant_feature in feature_lower for relevant_feature in lower_relevant_features)
            if matched:
                relevant.append(feature)
            else:
                additional.append(feature)

        product["features"] = list(dict.fromkeys(relevant))
        product["additionalFeatures"] = list(dict.fromkeys(additional))


    return {
        "search_products": search_products,
        "relevant_features": relevant_features
    }

def generate_next_message(request):
    return generate_next_ai_message(request.query, request.message, request.history)

def generate_questions(request):
    return generate_ai_questions(request.query)

def generate_search_term_from_questions(request):
    result = generate_ai_search_term_from_questions(request.query, request.questionsAndAnswers)
    return { "query": result }