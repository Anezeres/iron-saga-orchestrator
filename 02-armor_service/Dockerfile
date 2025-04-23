# Usa una imagen base ligera con Python
FROM python:3.13-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos del proyecto al contenedor
COPY . .

# Instala Flask
RUN pip install flask

# Expón el puerto en el que tu app corre
EXPOSE 5001

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
