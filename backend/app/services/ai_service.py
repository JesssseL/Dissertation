import re
import json
from app.clients.huggingface_client import (
    generate_chat_reply,
    generate_chat_completion
)

def fallback_ranges():
    return [
        {"label": "Low", "min": 20, "max": 80},
        {"label": "Mid", "min": 80, "max": 200},
        {"label": "High", "min": 200, "max": 400},
    ]

def fallback_relevant_features(query: str, features: list[str]):
    query_words = {
        word.lower()
        for word in query.split()
        if len(word) > 2
    }

    matched_features = []
    for feature in features:
        feature_lower = feature.lower()

        if any(word in feature_lower for word in query_words):
            matched_features.append(feature)

    return matched_features

def fallback_questions():
    return [
        {
            "question": "Will this be used inside or outside?",
            "description": "This helps identify whether durability or weather resistance is important.",
            "example": ["Inside", "Outside"]
        },
        {
            "question": "How often will this item be moved around?",
            "description": "This helps determine whether portability and weight are important.",
            "example": ["Never", "Frequently", "Daily commute"]
        },
        {
            "question": "How will it be stored when not in use?",
            "description": "This helps identify whether compact storage or permanent placement matters.",
            "example": ["Left out", "Closet shelf", "Folded away"]
        },
        {
            "question": "What temperature environment will it face?",
            "description": "This helps identify whether heat, cold or climate resistance is required.",
            "example": ["Extreme heat", "Air conditioned", "Freezing cold"]
        }
    ]

def fallback_tags():
    [
        "Recommended",
        "Recommended",
        "Recommended"
    ]

def validate_budget_ranges(ranges):
    if len(ranges) != 3:
        return False

    expected_labels = ["Low", "Mid", "High"]
    for index, item in enumerate(ranges):
        if item["label"] != expected_labels[index]:
            return False
        if not isinstance(item["min"], int):
            return False
        if not isinstance(item["max"], int):
            return False
        if item["min"] >= item["max"]:
            return False

    return True

def validate_questions(questions):
    if len(questions) != 4:
        return False

    expected_labels = ["question", "description", "example"]
    for index, item in enumerate(questions):
        if not all(key in item for key in expected_labels):
            return False
            
    return True

def generate_ai_budget_ranges(query: str, google_budgets: list[str]):
    formatted_budgets = "\n".join(google_budgets)
    prompt = f"""
        Suggest realistic UK online shopping budget ranges for buying: {query}

        Use these Google Shopping price ranges as the primary source for determining the budget ranges:
        {formatted_budgets}

        Please use this data to return three budget ranges:
        - Add a reasonable minimum floor (usually 0)
        - Add a realisitic upper ceiling (this should extend beyond the highest observed number when an "Over £X" exists)

        Return ONLY valid JSON in this format:
        [
          {{"label": "Low", "min": XX, "max": XX}},
          {{"label": "Mid", "min": XX, "max": XX}},
          {{"label": "High", "min": XX, "max": XX}}
        ]
    """

    try:
        generated_text = generate_chat_reply(prompt)
        json_text = re.search(r"\[.*\]", generated_text, re.DOTALL).group(0)
        json_ranges = json.loads(json_text)

        if validate_budget_ranges(json_ranges):
            return json_ranges

    except Exception as error:
        print("HF error:", error)

    return fallback_ranges()

def generate_ai_search_term(query: str, features: list[str]):
    formatted_features = "\n".join(features)
    prompt = f"""
        Generate an Google Shopping Search Query for buying: {query}

        Desired Features:
        {formatted_features}

        Please use this data to a query that will work well in Google Shopping:
        - Include the most important features naturally
        - Avoid unnecessary filler words
        - Avoid repeating words
        - Keep the search query under 15 words where possible realisitic upper ceiling (this should extend beyond the highest observed number when an "Over £X" exists)

        Return ONLY the final search query in plain text
    """

    try:
        generated_text = generate_chat_reply(prompt)
        return generated_text

    except Exception as error:
        print("HF error:", error)

    return query

