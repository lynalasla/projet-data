import pandas as pd
from sqlalchemy import create_engine

HOST = "jobs-db.c7gswyum803q.eu-north-1.rds.amazonaws.com"
USER = "postgres"
PASSWORD = "Lynalasla2002!"
DB = "jobsdb"

engine = create_engine(
    f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:5432/{DB}",
    connect_args={"sslmode": "require"}
)

# lire le csv nettoyé
df = pd.read_csv("data/processed/jobs_clean.csv")

# envoyer vers PostgreSQL
df.to_sql(
    "jobs",
    engine,
    if_exists="replace",
    index=False
)

print("Data loaded into RDS successfully!")