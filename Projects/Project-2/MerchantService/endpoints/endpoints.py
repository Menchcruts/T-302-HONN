import json

from container import Container
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Response
from merchant_repository import MerchantRepository
from models.merchant_model import MerchantModel

router = APIRouter()


@router.get("/merchants/{id}", status_code=200)
@inject
async def get_merchant(
    id: int,
    merchant_repository: MerchantRepository = Depends(
        Provide[Container.merchant_repository_provider]
    )
):
    merchant = merchant_repository.get_merchant(id=id)
    return merchant


@router.post("/merchants", status_code=201)
@inject
async def save_merchant(
    merchant: MerchantModel,
    merchant_repository: MerchantRepository = Depends(
        Provide[Container.merchant_repository_provider]
    ),
):
    json_data = merchant.json()
    data = json.loads(json_data)

    created_id = merchant_repository.save_merchant(merchant)

    resp = Response(
        content=str(created_id),
        status_code=201,
        headers={"Location": f"/merchants/{created_id}"}
    )
    return resp