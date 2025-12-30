from fastapi import FastAPI
from src.books.routes import book_router

version = 'v1' #api versioning

app = FastAPI(
    version= version,
    title="BOOKLY",
    description="A rest api for book review webservice"
)

app.include_router(book_router,prefix=f"/api/{version}/books")