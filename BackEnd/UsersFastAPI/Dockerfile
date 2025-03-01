FROM python:3.13.2-slim

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt


COPY . .

# Expone el puerto en el que correrá FastAPI
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

