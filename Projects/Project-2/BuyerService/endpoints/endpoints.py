import json

from container import Container
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Response
from repo.buyer_repository import BuyerRepository
from models.input.buyer import Buyer

router = APIRouter()


@router.get("/buyers/{id}", status_code=200)
@inject
async def get_buyer(
    id: int,
    buyer_repository: BuyerRepository = Depends(
        Provide[Container.buyer_repository_provider]
    )
):
    buyer = buyer_repository.get_buyer(id=id)

    if not buyer:
        resp = Response(
            content="Buyer not found",
            status_code=404
        )
        return resp
    
    return buyer


@router.post("/buyers", status_code=201)
@inject
async def save_buyer(
    buyer: Buyer,
    buyer_repository: BuyerRepository = Depends(
        Provide[Container.buyer_repository_provider]
    ),
):
    json_data = buyer.json()
    data = json.loads(json_data)

    created_id = buyer_repository.save_buyer(buyer)

    resp = Response(
        content=str(created_id),
        status_code=201,
        headers={"Location": f"/buyers/{created_id}"}
    )
    return resp