import os
from typing import Optional

import httpx

from errors import (
    BuyerNotFoundError,
    DiscountNotAllowedError,
    ExternalServiceCommunicationError,
    MerchantNotFoundError,
    ProductNotFoundError
)
from responseDtos.merchant_response_dto import MerchantResponseDTO
from responseDtos.product_response_dto import ProductResponseDTO
from order_inputmodel import OrderInputModel
from order_repository import OrderRepository
from order_dto import OrderDTO


class OrderService:

    def __init__(
        self,
        order_repository: OrderRepository,
        request_timeout_seconds: float = 5.0,
    ) -> None:
        self._order_repository = order_repository
        self._merchant_service_base_url = os.getenv("MERCHANT_SERVICE_BASE_URL")
        self._buyer_service_base_url = os.getenv("BUYER_SERVICE_BASE_URL")
        self._inventory_service_base_url = os.getenv("INVENTORY_SERVICE_BASE_URL")
        self._request_timeout_seconds = request_timeout_seconds

    async def create_order(self, order: OrderInputModel) -> int:
        merchant = await self._ensure_merchant_exists_and_fetch(order.merchantId)
        self._validate_discount(discount=order.discount, merchant=merchant)
        await self._ensure_buyer_exists(order.buyerId)
        created_order_id = self._order_repository.save_order(order)
        return created_order_id
    
    def get_order(self, order_id: int) -> Optional[OrderDTO]:
        order_data = self._order_repository.get_order(order_id)
        product = get_product_data
        order_data.totalPrice = product.price * order_data.discount
        if not order_data:
            return None

        return order_data

    async def _ensure_merchant_exists_and_fetch(self, merchant_id: int) -> MerchantResponseDTO:
        url = f"{self._merchant_service_base_url}/merchants/{merchant_id}"
        response = await self._get(url)
        if response.status_code == 404:
            raise MerchantNotFoundError()

        if response.is_error:
            message = (
                f"Unexpected response ({response.status_code}) "
            )
            raise ExternalServiceCommunicationError(message)

        merchant_payload = response.json()
        try:
            return MerchantResponseDTO(**merchant_payload)
        except TypeError as exc:
            message = f"Unexpected merchant payload ({exc})"
            raise ExternalServiceCommunicationError(message)
    

    async def _ensure_product_exists_and_fetch(self, product_id: int) -> ProductResponseDTO:
        url = f"{self._inventory_service_base_url}/products/{product_id}"
        response = await self._get(url)
        if response.status_code == 404:
            raise ProductNotFoundError()

        if response.is_error:
            message = (
                f"Unexpected response ({response.status_code}) "
            )
            raise ExternalServiceCommunicationError(message)

        product_payload = response.json()
        try:
            return ProductResponseDTO(**product_payload)
        except TypeError as exc:
            message = f"Unexpected product payload ({exc})"
            raise ExternalServiceCommunicationError(message)

    def _validate_discount(
        self,
        discount: Optional[float],
        merchant: MerchantResponseDTO,
    ) -> None:
        allows_discount = bool(merchant.allows_discount)
        if discount is None:
            return

        has_discount = float(discount) != 0.0

        if has_discount and not allows_discount:
            raise DiscountNotAllowedError()
        
        
    async def _ensure_buyer_exists(self, buyer_id: int) -> None:
        url = f"{self._buyer_service_base_url}/buyers/{buyer_id}"
        response = await self._get(url)
        if response.status_code == 404:
            raise BuyerNotFoundError()

        if response.is_error:
            message = (
                f"Unexpected response ({response.status_code}) "
            )
            raise ExternalServiceCommunicationError(message)

    async def _get(self, url: str) -> httpx.Response:
        async with httpx.AsyncClient(timeout=self._request_timeout_seconds) as client:
            response = await client.get(url)
        return response
