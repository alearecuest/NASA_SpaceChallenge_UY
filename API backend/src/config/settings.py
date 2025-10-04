import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    NASA_API_KEY: str = "XY1jmpyvJigOj9c3C1VkiVWab6mMc3t904wgjWwq"
    NASA_BASE_URL: str = "https://api.nasa.gov/neo/rest/v1"
    
    class Config:
        env_file = ".env"

def get_settings():
    return Settings()
