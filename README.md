# Proyecto Talana-Kombat-JRPG
Desafío para postular al puesto de desarrollador@ Back End

# Introducción
Desarrollar una solución que relate la pelea entre 2 jugadores y diga el resultado final.

# Instalación
En caso de utilizar **Docker**
La solución se levantó en un SO Windows 10

1. Instalamos Docker Desktop, pueden apoyarse desde la siguiente [Guía](https://docs.docker.com/desktop/windows/install/) oficial que nos provee Docker Docs.
2. Ejecutamos las Siguientes lineas por cmd, reemplazando el nombre de la imagen
```
docker build -t <image_name> .
```
3. Verificamos que creamos la imagen con el siguiente comando:
```
docker images
```
4. Creamos un contenedor desde la imagen que creamos anteriormente
```
docker run -it -p 8000:8000 -v /usr/scr/app <image_name>
```
5. Podemos ver los contenedores que tenemos en ejecución con:
```
docker ps
```
6. Podemos ver los contenedores que tenemos creados:
```
docker ps -a
```
7. Podemos inicializar un Contenedor con el siguiente comando:
```
docker start -a <CONTAINER_ID>
```
En caso de realizar pruebas en **Local**
1. Instalamos las dependencias necesarias para el proyecto, con el siguiente comando:
```
pip install -r requirements.txt
```
2. Luego ejecutamos el siguiente comando para correr la aplicación:
```
uvicorn main:app
```
# Ejemplo
![Esta es una imagen](https://github.com/jestayc/Talana-Kombat-JRPG/blob/main/Captura.PNG?raw=true)

# Nota
Puedes agregar Json con los Movimientos y Golpes de tus jugadores, en el formato de ejemplo del repositorio. Al momento de llamar al combate, solo se ingresa el nombre del archivo con extension .json
