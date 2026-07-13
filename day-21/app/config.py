"""
config.py
---------
Application configuration loaded from environment variables.
"""

from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./employees.db")
SECRET_KEY = os.getenv("SECRET_KEY", "fallback-secret-key")
TOKEN_EXPIRE_MINUTES = int(os.getenv("TOKEN_EXPIRE_MINUTES", "30"))
APP_NAME = os.getenv("APP_NAME", "Employee API")