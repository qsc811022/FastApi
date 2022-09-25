#main.py
from fastapi import FastAPI, Body
import schemas

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
def addItem(item:schemas.Item):
    newId = len(fakeDatabase.keys()) + 1
    fakeDatabase[newId] = {"task":item.task}
    return fakeDatabase



@app.put("/{id}")
def updateItems(id:int, item:schemas.Item):
    fakeDatabase[id]['task'] = item.task
    return fakeDatabase



@app.delete("/{id}")
def deleteItems(id:int):
    del fakeDatabase[id]
    return fakeDatabase