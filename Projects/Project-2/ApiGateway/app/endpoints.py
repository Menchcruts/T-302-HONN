from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, HTTPException, Response, status
from typing import Dict, Any

from app.container import Container
from app.gateway_service import GatewayService

router = APIRouter(prefix="/api")

@router.post("/orders", status_code=status.HTTP_201_CREATED)
@inject
async def create_order(
    order: Dict[str, Any],
    gateway_service: GatewayService = Depends(
        Provide[Container.gateway_service_provider]
    ),
) -> Response:
    order_id = await gateway_service.create_order(order)

    return Response(
        content=str(order_id),
        status_code=status.HTTP_201_CREATED,
        headers={"Location": f"{router.prefix}/orders/{order_id}"},
        media_type="text/plain",
    )

@router.get("/orders/{id}", status_code=200)
@inject
async def get_order(
    id: int,
    gateway_service: GatewayService = Depends(
        Provide[Container.gateway_service_provider]
    )
):
    order = await gateway_service.get_order(order_id=id)
    if not order:
        resp = Response(
            content="Order not found",
            status_code=404
        )
        return resp
    return order

@router.post("/merchants", status_code=status.HTTP_201_CREATED)
@inject
async def create_merchant(
    merchant: Dict[str, Any],
    gateway_service: GatewayService = Depends(
        Provide[Container.gateway_service_provider]
    ),
) -> Response:
    merchant_id = await gateway_service.create_merchant(merchant)
    return Response(
        content=str(merchant_id),
        status_code=status.HTTP_201_CREATED,
        headers={"Location": f"{router.prefix}/merchants/{merchant_id}"},
        media_type="text/plain",
    )

@router.get("/merchants/{id}", status_code=200)
@inject
async def get_merchant(
    id: int,
    gateway_service: GatewayService = Depends(
        Provide[Container.gateway_service_provider]
    )
):
    merchant = await gateway_service.get_merchant(merchant_id=id)
    if not merchant:
        resp = Response(
            content="Merchant not found",
            status_code=404
        )
        return resp
    return merchant

@router.post("/products", status_code=status.HTTP_201_CREATED)
@inject
async def create_product(
    product: Dict[str, Any],
    gateway_service: GatewayService = Depends(
        Provide[Container.gateway_service_provider]
    ),
) -> Response:
    product_id = await gateway_service.create_product(product)
    return Response(
        content=str(product_id),
        status_code=status.HTTP_201_CREATED,
        headers={"Location": f"{router.prefix}/products/{product_id}"},
        media_type="text/plain",
    )

@router.get("/products/{id}", status_code=200)
@inject
async def get_product(
    id: int,
    gateway_service: GatewayService = Depends(
        Provide[Container.gateway_service_provider]
    )
):
    product = await gateway_service.get_product(product_id=id)
    if not product:
        resp = Response(
            content="Product not found",
            status_code=404
        )
        return resp
    return product

@router.post("/buyers", status_code=status.HTTP_201_CREATED)
@inject
async def create_buyer(
    buyer: Dict[str, Any],
    gateway_service: GatewayService = Depends(
        Provide[Container.gateway_service_provider]
    ),
) -> Response:
    buyer_id = await gateway_service.create_buyer(buyer)
    return Response(
        content=str(buyer_id),
        status_code=status.HTTP_201_CREATED,
        headers={"Location": f"{router.prefix}/buyers/{buyer_id}"},
        media_type="text/plain",
    )

@router.get("/buyers/{id}", status_code=200)
@inject
async def get_buyer(
    id: int,
    gateway_service: GatewayService = Depends(
        Provide[Container.gateway_service_provider]
    )
):
    buyer = await gateway_service.get_buyer(buyer_id=id)
    if not buyer:
        resp = Response(
            content="Buyer not found",
            status_code=404
        )
        return resp
    return buyer