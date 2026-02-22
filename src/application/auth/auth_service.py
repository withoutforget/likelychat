import datetime
from dataclasses import dataclass

import jwt


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

    def validate(self, token: str) -> UserAuthModel:
        try:
            return jwt.decode(token,
                              self.config.secret_key,
                              algorithms=[self.config.algorithm])
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None
