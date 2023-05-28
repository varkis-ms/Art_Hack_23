from .auth import auth_router
from .health_check import health_check_router
from .user import user_router
from .courses import courses_router
from .task import task_router

list_of_routes = [
    health_check_router,
    auth_router,
    user_router,
    courses_router,
    task_router,
]


__all__ = [
    "list_of_routes",
]
