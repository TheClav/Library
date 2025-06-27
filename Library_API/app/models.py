from sqlalchemy import Column, Integer, String, Date
from .db import Base     # import the Base you created in db.py

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    genre = Column(String)
    status = Column(String, nullable=False)      # read / reading / want
    rating = Column(Integer)
    review = Column(String)
    completion_date = Column(Date)
