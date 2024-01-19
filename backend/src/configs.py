import os


POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")
POSTGRES_USER = os.getenv("POSTGRES_USER", "jan_pawel_2")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "zajebal_mi")
POSTGRES_DB_NAME = os.getenv("POSTGRES_DB", "szlugi")
