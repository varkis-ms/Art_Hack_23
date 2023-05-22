from .auth import auth_router
from .health_check import health_check_router
from .user import user_router

list_of_routes = [
    health_check_router,
    auth_router,
    user_router,
]


__all__ = [
    "list_of_routes",
]
