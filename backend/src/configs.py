import os


POSRGRES_HOST = os.getenv("POSRGRES_HOST", "localhost")
POSRGRES_PORT = os.getenv("POSRGRES_PORT", "5432")
POSTGRES_USER = os.getenv("POSTGRES_USER", "jan_pawel_2")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "zajebal_mi")
POSTGRES_DB_NAME = os.getenv("POSTGRES_DB", "szlugi")
