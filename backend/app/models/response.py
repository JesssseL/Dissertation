from pydantic import BaseModel


class BudgetRange(BaseModel):
    label: str
    min: float
    max: float

class ProductRecommendation(BaseModel):
    name: str
    brand: str
    rating: float
    image: str
    features: list[str]
    additionalFeatures: list[str]
    webUrl: str
    price: float

class EnhancedQuery(BaseModel):
    query: str

class ChatbotResponse(BaseModel):
    reply: str
    suggestedSearchTerm: str | None = None