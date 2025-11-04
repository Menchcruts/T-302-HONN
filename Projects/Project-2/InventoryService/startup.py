import threading

import uvicorn
from fastapi import FastAPI

from app.container import Container
import app.product_endpoints as endpoints

import integrations.payment_service

def create_app() -> FastAPI:
    threading.Thread(target=integrations.payment_service.main, daemon=True).start()

    container = Container()
    container.wire(modules=[endpoints])

    app = FastAPI()
    app.container = container
    app.include_router(endpoints.router)

    return app


app = create_app()

if __name__ == '__main__':
    uvicorn.run('startup:app', host='0.0.0.0', port=8000, reload=True)