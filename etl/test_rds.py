from sqlalchemy import create_engine, text

HOST = "jobs-db.c7gswyum803q.eu-north-1.rds.amazonaws.com"
USER = "postgres"
PASSWORD = "Lynalasla2002!"
DB = "postgres"

engine = create_engine(
    f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:5432/{DB}",
    connect_args={"sslmode": "require"}
)

with engine.connect() as conn:
    result = conn.execute(text("SELECT 1"))
    print(result.fetchall())