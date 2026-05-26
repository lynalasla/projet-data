from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

# Je charge les variables d'environnement depuis le fichier .env
load_dotenv()

HOST = os.getenv("DB_HOST")
USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
DB = os.getenv("DB_NAME")

# Connexion à la base RDS avec SSL obligatoire
engine = create_engine(
    f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:5432/{DB}",
    connect_args={"sslmode": "require"}
)

# Je teste la connexion avec une requête simple avant d'aller plus loin
with engine.connect() as conn:
    result = conn.execute(text("SELECT 1"))
    print(result.fetchall())