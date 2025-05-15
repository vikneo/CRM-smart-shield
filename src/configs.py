import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# Settings application
SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = os.getenv("DEBUG", 0)

# Settings database
BASE_DIR = Path(__file__).parent / "db"
BASE_DIR.mkdir(exist_ok=True, parents=True)

DB_BASE_URL = os.getenv("DB_BASE_URL")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
