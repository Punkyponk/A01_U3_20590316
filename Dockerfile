# Usar imagen base de Python
FROM python:3.10-slim

# Instalar las dependencias necesarias para compilar psycopg2
RUN apt-get update && apt-get install -y \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el archivo requirements.txt
COPY requirements.txt /app/

# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de los archivos de la aplicación
COPY . /app/

# Comando por defecto para ejecutar la app
CMD ["python", "app.py"]
