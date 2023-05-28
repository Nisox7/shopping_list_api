from dotenv import load_dotenv
import os

load_dotenv()

database_host = os.getenv("DATABASE_HOST")
database_name = os.getenv("DATABASE_NAME")
database_table = os.getenv("DATABASE_TABLE")
database_user = os.getenv("DATABASE_USER")
database_password = os.getenv("DATABASE_PASSWORD")