import os
from typing import Optional

import httpx
from dataclasses import asdict

from errors import (
    BuyerNotFoundError,
    DiscountNotAllowedError,
    ExternalServiceCommunicationError,
    MerchantNotFoundError,
    ProductNotFoundError,
    ProductMerchantMismatch,
    ProductOutOfStock
)
from responseDtos.buyer_response_dto import BuyerResponseDTO
from responseDtos.merchant_response_dto import MerchantResponseDTO
from responseDtos.product_response_dto import ProductResponseDTO
from order_inputmodel import OrderInputModel
from order_repository import OrderRepository
from order_dto import OrderDTO
from order_event_publisher import OrderEventPublisher


class OrderService:

    def __init__(
        self,
        order_repository: OrderRepository,
        order_event_publisher: OrderEventPublisher,
        request_timeout_seconds: float = 5.0,
    ) -> None:
        self._order_repository = order_repository
        self._order_event_publisher = order_event_publisher
        self._merchant_service_base_url = os.getenv("MERCHANT_SERVICE_BASE_URL")
        self._buyer_service_base_url = os.getenv("BUYER_SERVICE_BASE_URL")
        self._inventory_service_base_url = os.getenv("INVENTORY_SERVICE_BASE_URL")
        self._request_timeout_seconds = request_timeout_seconds

    async def create_order(self, order: OrderInputModel) -> int:
        merchant = await self._ensure_merchant_exists_and_fetch(order.merchant_id)
        self._validate_discount(discount=order.discount, merchant=merchant)
        product = await self._ensure_product_exists_and_fetch(order.product_id)

        self._ensure_product_belongs_to_merchant(product, order.merchant_id)

        buyer = await self._ensure_buyer_exists_and_fetch(order.buyer_id)
        created_order_id = self._order_repository.save_order(order)

        await self._reserve_product(order.product_id)

        discount_value = float(order.discount or 0.0)
        total_price = product.price * (1 - discount_value)

        order_event_payload = {
            "order_id": created_order_id,
            "product_name": product.product_name,
            "total_price": total_price,
            "buyer_name": buyer.name,
            "buyer_email": buyer.email,
            "merchant_name": merchant.name,
            "merchant_email": merchant.email,
            "credit_card": asdict(order.credit_card)
        }
        self._order_event_publisher.publish(order_event_payload)

        return created_order_id
    
    async def get_order(self, order_id: int) -> Optional[OrderDTO]:
        order_data = self._order_repository.get_order(order_id)
        if not order_data:
            return None

        product = await self._ensure_product_exists_and_fetch(order_data.product_id)
        totalPrice = product.price * (1 - order_data.discount)

        order = OrderDTO(
            product_id=order_data.product_id,
            merchant_id=order_data.merchant_id,
            buyer_id=order_data.buyer_id,
            card_number=self._hash_card_number(order_data.card_number),
            total_price=totalPrice
        )

        return order

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

    async def _reserve_product(self, product_id: int) -> None:
        url = f"{self._inventory_service_base_url}/products/reserve/{product_id}"
        response = await self._put(url)
        if response.status_code == 400:
            raise ProductOutOfStock()
        

    def _hash_card_number(self, cc_number: str) -> str:
        str_len = len(cc_number)
        stars = str_len - 4
        return "*"*stars + cc_number[-4:]

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
        
    def _ensure_product_belongs_to_merchant(
        self,  
        product: ProductResponseDTO,
        merchant_id: int
    ) -> bool:
        if product.merchant_id != merchant_id: 
            raise ProductMerchantMismatch()
        return True

        
    async def _ensure_buyer_exists_and_fetch(self, buyer_id: int) -> BuyerResponseDTO:
        url = f"{self._buyer_service_base_url}/buyers/{buyer_id}"
        response = await self._get(url)
        if response.status_code == 404:
            raise BuyerNotFoundError()

        if response.is_error:
            message = (
                f"Unexpected response ({response.status_code}) "
            )
            raise ExternalServiceCommunicationError(message)

        buyer_payload = response.json()
        try:
            return BuyerResponseDTO(**buyer_payload)
        except TypeError as exc:
            message = f"Unexpected buyer payload ({exc})"
            raise ExternalServiceCommunicationError(message)

    async def _get(self, url: str) -> httpx.Response:
        async with httpx.AsyncClient(timeout=self._request_timeout_seconds) as client:
            response = await client.get(url)
        return response

    async def _put(self, url: str) -> httpx.Response:
        async with httpx.AsyncClient(timeout=self._request_timeout_seconds) as client:
            response = await client.put(url)
        return response
