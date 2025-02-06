from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel

app = FastAPI()

books = [
    {'id':1,
    'title': "Асинхронность в Pyhton",
    'author': "Мэттью"},
    {'id':2,
    'title': "Backend разработка на python",
    'author': 'Женя'}
]

@app.get('/')
def hw():
    return "Hello World!"

@app.get(
    '/books',
    tags=["Книги 😱"],
    summary="Получить конкретную книгу")
def read_books():
    return books

@app.get(
    "/books/{book_id}",
    tags=["Книги 😱"],
    summary = "Получить все книги")
def get_book(book_id: int):
    for book in books:
        if book['id'] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


class NewBook(BaseModel):
    title: str
    author: str


@app.post("/authors")
def create_book(new_book:NewBook):
    books.append({
        "id": len(books) + 1,
         "title": new_book.title,
         "author":new_book.author
    })
    return {"success": True, "message": "Книга успешно добавлена"}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
