from fastapi import FastAPI

import endpoints.user_endpoints as user_endpoints
import endpoints.movie_endpoints as movie_endpoints
import endpoints.pricing_endpoints as pricing_endpoints
import endpoints.subscription_endpoints as subscription_endpoints


def __get_endpoint_modules():
    return [user_endpoints, movie_endpoints, pricing_endpoints, subscription_endpoints]


def create_app() -> FastAPI:
    endpoint_modules = __get_endpoint_modules()
    app = FastAPI()
    for module in endpoint_modules:
        app.include_router(module.router)
    return app
