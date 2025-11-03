import uvicorn
from container import Container
from fastapi import FastAPI

import endpoints


def create_app() -> FastAPI:
    container = Container()
    container.wire(modules=[endpoints])

    app = FastAPI()
    app.container = container
    app.include_router(endpoints.router)

    return app


app = create_app()

if __name__ == '__main__':
    uvicorn.run('startup:app', host='0.0.0.0', port=8001, reload=True)
