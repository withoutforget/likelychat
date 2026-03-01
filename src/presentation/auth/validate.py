from dataclasses import dataclass, field


from dishka.integrations.fastapi import DishkaRoute, FromDishka
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

from src.application.auth.auth_service import AuthService, UserAuthModel


ROUTER = APIRouter(prefix="/validate", route_class=DishkaRoute)


class TokenRequest(BaseModel):
    token: str


class ValidateResponse(BaseModel):
    validate: bool
    msg: str


@ROUTER.get("/")
async def validate(
    token_request: TokenRequest, 
    service: FromDishka[AuthService]
) -> ValidateResponse:
    token = token_request.token
    if type(service.validate(token)) == UserAuthModel:
        return ValidateResponse(
            validate= True,
            msg= "token is valid"
        )
    else:
        return service.validate(token)
