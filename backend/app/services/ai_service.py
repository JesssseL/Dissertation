import re
import json
from app.clients.huggingface_client import generate_chat_completion

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
        generated_text = generate_chat_completion(prompt)
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
        generated_text = generate_chat_completion(prompt)
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
        generated_text = generate_chat_completion(prompt)
        print(generated_text)
        json_text = re.search(r"\[.*\]", generated_text, re.DOTALL).group(0)
        relevant_features = json.loads(json_text)

        if isinstance(relevant_features, list):
            return list(dict.fromkeys(relevant_features + search_term_features))

    except Exception as error:
        print("HF error:", error)

    return search_term_features