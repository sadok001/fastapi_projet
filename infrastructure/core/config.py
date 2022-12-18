import secrets

from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"

    MONGO_CON_URL: str = "mongodb://admin:admin@mongodb_container:27017/"

    SMTP_API_KEY: str = "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"

    class Config:
        case_sensitive = True


settings = Settings()
