from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Modelo de datos
class Item(BaseModel):
    name: str
    description: str = None
    price: float

# Base de datos en memoria caché
fake_db = {
    1: {"name": "Monster Ultra", "description": "Bebida energetica sin azucar", "price": 2000},
    2: {"name": "Red Bull Light", "description": "Bebida energetica sin azucar pero premium", "price": 2300}
}

# GET
@app.get("/items")
def get_items():
    return fake_db

# POST
@app.post("/items")
def create_item(item: Item):
    new_id = max(fake_db.keys()) + 1
    fake_db[new_id] = item.dict()
    return {"message": "Nuevo item cerado", "item_id": new_id, "data": fake_db[new_id]}

# PUT
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id in fake_db:
        fake_db[item_id] = item.dict()
        return {"message": "Ítem actualizado", "data": fake_db[item_id]}
    else:
        return {"error": "Ítem no encontrado"}

# PATCH - Actualizar parcialmente un ítem
@app.patch("/items/{item_id}")
def patch_item(item_id: int, item: dict):
    if item_id in fake_db:
        fake_db[item_id].update(item)
        return {"message": "Ítem modificado parcialmente", "data": fake_db[item_id]}
    else:
        return {"error": "Ítem no encontrado"}

# DELETE - Eliminar un ítem
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id in fake_db:
        deleted = fake_db.pop(item_id)
        return {"message": "Ítem eliminado", "data": deleted}
    else:
        return {"error": "Ítem no encontrado"}
