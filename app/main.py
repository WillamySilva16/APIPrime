from fastapi import FastAPI
import pymssql

app = FastAPI()

AZURE_SERVER = "pbdb3073.database.windows.net"
AZURE_DATABASE = "PBDB3073"
AZURE_USER = "admrs"
AZURE_PASSWORD = "Gf3$Rn8!Qb12^KsW0tZ"

@app.get("/")
def home():
    return {"status": "API rodando!"}

@app.get("/visitas")
def get_visitas():
    try:
        conn = pymssql.connect(
            server=AZURE_SERVER,
            user=AZURE_USER,
            password=AZURE_PASSWORD,
            database=AZURE_DATABASE
        )

        cursor = conn.cursor(as_dict=True)

        cursor.execute("SELECT * FROM TAB_REGISTRO_VISITA_SUPERVISAO_CABECALHO")
        dados = cursor.fetchall()

        conn.close()

        return dados

    except Exception as e:
        return {"erro": str(e)}
