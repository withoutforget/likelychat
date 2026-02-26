from dataclasses import dataclass, field

from dishka.integrations.fastapi import DishkaRoute, FromDishka
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

from src.application.auth.auth_service import AuthService
from src.infra.postgres.repo.user.repository import UserRepository

ROUTER = APIRouter(prefix="/register", route_class=DishkaRoute)


class RegisterRequest(BaseModel):
    username: str
    password: str



class RegisterResponse(BaseModel):
    token: str | None = field(default=None)


@ROUTER.post("/")
async def register(
    payload: RegisterRequest,
    service: FromDishka[AuthService],
    rep: FromDishka[UserRepository]
) -> RegisterResponse:
        if await rep.exists(payload.username):
            raise HTTPException(
                status_code= 400,
                detail= "user with that username alredy exist")
        else:
            await rep.create(payload.username, payload.password)
            user = await rep.get_by_username(payload.username)
            user_id = user.id
            token = service.create_token(user_id, payload.username)
            return RegisterResponse(token=token)
            