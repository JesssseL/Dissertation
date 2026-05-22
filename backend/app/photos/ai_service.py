from app.config import settings
import re
import json
from huggingface_hub import InferenceClient

ai_client = InferenceClient(
    api_key=settings.huggingface_api_key,
)

def generate_ai_feature_based_query(query: str, features: list[str]):
    formatted_features = "\n".join(features)
    prompt = f"""
        A customer has been asked to select images that match their shopping preferances for {query}

        They selected products containing the following features
        {formatted_features}
        
        please generate a new query to better represent the customers product that they want
        - the query should work well in Google Shopping
        - Include the most important features naturally
        - Avoid unnecessary filler words
        - Avoid repeating words
        - Keep the search query under 15 words where possible

        Return ONLY the final search query in plain text
    """

    try:
        completion = ai_client.chat.completions.create(
            model="openai/gpt-oss-20b:groq",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
        )

        generated_text = completion.choices[0].message.content
        return generated_text

    except Exception as error:
        print("HF error:", error)

    return query