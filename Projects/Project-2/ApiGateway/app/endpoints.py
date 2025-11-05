from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, HTTPException, Response, status
from typing import Dict, Any

from app.container import Container
from gateway_service import GatewayService

router = APIRouter(prefix="/api")

@router.post("/orders", status_code=status.HTTP_201_CREATED)
@inject
async def create_order(
    order: Dict[str, Any],
    gateway_service: GatewayService = Depends(
        Provide[Container.gateway_service_provider]
    ),
) -> Response:
    response = await gateway_service.create_order(order)

    return response

@router.get("/orders/{id}", status_code=200)
@inject
async def get_order(
    id: int,
    gateway_service: GatewayService = Depends(
        Provide[Container.gateway_service_provider]
    )
):
    response = await gateway_service.get_order(order_id=id)
    return response



@router.post("/merchants", status_code=status.HTTP_201_CREATED)
@inject
async def create_merchant(
    merchant: Dict[str, Any],
    gateway_service: GatewayService = Depends(
        Provide[Container.gateway_service_provider]
    ),
) -> Response:
    response = await gateway_service.create_merchant(merchant)

    return response

@router.get("/merchants/{id}", status_code=200)
@inject
async def get_merchant(
    id: int,
    gateway_service: GatewayService = Depends(
        Provide[Container.gateway_service_provider]
    )
):
    response = await gateway_service.get_merchant(merchant_id=id)
    return response

@router.post("/products", status_code=status.HTTP_201_CREATED)
@inject
async def create_product(
    product: Dict[str, Any],
    gateway_service: GatewayService = Depends(
        Provide[Container.gateway_service_provider]
    ),
) -> Response:
    response = await gateway_service.create_product(product)

    return response

@router.get("/products/{id}", status_code=200)
@inject
async def get_product(
    id: int,
    gateway_service: GatewayService = Depends(
        Provide[Container.gateway_service_provider]
    )
):
    response = await gateway_service.get_product(product_id=id)
    return response

@router.post("/buyers", status_code=status.HTTP_201_CREATED)
@inject
async def create_buyer(
    buyer: Dict[str, Any],
    gateway_service: GatewayService = Depends(
        Provide[Container.gateway_service_provider]
    ),
) -> Response:
    response = await gateway_service.create_buyer(buyer)

    return response

@router.get("/buyers/{id}", status_code=200)
@inject
async def get_buyer(
    id: int,
    gateway_service: GatewayService = Depends(
        Provide[Container.gateway_service_provider]
    )
):
    response = await gateway_service.get_buyer(buyer_id=id)
    return response