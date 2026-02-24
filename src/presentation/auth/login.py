from dataclasses import dataclass, field

from dishka.integrations.fastapi import DishkaRoute, FromDishka
from fastapi import APIRouter

from src.application.auth.auth_service import AuthService

ROUTER = APIRouter(prefix="/login", route_class=DishkaRoute)


@dataclass(slots=True)
class LoginRequest:
    username: str
    password: str


@dataclass(slots=True)
class LoginResponse:
    token: str | None = field(default=None)


@ROUTER.post("/")
async def login(
    payload: LoginRequest, service: FromDishka[AuthService]
) -> LoginResponse:
    pass
