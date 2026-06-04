from app.clients.huggingface_client import generate_chat_reply

def generate_ai_feature_based_query(query: str, product_names: list[str], common_features: list[str], descriptions: list[str]):
    formatted_products = "\n".join(product_names)
    formatted_features = "\n".join(common_features)
    formatted_descriptions = "\n".join(descriptions)

    prompt = f"""
        A customer searched for: {query}

        They selected these products:
        {formatted_products}

        Common product features:
        {formatted_features}

        Relevant product descriptions:
        {formatted_descriptions}
        
        Generate a new Google Shopping search query that reflects the customer's likely preferences.
        - Generalise from the selected products rather than describing one exact product
        - Prefer broad useful terms over exact specifications
        - Do not include exact sizes, capacities, model names, or minor details unless repeated across products
        - the query should work well in Google Shopping
        - Prioritise repeated/common features
        - Use product names only to infer style and intent
        - Do not include brand names unless clearly important
        - Keep under 15 words
        - Avoid filler words

        Return ONLY the final search query in plain text
    """

    try:
        generated_text = generate_chat_reply(prompt)
        return generated_text

    except Exception as error:
        print("HF error:", error)

    return query