import pandas as pd
from sqlalchemy import create_engine

HOST = "jobs-db.c7gswyum803q.eu-north-1.rds.amazonaws.com"
USER = "postgres"
PASSWORD = "Lynalasla2002!"
DB = "postgres"

engine = create_engine(
    f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:5432/{DB}",
    connect_args={"sslmode": "require"}
)

query = "SELECT * FROM jobs LIMIT 5"

df = pd.read_sql(query, engine)

print(df)