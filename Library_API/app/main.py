from fastapi import FastAPI, HTTPException, Depends, Response, status
from sqlalchemy.orm import Session

from app import db, models, schemas

app = FastAPI()

# run once at startup
@app.on_event("startup")
def init_db() -> None:
    models.Base.metadata.create_all(bind=db.engine)

# DB session dependency
def get_db():
    session = db.SessionLocal()
    try:
        yield session
    finally:
        session.close()

# ───── CRUD routes ─────────────────────────────────────────

@app.post("/books", response_model=schemas.Book, status_code=status.HTTP_201_CREATED)
def create_book(book: schemas.BookCreate, db_session: Session = Depends(get_db)):
    new_book = models.Book(**book.dict())
    db_session.add(new_book)
    db_session.commit()
    db_session.refresh(new_book)
    return new_book

@app.get("/books", response_model=list[schemas.Book])
def read_books(db_session: Session = Depends(get_db)):
    return db_session.query(models.Book).all()

@app.get("/books/{book_id}", response_model=schemas.Book)
def read_book(book_id: int, db_session: Session = Depends(get_db)):
    book = db_session.query(models.Book).get(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.put("/books/{book_id}", response_model=schemas.Book)
def update_book(book_id: int, updated: schemas.BookCreate, db_session: Session = Depends(get_db)):
    book = db_session.query(models.Book).get(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    for k, v in updated.dict().items():
        setattr(book, k, v)

    db_session.commit()
    db_session.refresh(book)
    return book

@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db_session: Session = Depends(get_db)):
    book = db_session.query(models.Book).get(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    db_session.delete(book)
    db_session.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
