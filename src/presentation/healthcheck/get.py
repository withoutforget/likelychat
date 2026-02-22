from dataclasses import dataclass, field

from dishka.integrations.fastapi import DishkaRoute, FromDishka
from fastapi import APIRouter

from src.application.auth.auth_service import UserAuthModel


ROUTER = APIRouter(prefix="/healthcheck", route_class=DishkaRoute)


@dataclass(slots=True)
class GetServiceStatusResponse:
    ok: bool
    message: str | None = field(default=None)


@ROUTER.get("/")
async def get_service_status(user: FromDishka[UserAuthModel]) -> GetServiceStatusResponse:
    return GetServiceStatusResponse(ok=True)
