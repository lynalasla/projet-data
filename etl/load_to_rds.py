import pandas as pd
from sqlalchemy import create_engine
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

# Je lis le CSV nettoyé depuis le dossier local
df = pd.read_csv("data/processed/jobs_clean.csv")

# J'envoie les données vers PostgreSQL en remplaçant la table si elle existe déjà
df.to_sql(
    "jobs",
    engine,
    if_exists="replace",  # Je recrée la table à chaque fois pour avoir des données fraîches
    index=False           # Je n'exporte pas l'index pandas, inutile en base
)

print("Data loaded into RDS successfully!")