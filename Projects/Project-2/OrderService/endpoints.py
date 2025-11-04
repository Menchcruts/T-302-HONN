from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, HTTPException, Response, status

from container import Container
from errors import (
    ExternalServiceCommunicationError,
    OrderServiceError
)
from order_inputmodel import OrderInputModel
from order_service import OrderService

router = APIRouter()


@router.post("/orders", status_code=status.HTTP_201_CREATED)
@inject
async def create_order(
    order: OrderInputModel,
    order_service: OrderService = Depends(
        Provide[Container.order_service_provider]
    ),
) -> Response:
    try:
        order_id = await order_service.create_order(order)
    except ExternalServiceCommunicationError as error:
        raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail=str(error))
    except OrderServiceError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error))

    return Response(
        content=str(order_id),
        status_code=status.HTTP_201_CREATED,
        headers={"Location": f"/orders/{order_id}"},
        media_type="text/plain",
    )

@router.get("/orders/{id}", status_code=200)
@inject
async def get_merchant(
    id: int,
    order_service: OrderService = Depends(
        Provide[Container.order_service_provider]
    )
):
    order = order_service.get_merchant(id=id)

    if not order:
        resp = Response(
            content="order not found",
            status_code=404
        )
        return resp
    return order

