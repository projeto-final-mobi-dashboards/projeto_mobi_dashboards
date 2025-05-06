
from sqlalchemy import create_engine
from dotenv import load_dotenv
from os import getenv

load_dotenv(dotenv_path="backend/blueprints/dash/.env")

engine=create_engine(getenv("DATABASE_URL"))