from dataclasses import dataclass, field
from typing import Optional

from fastapi import APIRouter

ROUTER = APIRouter(
    prefix = '/healthcheck'
)

@dataclass(slots=True)
class GetServiceStatusResponse:
    ok: bool
    message: Optional[str] = field(default=None)

@ROUTER.get('/', response_model_exclude_none=True)
async def get_service_status() -> GetServiceStatusResponse:
    return GetServiceStatusResponse(ok=True)