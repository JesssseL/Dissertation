from pydantic import BaseModel

# Request
class QuestionRequest(BaseModel):
    query: str

class AnsweredQuestion(BaseModel):
    question: str
    answer: str

class AnswerRequest(BaseModel):
    query: str
    questionsAndAnswers: list[AnsweredQuestion]

# Response
class QuestionAndExample(BaseModel):
    question: str
    example: str