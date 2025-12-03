import pyodbc
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

# Função de conexão
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

# ➜ ROTA QUE CONSULTA O BANCO
@app.get("/dados")
def get_dados():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT TOP 50 * FROM TAB_REGISTRO_VISITA_SUPERVISAO_CABECALHO")   # <<< coloque aqui sua tabela real

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]

        cursor.close()
        conn.close()

        return JSONResponse(content=results)

    except Exception as e:
        return {"erro": str(e)}
