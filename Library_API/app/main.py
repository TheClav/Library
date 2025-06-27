from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app import db, models

app = FastAPI()

def get_db():
    database = db.SessionLocal()
    try:
        yield database
    finally:
        database.close()

@app.post("/books", response_model=models.Book)
def create_book(book: models.BookCreate, db_session: Session = Depends(get_db)):
    new_book = db.Book(**book.dict())
    db_session.add(new_book)
    db_session.commit()
    db_session.refresh(new_book)
    return new_book

@app.get("/books", response_model=list[models.Book])
def read_books(db_session: Session = Depends(get_db)):
    return db_session.query(db.Book).all()

@app.get("/books/{book_id}", response_model=models.Book)
def read_book(book_id: int, db_session: Session = Depends(get_db)):
    book = db_session.query(db.Book).filter(db.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.put("/books/{book_id}", response_model=models.Book)
def update_book(book_id: int, updated: models.BookCreate, db_session: Session = Depends(get_db)):
    book = db_session.query(db.Book).filter(db.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    for key, value in updated.dict().items():
        setattr(book, key, value)
    db_session.commit()
    return book

@app.delete("/books/{book_id}")
def delete_book(book_id: int, db_session: Session = Depends(get_db)):
    book = db_session.query(db.Book).filter(db.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    db_session.delete(book)
    db_session.commit()
    return {"message": "Book deleted"}
