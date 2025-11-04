from dataclasses import asdict

from app.container import Container
from dependency_injector.wiring import Provide, inject

from fastapi import APIRouter, Depends, Response, status

from app.product_repo import ProductRepository
from app.create_product_dto import CreateProductDto
from app.product import Product

router = APIRouter()

@router.get("/products/{id}", status_code=status.HTTP_200_OK)
@inject
async def get_product(
    id: int,
    product_repo: ProductRepository = Depends(Provide[Container.product_repo_provider])
) -> Product:
    product = product_repo.get_product(id=id)

    if not product:
        resp = Response(
            content="Product not found",
            status_code=status.HTTP_404_NOT_FOUND
        )
        return resp

    return product


@router.post("/products", status_code=status.HTTP_201_CREATED)
@inject
async def post_product(
    product: CreateProductDto,
    product_repo: ProductRepository = Depends(Provide[Container.product_repo_provider])
) -> int:
    created_id = product_repo.save_product(product)

    resp = Response(
        content=str(created_id),
        status_code=status.HTTP_201_CREATED,
        headers={"Location":f"/products/{created_id}"}
    )
    return resp