from app.config import settings
import re
import json
from huggingface_hub import InferenceClient

client = InferenceClient(
    api_key=settings.huggingface_api_key,
)

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

def generate_ai_budget_ranges(query: str):
    prompt = f"""
        Suggest realistic UK online shopping budget ranges for buying: {query}

        Return ONLY valid JSON in this format:
        [
          {{"label": "Low", "min": XX, "max": XX}},
          {{"label": "Mid", "min": XX, "max": XX}},
          {{"label": "High", "min": XX, "max": XX}}
        ]
    """

    try:
        completion = client.chat.completions.create(
            model="google/gemma-2-2b-it:featherless-ai",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
        )

        generated_text = completion.choices[0].message.content
        json_text = re.search(r"\[.*\]", generated_text, re.DOTALL).group(0)
        json_ranges = json.loads(json_text)

        if validate_budget_ranges(json_ranges):
            return json_ranges

    except Exception as error:
        print("HF error:", error)

    return fallback_ranges()