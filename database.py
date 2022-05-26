from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create sqlite engine instance
engine = create_engine('sqlite:///todo.db', echo=True)

# Create declarative base meta instance
Base = declarative_base()

# Create Session local class for session maker
sessionLocal = sessionmaker(bind=engine, expire_on_commit=False)