from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models.requests import (
    BudgetRangesRequest,
    ProductFeaturesRequest,
    RecommendationsRequest,
)
from app.models.response import (
    BudgetRange,
    ProductRecommendation,
)
from app.services.search_service import (
    generate_budget_ranges,
    generate_product_feature_list,
    generate_recommendations,
)

app = FastAPI(
        title="AI Shopping API",
        description="Backend API for the AI-assisted shopping recommendation system.",
        version="0.0.1",
        contact={
            "name": "Jessica Long",
            "email": "s5507056@bournemouth.ac.uk"
        }
    )

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/api/budget-ranges", response_model=list[BudgetRange])
def get_budget_ranges(request: BudgetRangesRequest):
    return generate_budget_ranges(request)

@app.post("/api/features", response_model=list[str])
def get_product_feature_list(request: ProductFeaturesRequest):
    return generate_product_feature_list(request)

@app.post("/api/recommendations", response_model=list[ProductRecommendation])
def create_recommendations(request: RecommendationsRequest):
    return generate_recommendations(request)