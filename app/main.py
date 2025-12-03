import pyodbc
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from datetime import datetime, date

app = FastAPI()

# Função de conexão
def get_connection():
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=pbdb3073.database.windows.net;"
        "DATABASE=PBDB3073;"
        "UID=admrs;"
        "PWD=Gf3$Rn8!Qb12^KsW0tZ;"
        "Encrypt=yes;"
        "TrustServerCertificate=no;"
    )
    return conn

# Função para converter datetime em string
def serialize_row(columns, row):
    serialized = {}
    for col, value in zip(columns, row):
        if isinstance(value, (datetime, date)):
            serialized[col] = value.isoformat()
        else:
            serialized[col] = value
    return serialized

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/dados")
def get_dados():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT TOP 50 * FROM TAB_REGISTRO_VISITA_SUPERVISAO_CABECALHO")

        columns = [column[0] for column in cursor.description]
        results = [serialize_row(columns, row) for row in cursor.fetchall()]

        cursor.close()
        conn.close()

        return JSONResponse(content=results)

    except Exception as e:
        return {"erro": str(e)}
