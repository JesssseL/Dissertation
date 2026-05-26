import re
import json
from app.clients.huggingface_client import generate_chat_completion

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
        generated_text = generate_chat_completion(prompt)
        return generated_text

    except Exception as error:
        print("HF error:", error)

    return query