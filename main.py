from fastapi import FastAPI

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