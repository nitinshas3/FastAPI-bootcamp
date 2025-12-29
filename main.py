from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
async def read_root():
    return{"message":"hello world"}

@app.get('/greet/{name}')
async def greet_name(name:Optional[str]='nitin',age:int =0) ->dict: #-> is used to define the return type
    return{"message":f"hello {name}" , "age" : age}# path and query parameter

class BookCreateModel(BaseModel):
    title : str
    author : str


@app.post('/create_book')
async def create_book(book_data:BookCreateModel):
    return{
        'title':book_data.title,
        'author':book_data.author
    }
'''In HTTP, request headers are used to send metadata that gives the server context about a request, rather than the actual data itself. Headers tell the server who is making the request (User-Agent), what type of response the client can handle (Accept), how the request body should be parsed (Content-Type), and whether the request is authenticated and authorized (Authorization). Authentication and authorization information is placed in headers because headers are read first when a request arrives, allowing the server to quickly verify identity and permissions before spending time parsing and processing the request body, which improves efficiency and follows standard API design practices. The request body is sent directly and independently of headers; headers do not contain the body but only describe how it should be interpreted or whether the request should be allowed at all. Accessing headers is also useful for content negotiation, client or device detection, API versioning, and request-level decision making. In FastAPI, headers are accessed explicitly by declaring them as parameters using Header() in the path operation function, which enables automatic validation, clear function signatures, and proper API documentation in Swagger/OpenAPI. This approach encourages clean, secure, and well-structured backend development.'''

from fastapi import Header

@app.get('/get_headers')
async def get_headers(
    accept:str = Header(None),
    content_type :str =Header(None),
    user_agent:str = Header(None),
    host:str = Header(None)
):
    request_headers = {}
    request_headers['Accept'] = accept
    request_headers['Content-Type'] = content_type
    request_headers['User_Agent'] = user_agent
    request_headers['Host'] = host
    return request_headers
'''''Why FastAPI makes headers explicit

FastAPI:

Forces you to declare where data comes from

Avoids ambiguity

Improves validation

Generates documentation

Header() → headers
Query() → URL query
Path() → URL path
Body() → request body'''