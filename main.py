from fastapi import FastAPI, Body
import schemas

app = FastAPI()

fakeDatabase = {
    1: {'task': "Clean Car"},
    2: {'task': "Write Blog"},
    3: {'task': "Learn Python"},
}

@app.get("/")
def getItems():
    return fakeDatabase

@app.get("/{id}")
def getItem(id: int):
    return fakeDatabase[id]

#Option # 1
@app.post("/")
def addItem(task: str):
    newId = len(fakeDatabase.keys()) + 1
    fakeDatabase[newId] = {'task': task}
    return fakeDatabase

# Option # 2
@app.post("/")
def addItem(item: schemas.Item):
    newId = len(fakeDatabase.keys()) + 1
    fakeDatabase[newId] = {'task': item.task}
    return fakeDatabase

# OPTION # 3
# @app.post("/")
# def addItem(body = Body()):
#     newId = len(fakeDatabase.keys()) + 1
#     fakeDatabase[newId] = {'task': body["task"]}

@app.put("/{id}")
def updateItem(id: int, item: schemas.Item):
    fakeDatabase[id]["task"] = item.task
    return fakeDatabase

@app.delete("/{id}")
def deleteItem(id: int):
    del fakeDatabase[id]
    return fakeDatabase