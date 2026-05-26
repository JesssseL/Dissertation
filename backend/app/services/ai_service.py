import re
import json
from app.clients.huggingface_client import generate_chat_completion

def fallback_ranges():
    return [
        {"label": "Low", "min": 20, "max": 80},
        {"label": "Mid", "min": 80, "max": 200},
        {"label": "High", "min": 200, "max": 400},
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