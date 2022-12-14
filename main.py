# uvicorn main:app --reload
from fastapi import FastAPI, Body,Depends
import schemas
app = FastAPI()
fakeDatabase = {
    1:{'task':'Clean car'},
    2:{'task':'Write blog'},
    3:{'task':'Start stream'},
}

# @app.get("/")
# def getItems():
#     return fakeDatabase

@app.get("/{id}")
def getItem(id:int):
    return fakeDatabase[id]

@app.get("/{id}")
def getItem(id:int):
    return fakeDatabase[id]

@app.post("/")
def addItem(body = Body()):
   newId = len(fakeDatabase.keys()) + 1
   fakeDatabase[newId] = {"task":body['task']}
   return fakeDatabase



@app.put("/{id}")
def updateItem(id:int, item:schemas.Item):
    fakeDatabase[id]['task'] = item.task 
    return fakeDatabase


@app.delete("/{id}")
def deleteItem(id:int):
    del fakeDatabase[id]
    return fakeDatabase