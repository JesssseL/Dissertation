from pydantic import BaseModel, Field

class BudgetRangesRequest(BaseModel):
    query: str

class ProductFeaturesRequest(BaseModel):
    query: str

class RecommendationsRequest(BaseModel):
    query: str
    minPrice: float
    maxPrice: float
    features: list[str] = Field(default_factory=list)

class ChatbotRequest(BaseModel):
    message: str
    query: str | None = None
    history: list[dict] = Field(default_factory=list)