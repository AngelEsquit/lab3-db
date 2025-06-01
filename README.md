# Laboratorio 3
## Integrantes
- Angel Esquit
- Javier Benitez
## Instrucciones para ejecutar
### Ejecutar contenedores
``` bash
docker compose up --build
```
### Detener contenedores
``` bash
docker compose down --volumes --remove-orphans
```
### Ingresar al contenedor de la base de datos
``` bash
docker compose exec db psql -U postgres -d lab3
```
### Ejecutar el programa dentro del contenedor
``` bash
docker compose exec app python -m app.cli
```
