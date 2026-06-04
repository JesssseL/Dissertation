from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models.requests import (
    BudgetRangesRequest,
    ProductFeaturesRequest,
    RecommendationsRequest,
    ChatbotRequest,
)
from app.models.response import (
    BudgetRange,
    ProductRecommendation,
    EnhancedQuery,
    ChatbotResponse,
)
from app.services.search_service import (
    generate_budget_ranges,
    generate_product_feature_list,
    generate_recommendations,
    generate_next_message
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

#@app.post("/api/recommendations", response_model=list[ProductRecommendation])
@app.post("/api/recommendations")
def create_recommendations(request: RecommendationsRequest):
    return generate_recommendations(request)

@app.post("/api/chatbot", response_model=ChatbotResponse)
def reply_to_conversation(request: ChatbotRequest):
    return generate_next_message(request)

# ------------------------------------------
# Intent Specific - Questions
# ------------------------------------------
from app.question.ai_service import (
    generate_ai_questions,
    generate_ai_search_term_from_questions
)
from app.question.models import (
    QuestionRequest,
    AnswerRequest,
    QuestionAndExample
    )
@app.post("/api/questions", response_model=list[QuestionAndExample])
def get_product_questions(request: QuestionRequest):
    return generate_ai_questions(request)

@app.post("/api/answers", response_model=EnhancedQuery)
def get_query_from_question_answers(request: AnswerRequest):
    result = generate_ai_search_term_from_questions(request.query, request.questionsAndAnswers)
    return { "query": result }

# ------------------------------------------
# Intent Specific - Features
# ------------------------------------------
@app.post("/api/features", response_model=list[str])
def get_product_feature_list(request: ProductFeaturesRequest):
    return generate_product_feature_list(request)

# ------------------------------------------
# Intent Specific - Photos
# ------------------------------------------
from app.photos.product_service import (
    get_product_photos,
    get_product_features
)
from app.photos.ai_service import (
    generate_ai_feature_based_query
)
from app.photos.models import (
    ImageRequest,
    SelectedProductsRequest,
    ProductWithImage
)

@app.post("/api/photos", response_model=list[ProductWithImage])
def get_product_images(request: ImageRequest):
    return get_product_photos(request.query)

@app.post("/api/photo-features", response_model=EnhancedQuery)
def get_query_from_selected_photos(request: SelectedProductsRequest):
    photo_features = get_product_features(request.products)
    result = generate_ai_feature_based_query(
        request.query,
        photo_features.get("productNames", []),
        photo_features.get("features", []),
        photo_features.get("descriptions", [])
    )
    return { "query": result }
