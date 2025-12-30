#this is the initial version of code from which the learing starts 2)
from fastapi import FastAPI, status
from typing import List
from fastapi.exceptions import HTTPException

from src.books.book_data import books
from src.books.schema import Book,BookUpdateModel

app = FastAPI()







@app.get("/books", response_model=List[Book])
async def get_all_books():
    return books


@app.get("/book/{book_id}")
async def get_book(book_id: int) -> dict:
    for book in books:
        if books[book_id] == book:
            return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found"
    )


# The `response_model` parameter ensures that the data returned by this endpoint
# matches a defined Pydantic schema. It validates and serializes the output,
# strips out any extra fields, and makes the OpenAPI docs clear.
# Use a single model (e.g., User) when returning one object,
# or a list (e.g., List[User]) when returning multiple objects.
#
# In Python, the typing module provides type hints for static analysis and clarity.
# List is a generic type that lets you specify what kind of elements a list contains.
# Example: List[int] means “a list of integers,” while List[User] means “a list of User models.”


@app.post("/books", status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data: Book) -> dict:
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book


"""
Parameter inference rules in FastAPI:
- Path: If a parameter name matches {} in the route, FastAPI knows it’s a path variable.
- Query: Simple types (int, str, bool) not in the path are assumed to come from the query string.
- Body: Complex types (Pydantic models, dicts, lists) are assumed to come from the request body.
- Header: Must be explicitly declared with Header(), not inferred automatically.
Helpers like Body(), Query(), Path(), Header() are for extra control (metadata, defaults, etc.).
"""


# Workflow summary:
# 1. Client sends HTTP request (method, path, headers, body).
# 2. ASGI server (Uvicorn/Hypercorn) passes request to FastAPI (still in dict form).
# 3. Router matches path + method to the correct endpoint.
# 4. Parameters are resolved:
#    - Path params → extracted from URL
#    - Query params → parsed from query string
#    - Body params → parsed & validated with Pydantic
#    - Header/Cookie → only if explicitly declared
# 5. Pydantic validates and converts inputs into clean Python objects.
# 6. Endpoint function is executed with these parameters.
# 7. Response is validated against response_model (if set), serialized to JSON.
# 8. ASGI server sends final response back to the client.



@app.patch("/book/{book_id}")
async def update_book(book_id: int,book_update_data:BookUpdateModel) -> dict:
     for book in books:
         if book['id'] == book_id:
             book['title'] = book_update_data.title
             book['author'] = book_update_data.author
             book['publisher'] == book_update_data.publisher
             book['page_count'] = book_update_data.page_count
             book['language'] = book_update_data.language
             return book
     raise HTTPException (status_code = status.HTTP_404_NOT_FOUND,detail="book not found")



@app.delete("/book/{book_id}")
async def delete_book(book_id: int) -> dict :
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return {}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="book not found to delete")