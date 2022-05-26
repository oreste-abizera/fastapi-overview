from fastapi import FastAPI, Body, Depends
import schemas

import models
from database import Base, engine, sessionLocal
from sqlalchemy.orm import Session

import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

# This will create our database if it doesn't exist
Base.metadata.create_all(bind=engine)

def get_session():
    sesion = sessionLocal()
    try:
        yield sesion
    finally:
        sesion.close()

app = FastAPI()

fakeDatabase = {
    1: {'task': "Clean Car"},
    2: {'task': "Write Blog"},
    3: {'task': "Learn Python"},
}

@app.get("/")
def getItems(session: Session = Depends(get_session)):
    items = session.query(models.Item).all()
    return items

@app.get("/{id}")
def getItem(id: int, session: Session = Depends(get_session)):
    item = session.query(models.Item).get(id)
    return item

#Option # 1
# @app.post("/")
# def addItem(task: str):
#     newId = len(fakeDatabase.keys()) + 1
#     fakeDatabase[newId] = {'task': task}
#     return fakeDatabase

# Option # 2
@app.post("/")
def addItem(item: schemas.Item, session: Session = Depends(get_session)):
    item = models.Item(task=item.task)
    session.add(item)
    session.commit()
    session.refresh(item)
    return item

# OPTION # 3
# @app.post("/")
# def addItem(body = Body()):
#     newId = len(fakeDatabase.keys()) + 1
#     fakeDatabase[newId] = {'task': body["task"]}

@app.put("/{id}")
def updateItem(id: int, item: schemas.Item, session: Session = Depends(get_session)):
    itemObject = session.query(models.Item).get(id)
    itemObject.task = item.task
    session.commit()
    return itemObject

@app.delete("/{id}")
def deleteItem(id: int, session: Session = Depends(get_session)):
    itemObject = session.query(models.Item).get(id)
    session.delete(itemObject)
    session.commit()
    session.close()
    return 'Item deleted'
