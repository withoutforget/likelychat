from dishka import Provider, Scope, from_context, provide
from fastapi import HTTPException, Request

from src.application.auth.auth_service import AuthService, UserAuthModel
from src.config import Config


class AuthServiceProvider(Provider):
    request = from_context(provides=Request, scope=Scope.REQUEST)

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
        except KeyError:
            raise HTTPException(status_code=401, detail = {"message": "token must be provded"})
        return service.validate(token)  # move token name to cfg?

