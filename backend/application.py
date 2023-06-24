from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.core.settings import settings
from backend.task_one.router import router as quadratic_equation_router
from backend.task_two.router import router as colored_objects_router


def create_app() -> FastAPI:
    app = FastAPI(debug=settings.DEBUG, root_path=settings.ROOT_PATH)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    app.include_router(quadratic_equation_router)
    app.include_router(colored_objects_router)

    return app
