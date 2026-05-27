from pyexpat import features
from app.services.ai_service import (
    generate_ai_budget_ranges,
    generate_ai_search_term
)
from app.services.product_service import (
    get_product_feature_list,
    get_product_budget_ranges,
    get_product_list,
)

def generate_product_feature_list(request):
    # SerpAPI request with query is cached, no extra tokens are used seperating these two
    results = get_product_feature_list(request.query)
    return results

def generate_budget_ranges(request):
    # SerpAPI request with query is cached, no extra tokens are used seperating these two
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
    return search_products