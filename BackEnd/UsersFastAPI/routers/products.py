from fastapi import APIRouter


# APIRouter() is used to define a modular router in FastAPI, allowing better organization of API endpoints.
# This router will handle all routes related to "products".

router = APIRouter(
    prefix="/products",  # Sets a common prefix for all routes in this router (e.g., "/products/{id}").
    tags=["products"],  # Tags help categorize routes in the automatic API documentation (Swagger UI).
    responses={404: {"message": "Not Found"}}  # Defines a default response for 404 errors.
)


products_list = ["Product 1", "Product 2", "Product 3", "Product 4", "Product 5"]
@router.get("/")
async def products():
    return products_list


@router.get("/{id}")
async def products(id: int):
    return products_list[id]