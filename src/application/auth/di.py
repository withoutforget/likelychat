from dishka import Provider, Scope, provide
from fastapi import HTTPException, Request

from src.application.auth.auth_service import AuthService, UserAuthModel
from src.config import Config


class AuthServiceProvider(Provider):
    @provide(scope=Scope.APP)
    def provide_auth_service(self, config: Config) -> AuthService:
        return AuthService(config=config.auth)

    @provide(scope=Scope.REQUEST)
    def provide_user_auth_model(
        self, service: AuthService, request: Request
    ) -> UserAuthModel:
        headers = request.headers
        try:
            token = headers["token"]
        except KeyError as err:
            raise HTTPException(
                status_code=401, detail={"message": "token must be provded"}
            ) from err
        return service.validate(token)  # move token name to cfg?