def generate_ai_relevant_features(query: str, features: list[str]):
    formatted_features = "\n".join(features)
    prompt = f"""
        Identify the most relevant product features for buying: {query}

        Product Features:
        {formatted_features}

        Select ONLY the features from the provided list that are most relevant to the customer's search intent.
        - ONLY return features that already exist in the provided list
        - Do NOT rename, summarise, combine, or simplify features
        - Do NOT invent new features
        - Prioritise features most useful to the customer query
        - The search query may imply related features even when the exact words are not used
        - Include direct query matches where relevant
        - Keep the response concise

        Return ONLY valid JSON in this format:
        [
          "Feature One",
          "Feature Two",
          "Feature Three"
        ]
    """
    
    search_term_features = fallback_relevant_features(query, features)
    try:
        generated_text = generate_chat_reply(prompt)
        json_text = re.search(r"\[.*\]", generated_text, re.DOTALL).group(0)
        relevant_features = json.loads(json_text)

        if isinstance(relevant_features, list):
            return list(dict.fromkeys(relevant_features + search_term_features))

    except Exception as error:
        print("HF error:", error)

    return search_term_features

def generate_next_ai_message(query: str | None, user_message: str, conversation_history: list[dict]):
    system_message = {
        "role": "system",
        "content": f"""
            The customer is {
                f"asking questions before buying: {query}"
                if query
                else "trying to decide what to search for"
            }

            - Help the user by replying to their question
            {
                f'''
                - If appropriate, suggest a better search term than "{query}"
                - If no search term change is needed, set suggestedSearchTerm to null
                '''
                if query
                else '''
                - Suggest a useful Google Shopping search term to be used
                - suggestedSearchTerm must never be null
                - If the customer is vague, ask one useful narrowing question.
                '''
            }
            - Queries should be concise, built for shopping and derived from the user's intent
            Search term rules:
            - Preserve the user's original intent.
            - Do not add premium, luxury, organic, designer, cheap, professional, best, or branded wording unless the user said it.
            - For broad queries, keep the search term close to the original query.
            - Keep the reply concise and useful.

            Return ONLY valid JSON in this format:
            {{
                "reply": "...",
                "suggestedSearchTerm": {
                    f'''"..." | null'''
                    if query
                    else '''"..."'''
                }
            }}
        """
    }
    newest_message = {
        "role": "user",
        "content": user_message
    }

    try:
        generated_text = generate_chat_completion( 
            [system_message]
            + conversation_history 
            + [newest_message] 
        )
        json_text = re.search(r"\{.*\}", generated_text, re.DOTALL).group(0)
        return json.loads(json_text)

    except Exception as error:
        print("HF error:", error)

    return {
        "reply": "Sorry, I couldn't generate a response.",
        "suggestedSearchTerm": None
    }

def generate_ai_questions(query: str):
    prompt = f"""
        Suggest questions specific for a user buying a: {query}

        - Return exatly 4 questions
        - description: A short sentence explaining what preference, constraint or requirement this question is trying to discover.
        - examples: 2-5 realistic example answers the user may select.
        - examples should be 1-3 words responses to guild the user
        - DO NOT MENTION BUDGET OR PRICE POINTS UNDER ANY CIRCUMSTANCE
        - Try to stay away from questions that require technical answers

        Return ONLY valid JSON in this format:
        [
          {{
            "question": "...",
            "description": "...",
            "example": ["...", "..."]
          }}    
        ]
    """

    try:
        generated_text = generate_chat_reply(prompt)
        json_text = re.search(r"\[.*\]", generated_text, re.DOTALL).group(0)
        json_questions = json.loads(json_text)

        if validate_questions(json_questions):
            return json_questions
    except Exception as error:
        print("HF error:", error)

    return fallback_questions()

def generate_ai_search_term_from_questions(query: str, questionsAndAnswers):
    formatted_questions = "\n".join(
        [
            f"Question: {item.question}\nAnswer: {item.answer}"
            for item in questionsAndAnswers
            if item.answer
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
        generated_text = generate_chat_reply(prompt)
        return generated_text

    except Exception as error:
        print("HF error:", error)

    return query

def generate_ai_search_products_with_tag(query: str, search_products):
    prompt = f"""
        Assign one short recommendation tag to each product for buying {query}:

        Products:
        {search_products}

        - Return exactly one tag per product
        - Tags should be short, 1-3 words
        - Tags should help the user understand why the product may be useful
        - Do not invent product details
        - Safe example tags: Best Match, Good Value, Budget Option, Popular Choice, Alternative Option

        Return ONLY valid JSON in this format:
        [
          "Best Match",
          "Good Value",
          "Alternative Option"
        ]
    """

    try:
        generated_text = generate_chat_reply(prompt)
        json_text = re.search(r"\[.*\]", generated_text, re.DOTALL).group(0)
        json_tags = json.loads(json_text)
        return json_tags

    except Exception as error:
        print("HF error:", error)

    return query

    return fallback_tags()