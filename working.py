from fastapi import FastAPI, Path

app = FastAPI()


'''
HTTP VERBS
GET
POST
PUT
DELETE etc.'''
@app.get("/")
def home():
    return {"data":"Testing"} 

@app.get("/about")
def about():
    return {"Data": "About"}

inventory = {
    1: {
        "name":"Milk",
        "price": 3.99,
        "brand": "Regular"
    }
}

@app.get("/get-item/{item_id}")
def get_item(item_id: int):
    return inventory[item_id]

@app.get("/get-items/{items_id}/{name}")
def get_items(items_id: int, name: str):
    return inventory[items_id]
# Path function
'''@app.get("/gets_item/{items_id}")
def gets_item(items_id: int = Path(None, description="The ID of the item you would like to view")):
    return inventory[items_id] '''
# python -m uvicorn main:app --reload --command to run uvicorn.