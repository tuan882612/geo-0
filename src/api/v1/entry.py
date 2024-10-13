from fastapi import APIRouter

_router = APIRouter(prefix="/v1")


def new_v1_router() -> APIRouter:
    return _router


@_router.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}
