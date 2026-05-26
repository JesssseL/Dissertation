from app.clients.huggingface_client import generate_chat_completion
import re
import json

def fallback_questions():
    return [
        {
            "question": "Will this be used inside or outside", 
            "example": "Inside, Outside"
        },
        {
            "question": "How often will this item be moved around?",
            "example": "Never / Frequently / Daily commute"
        },        
        {
            "question": "How will it be stored when not in use?",
            "example": "Left out / Closet shelf / Folded away"
        },
        {
            "question": "What temperature environment will it face?",
            "example": "Extreme heat / Air conditioned / Freezing cold"
        }
    ]

def validate_questions(questions):
    if len(questions) != 4:
        return False

    expected_labels = ["question", "example"]
    for index, item in enumerate(questions):
        if not all(key in item for key in expected_labels):
            return False
            
    return True

def generate_ai_questions(query: str):
    prompt = f"""
        Suggest questions specific for a user buying a: {query}

        - Return exatly 4 questions
        - Examples should be 1-3 words responses to guild the user
        - DO NOT MENTION BUDGET OR PRICE POINTS UNDER ANY CIRCUMSTANCE

        Return ONLY valid JSON in this format:
        [
          {{"question": "Will this be used inside or outside", 
            "example": "Inside, Outside"}},
          {{""question": "How often will this item be moved around?",
            "example": "Never / Frequently / Daily commute"}},
          {{"question": "How will it be stored when not in use?",
            "example": "Left out / Closet shelf / Folded away"}},
          {{"question": "What temperature environment will it face?",
            "example": "Extreme heat / Air conditioned / Freezing cold"}}
        ]
    """

    try:
        generated_text = generate_chat_completion(prompt)
        json_text = re.search(r"\[.*\]", generated_text, re.DOTALL).group(0)
        json_questions = json.loads(json_text)

        if validate_questions(json_questions):
            return json_questions

    except Exception as error:
        print("HF error:", error)

    return fallback_questions()

def generate_ai_search_term_from_questions(query: str, questionsAndAnswers: list[dict]):
    formatted_questions = "\n".join(
        [
            f"Question: {item['question']}\nAnswer: {item['answer']}"
            for item in questionsAndAnswers
            if item.get("answer")
        ]
    )
    prompt = f"""
        We asked a customer the following questions for buying a {query}:

        {formatted_questions}

        Please use this data to create a query that will work well in Google Shopping:
        - Include the most important features naturally
        - Avoid unnecessary filler words
        - Avoid repeating words
        - Keep the search query under 15 words where possible

        Return ONLY the final search query in plain text
    """

    try:
        generated_text = generate_chat_completion(prompt)
        return generated_text

    except Exception as error:
        print("HF error:", error)

    return query
