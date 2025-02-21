from fastapi import FastAPI
from routers import products, users  # Including routers in the FastAPI application
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Routers
app.include_router(products.router)  # Includes the 'products' router, which handles product-related endpoints.
app.include_router(users.router) # Includes the 'users' router, which manages user-related endpoints.

# Static Resources
app.mount(
    "/static",  # URL path where the static files will be accessible (e.g., /static/style.css).
    StaticFiles(directory="static"),  # Specifies the directory ("static") where static files are stored.
    name='static'  # Optional name for this mounted route, useful for reference and debugging.
)

@app.get("/")
async def root():
    return "Hello FastAPI!"

@app.get("/url_oscar")
async def url():
    return {"url_course": "https://devdata.com/python"}


"""
To run the FastAPI application, execute the following commands in the terminal:
1. Start the development server using:
    fastapi dev main.py

2. Alternatively, run the application with Uvicorn:
    uvicorn main:app --reload
The `--reload` flag enables automatic reloading for code changes.

Documemtation with Swagger: https://127.0.0.1:8000/docs
Documemtation with Redocly: https://127.0.0.1:8000/redoc

"""