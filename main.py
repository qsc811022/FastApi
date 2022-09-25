#main.py
from fastapi import FastAPI
import schemas;

app = FastAPI()
fakeDatabase = {
    1:{'task':'Clean car'},
    2:{'task':'Write blog'},
    3:{'task':'Start stream'},
}

@app.get("/")
def getItems():
    return fakeDatabase

@app.get("/{id}")
def getItems(id:int):
    return fakeDatabase[id]


@app.post("/")
def addItems(task:schemas.Item):
    newId = len(fakeDatabase.keys())+1
    fakeDatabase[newId] = {"task":task}
    return fakeDatabase