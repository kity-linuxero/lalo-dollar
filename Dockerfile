# Usa la imagen oficial de Python 3.7
FROM python:3.12.2-alpine3.19

WORKDIR /app
COPY requirements.txt .

# Actualiza pip
RUN pip install --upgrade pip
# Instala las dependencias especificadas en requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY lalo-dollar.py .

CMD ["python", "-u", "lalo-dollar.py"]
