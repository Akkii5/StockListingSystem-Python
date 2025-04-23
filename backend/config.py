# DATABASE_URI = "postgresql+psycopg2://postgres:123456@localhost:5432/postgres"
import os

DATABASE_URI = os.getenv("DATABASE_URL", "postgresql+psycopg2://postgres:123456@localhost:5432/postgres")
