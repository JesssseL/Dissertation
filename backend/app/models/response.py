from pydantic import BaseModel
from typing import Any

class BudgetRange(BaseModel):
    label: str
    min: float
    max: float

class Product(BaseModel):
    name: str
    brand: str
    rating: float
    image: str
    features: list[str]
    additionalFeatures: list[str]
    webUrl: str
    price: float

class ProductRecommendationResponse(BaseModel):
    search_products: list[Product]
    relevant_features: list[str]

class EnhancedQuery(BaseModel):
    query: str

class ChatbotResponse(BaseModel):
    reply: str
    suggestedSearchTerm: str | None = None

class QuestionAndExample(BaseModel):
    question: str
    description: str
    example: list[str]