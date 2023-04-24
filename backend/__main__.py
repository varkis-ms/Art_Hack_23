from logging import getLogger

from fastapi import FastAPI
from uvicorn import run

from backend.config import DefaultSettings
from backend.config.utils import get_settings
from backend.endpoints import list_of_routes
from backend.utils.common import get_hostname

logger = getLogger(__name__)


def bind_routes(application: FastAPI, setting: DefaultSettings) -> None:
    for route in list_of_routes:
        application.include_router(route, prefix=setting.PATH_PREFIX)


def get_app() -> FastAPI:
    description = "Backend мобильного приложения для популяризации искусства"

    tags_metadata = [
        {
            "name": "Health check",
            "description": "Тестовая ручка для проверки работоспособности сервера",
        },
        {
            "name": "auth",
            "description": "Ручка регистриции, аутентификации и авторизации пользователей",
        },
    ]

    application = FastAPI(
        title="Backend for art",
        description=description,
        docs_url="/swagger",
        openapi_url="/openapi",
        version="0.1.0",
        openapi_tags=tags_metadata,
    )
    settings = get_settings()
    bind_routes(application, settings)
    application.state.settings = settings
    return application


app = get_app()


if __name__ == "__main__":
    settings_for_application = get_settings()
    run(
        "backend.__main__:app",
        host=get_hostname(settings_for_application.APP_HOST),
        port=settings_for_application.APP_PORT,
        reload=True,
        reload_dirs=["backend", "tests"],
        log_level="debug",
    )
