FROM python:3.12-slim

# Instalar dependências ODBC
RUN apt-get update && apt-get install -y curl gnupg unixodbc unixodbc-dev

# Instalar Driver ODBC para SQL Server (Microsoft msodbcsql17)
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/12/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql17

# Instalar dependências Python
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar app
COPY . .

# Expor porta
EXPOSE 8000

# Rodar FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
