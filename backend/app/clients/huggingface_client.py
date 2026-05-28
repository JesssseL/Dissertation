from app.config import settings
from huggingface_hub import InferenceClient

hf_client = InferenceClient(
    api_key=settings.huggingface_api_key
)

def generate_chat_completion(prompt: str):
    completion = hf_client.chat.completions.create(
        model="openai/gpt-oss-20b:groq",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
    )
    return completion.choices[0].message.content