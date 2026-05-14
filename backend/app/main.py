from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random

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

class BudgetRangesRequest(BaseModel):
    query: str

class RecommendationsRequest(BaseModel):
    query: str
    minPrice: float
    maxPrice: float

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/api/budget-ranges")
def get_budget_ranges(request: BudgetRangesRequest):
    return [
        {
            "label": "Low",
            "min": 20,
            "max": 80
        },
        {
            "label": "Mid",
            "min": 80,
            "max": 200
        },
        {
            "label": "High",
            "min": 200,
            "max": 400
        }
    ]

@app.post("/api/recommendations")
def create_recommendations(request: RecommendationsRequest):
    return [
        {
            "name": f"Everyday {request.query} XV",
            "image": "https://picsum.photos/200/300?random=1",
            "features": ["Eco-Friendly Packaging", "Portable", "Weather-Resistant"],
            "additionalFeatures": ["Extended Warranty", "Lifetime Support", "Free Shipping"],
            "webUrl": "https://www.amazon.com/",
            "price": round(random.uniform(request.minPrice, request.maxPrice), 2)
        },
        {
            "name": f"{request.query} Afterglow",
            "image": "https://picsum.photos/200/300?random=1",
            "features": ["Eco-Friendly Packaging", "Portable", "Weather-Resistant"],
            "additionalFeatures": ["Instant-Setup", "BPA-Free", "Scratch-Resistant"],
            "webUrl": "https://www.amazon.com/",
            "price": round(random.uniform(request.minPrice, request.maxPrice), 2)
        },
        {
            "name": f"Artisan's Choice {request.query}",
            "image": "https://picsum.photos/200/300?random=1",
            "features": ["Eco-Friendly Packaging", "Portable", "Weather-Resistant"],
            "additionalFeatures": ["Reinforced Stitching", "Fair-trade", "Hand-painted"],
            "webUrl": "https://www.amazon.com/",
            "price": round(random.uniform(request.minPrice, request.maxPrice), 2)
        },
    ]