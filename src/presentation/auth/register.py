from dataclasses import dataclass, field

from dishka.integrations.fastapi import DishkaRoute, FromDishka
from fastapi import APIRouter

from src.application.auth.auth_service import AuthService
from src.infra.postgres.repo.user.repository import UserRepository

ROUTER = APIRouter(prefix="/register", route_class=DishkaRoute)


@dataclass(slots=True)
class RegisterRequest:
    username: str
    password: str


@dataclass(slots=True)
class RegisterResponse:
    token: str | None = field(default=None)


@ROUTER.post("/")
async def register(
    payload: RegisterRequest, service: FromDishka[AuthService]
) -> RegisterResponse:
    pass
