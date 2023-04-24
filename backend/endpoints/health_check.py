from fastapi import APIRouter, status

from backend.schemas import PingResponse

health_check_router = APIRouter(tags=["Health check"])


@health_check_router.get(
    "/health_check/ping",
    response_model=PingResponse,
    status_code=status.HTTP_200_OK,
)
async def health_check():
    return PingResponse()
