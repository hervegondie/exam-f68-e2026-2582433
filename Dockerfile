# Imagine de bază
FROM python:3.10-slim

# Setăm directorul de lucru
WORKDIR /app

# Copiem toate fișierele în container
COPY . /app

# Instalăm dependențele
RUN pip install --no-cache-dir -r requirements.txt 

# Setăm PYTHONPATH pentru a include directorul de lucru
ENV PYTHONPATH=/app

# Expunem portul 8000
EXPOSE 8000

# Comanda de pornire
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
