from dataclasses import dataclass, field
import bcrypt

from dishka.integrations.fastapi import DishkaRoute, FromDishka
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

from src.application.auth.auth_service import AuthService
from src.infra.postgres.repo.user.repository import UserRepository


ROUTER = APIRouter(prefix="/login", route_class=DishkaRoute)


class LoginRequest(BaseModel):
    username: str
    password: str



class LoginResponse(BaseModel):
    token: str | None = field(default=None)


@ROUTER.post("/")
async def login(
    payload: LoginRequest, 
    service: FromDishka[AuthService],
    rep: FromDishka[UserRepository]
) -> LoginResponse:
    if await rep.exists(payload.username):
        user = await rep.get_by_username(payload.username)
        if bcrypt.checkpw(payload.password.encode('utf-8'), user.password.encode('utf-8')):
            token = service.create_token(user.id, user.username)
            return LoginResponse(token=token)
        else:
            raise HTTPException(
            status_code= 401,
            detail= "invalid username or password"
        )
    else:
        raise HTTPException(
            status_code= 401,
            detail= "invalid username or password"
        )
