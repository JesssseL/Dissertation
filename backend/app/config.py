from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    huggingface_api_key: str
    serpapi_api_key: str
    db_connection: str
    debug: bool = False

    class Config:
        env_file = ".env"


settings = Settings()