from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models.requests import (
    BudgetRangesRequest,
    ProductFeaturesRequest,
    RecommendationsRequest,
    ChatbotRequest,
    QuestionRequest,
    AnswerRequest,
    AccountRequest,
    AccountProductRequest
)
from app.models.response import (
    BudgetRange,
    ProductRecommendationResponse,
    EnhancedQuery,
    ChatbotResponse,
    QuestionAndExample,
)

from app.services.search_service import (
    generate_budget_ranges,
    generate_recommendations,
    generate_next_message,
    generate_questions,
    generate_search_term_from_questions
)
from app.services.data_service import (
    add_or_get_account_db,
    add_account_products_to_db,
    get_account_products_from_db
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

@app.post("/api/recommendations", response_model=ProductRecommendationResponse)
def create_recommendations(request: RecommendationsRequest):
    return generate_recommendations(request)

@app.post("/api/chatbot", response_model=ChatbotResponse)
def reply_to_conversation(request: ChatbotRequest):
    return generate_next_message(request)

@app.post("/api/questions", response_model=list[QuestionAndExample])
def get_product_questions(request: QuestionRequest):
    return generate_questions(request)

@app.post("/api/answers", response_model=EnhancedQuery)
def get_query_from_question_answers(request: AnswerRequest):
    return generate_search_term_from_questions(request)

@app.post("/api/account")
def add_new_account(request: AccountRequest):
    return add_or_get_account_db(request.email, request.password)

@app.post("/api/account/save-product")
def add_account_product(request: AccountProductRequest):
    return add_account_products_to_db(request.email, request.password, request.product)

@app.post("/api/account/get-products")
def get_account_products(request: AccountRequest):
    return get_account_products_from_db(request.email, request.password)