from dataclasses import dataclass, field

from fastapi import APIRouter

ROUTER = APIRouter(prefix="/healthcheck")


@dataclass(slots=True)
class GetServiceStatusResponse:
    ok: bool
    message: str | None = field(default=None)


@ROUTER.get("/")
async def get_service_status() -> GetServiceStatusResponse:
    return GetServiceStatusResponse(ok=True)
