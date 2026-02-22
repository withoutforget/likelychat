from dataclasses import dataclass, field

from dishka.integrations.fastapi import DishkaRoute, FromDishka
from fastapi import APIRouter, HTTPException

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
    # dummy, replace later
    if payload.username == "root" and payload.password == "123456":  # noqa: S105 // ignoring Possible hardcoded password assigned to
        token = service.create_token(1, "root")
        return LoginResponse(token=token)
    raise HTTPException(
        status_code=401, detail={"message": "invalid credentionals"}
    )
