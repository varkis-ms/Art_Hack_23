from .health_check import health_check_router
from .auth import user_router


list_of_routes = [
    health_check_router,
    user_router,
]


__all__ = [
    "list_of_routes",
]
