import os
from dotenv import load_dotenv
load_dotenv()


PROJECT_STATUS = os.getenv("PROJECT_STATUS")

if PROJECT_STATUS == "production":
    BOT_TOKEN = os.getenv("PRODUCTION_BOT_TOKEN")
    DATABASE_URL = os.getenv("DATABASE_URL")
else:
    BOT_TOKEN = os.getenv("TEST_BOT_TOKEN")
    DATABASE_URL = os.getenv("SQLITE_URL")
