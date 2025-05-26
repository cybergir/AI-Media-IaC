import os
from pathlib import Path
from pydantic import BaseSettings

class Settings(BaseSettings):
    # Database
    DB_URL: str = "postgresql+asyncpg://user:pass@localhost/db"
    
    # AI Services
    WHISPER_DEVICE: str = "cpu"  # Change to "cuda" later
    TORCH_DEVICE: str = "cpu"
    
    class Config:
        env_file = Path(__file__).parent / ".env"

settings = Settings()