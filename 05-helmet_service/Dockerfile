# Imagen base de Python
FROM python:3.10-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia el código fuente
COPY . .

# Instala Flask
RUN pip install flask

# Expone el puerto que usas en app.py
EXPOSE 5005

# Comando para ejecutar el microservicio
CMD ["python", "app.py"]
