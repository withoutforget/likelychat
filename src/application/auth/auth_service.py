import datetime
import uuid
from dataclasses import dataclass

import jwt
from fastapi import HTTPException


@dataclass(slots=True)
class UserAuthModel:
    id: int
    username: str
    expires_at: datetime.datetime


@dataclass(slots=True)
class AuthServiceConfig:
    secret_key: str
    algorithm: str
    token_timeout: int


@dataclass(slots=True)
class AuthService:
    config: AuthServiceConfig

    def create_token(self, idx: int, username: str) -> str:
        payload = {
            "exp": int(datetime.datetime.now(tz=datetime.UTC).timestamp())
            + self.config.token_timeout,
            "sub": str(idx),
            "jti": uuid.uuid4().hex,
            "username": username,
        }

        return jwt.encode(
            payload=payload,
            key=self.config.secret_key,
            algorithm=self.config.algorithm,
        )

    def validate(self, token: str) -> UserAuthModel:
        try:
            return jwt.decode(
                token,
                self.config.secret_key,
                algorithms=[self.config.algorithm],
            )
        except jwt.ExpiredSignatureError as err:
            raise HTTPException(
                status_code=401, detail={"message": "token expired"}
            ) from err
        except jwt.InvalidTokenError as err:
            raise HTTPException(
                status_code=401, detail={"message": "token invalid"}
            ) from err
