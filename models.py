import imp
from sqlalchemy import Column, Integer, String
from database import Base

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    task = Column(String(256), nullable=False)

    def __init__(self, task):
        self.task = task

    def __repr__(self):
        return '<Item %r>' % self.task