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

class QuestionRequest(BaseModel):
    query: str

class AnsweredQuestion(BaseModel):
    question: str
    answer: str

class AnswerRequest(BaseModel):
    query: str
    questionsAndAnswers: list[AnsweredQuestion]

class AccountRequest(BaseModel):
    email: str
    password: str

class DBProduct(BaseModel):
    name: str
    brand: str
    rating: float
    image: str
    webUrl: str
    price: float
    tag: str | None = None

class AccountProductRequest(BaseModel):
    email: str
    password: str
    product: DBProduct