# Usa una imagen ligera de Node.js
FROM node:18-alpine

# Directorio de trabajo en el contenedor
WORKDIR /usr/src/app

# Copia los archivos de dependencias primero (para aprovechar caché de Docker)
COPY package*.json ./

# Instala las dependencias
RUN npm install --production

# Copia el resto de los archivos
COPY . .

# Expone el puerto del microservicio
EXPOSE 5006

# Comando para iniciar el servicio
CMD ["npm", "start"]