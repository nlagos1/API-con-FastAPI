# API-con-FastAPI

Mini proyecto de ejemplo que demuestra cómo funcionan los métodos HTTP (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`) utilizando FastApi, un framework para construir APIs con Python.

## Requisitos

- Python 3.8 o superior
- `pip` (gestor de paquetes de Python)

## Instalación

1. Clona este repositorio o copia los archivos en una carpeta:

```bash
git clone https://github.com/nlagos1/API-con-FastAPI
```

2. Instala las dependencias:

```bash
pip install fastapi uvicorn
```

## Ejecución

Corre el servidor con:

```bash
python -m uvicorn main:app --reload
```

La API estará disponible en: [http://127.0.0.1:8000](http://127.0.0.1:8000)

Documentación automática (Swagger UI):  
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Endpoints

| Método | Ruta               | Descripción                          |
|--------|--------------------|--------------------------------------|
| GET    | `/items`           | Listar todos los ítems simulados     |
| POST   | `/items`           | Crear un nuevo ítem                  |
| PUT    | `/items/{id}`      | Reemplazar completamente un ítem     |
| PATCH  | `/items/{id}`      | Actualizar parcialmente un ítem      |
| DELETE | `/items/{id}`      | Eliminar un ítem                     |

## Ejemplos de uso con `curl`

```bash
curl http://127.0.0.1:8000/items
curl -X POST http://127.0.0.1:8000/items -H "Content-Type: application/json" -d '{"name": "Nuevo", "description": "Ejemplo", "price": 9.99}'
curl -X PUT http://127.0.0.1:8000/items/1 -H "Content-Type: application/json" -d '{"name": "Actualizado", "description": "Texto nuevo", "price": 19.99}'
curl -X PATCH http://127.0.0.1:8000/items/2 -H "Content-Type: application/json" -d '{"price": 5.99}'
curl -X DELETE http://127.0.0.1:8000/items/1
```
