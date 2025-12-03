import pyodbc
from fastapi import FastAPI

app = FastAPI()

def get_connection():
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        "SERVER=pbdb3073.database.windows.net;"
        "DATABASE=PBDB3073;"
        "UID=admrs;"
        "PWD=Gf3$Rn8!Qb12^KsW0tZ;"
        "Encrypt=yes;"
        "TrustServerCertificate=no;"
    )
    return conn

@app.get("/")
def root():
    return {"status": "ok"}
