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
