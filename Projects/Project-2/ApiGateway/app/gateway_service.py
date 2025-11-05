import os
from typing import Optional, Dict, Any

import httpx
from dataclasses import asdict

class GatewayService:

    def __init__(
        self,
        request_timeout_seconds: float = 5.0,
    ) -> None:
        self._request_timeout_seconds = request_timeout_seconds
        self.order_service_base_url = os.getenv("ORDER_SERVICE_BASE_URL")
        self.merchant_service_base_url = os.getenv("MERCHANT_SERVICE_BASE_URL")
        self.buyer_service_base_url = os.getenv("BUYER_SERVICE_BASE_URL")
        self.inventory_service_base_url = os.getenv("INVENTORY_SERVICE_BASE_URL")

    async def create_order(self, order_data: Dict[str, Any]) -> int:
        response = await self._post(f"{self.order_service_base_url}/orders", order_data)
        return response
    
    async def get_order(self, order_id: int) -> Dict[str, Any]:
        response = await self._get(f"{self.order_service_base_url}/orders/{order_id}")
        return response

    async def create_buyer(self, buyer_data: Dict[str, Any]) -> int:
        response = await self._post(f"{self.buyer_service_base_url}/buyers", buyer_data)
        return response.text
    
    async def get_buyer(self, buyer_id: int) -> Dict[str, Any]:
        response = await self._get(f"{self.buyer_service_base_url}/buyers/{buyer_id}")
        return response

    async def create_merchant(self, merchant_data: Dict[str, Any]) -> int:
        response = await self._post(f"{self.merchant_service_base_url}/merchants", merchant_data)
        return response
    
    async def get_merchant(self, merchant_id: int) -> Dict[str, Any]:
        response = await self._get(f"{self.merchant_service_base_url}/merchants/{merchant_id}")
        return response
        

    async def create_product(self, product_data: Dict[str, Any]) -> int:
        response = await self._post(f"{self.inventory_service_base_url}/products", product_data)
        return response
    
    async def get_product(self, product_id: int) -> Dict[str, Any]:
        response = await self._get(f"{self.inventory_service_base_url}/products/{product_id}")
        return response

    async def _get(self, url: str) -> httpx.Response:
        async with httpx.AsyncClient(timeout=self._request_timeout_seconds) as client:
            response = await client.get(url)
        return response

    async def _post(self, url: str, json_data: Dict[str, Any]) -> httpx.Response:
        async with httpx.AsyncClient(timeout=self._request_timeout_seconds) as client:
            response = await client.post(url, json=json_data)
        return response
