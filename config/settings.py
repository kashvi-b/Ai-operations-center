from dotenv import load_dotenv
import os

load_dotenv()


class Settings:

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    DATABASE_URL = os.getenv("DATABASE_URL")

    MODEL_NAME = os.getenv("MODEL_NAME")

    LOG_LEVEL = os.getenv("LOG_LEVEL")


settings = Settings()