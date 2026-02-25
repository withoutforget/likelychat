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

    def create_token(self, idx: uuid.UUID, username: str) -> str:
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
            tmp_decode_data = jwt.decode(
                token,
                self.config.secret_key,
                algorithms=[self.config.algorithm],
            )

            return UserAuthModel(
                id= tmp_decode_data["sub"],
                username= tmp_decode_data["username"],
                expires_at= tmp_decode_data["exp"]
            )
        
        except jwt.ExpiredSignatureError as err:
            raise HTTPException(
                status_code=401, detail={"message": "token expired"}
            ) from err
        except jwt.InvalidTokenError as err:
            raise HTTPException(
                status_code=401, detail={"message": "token invalid"}
            ) from err
