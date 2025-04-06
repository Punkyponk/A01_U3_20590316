# Usa una imagen oficial de Python como imagen base
FROM python:3.10-slim

# Establece un directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de requerimientos al contenedor
COPY requirements.txt /app/

# Instala las dependencias necesarias
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el código de tu aplicación al contenedor
COPY . /app/

# Establece la variable de entorno para que Flask corra en modo desarrollo
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

# Expón el puerto que Flask usará para servir la aplicación
EXPOSE 5000

# Comando para ejecutar la aplicación Flask cuando el contenedor se inicie
CMD ["python", "app.py"]
