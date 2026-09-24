from fastapi import APIRouter

router = APIRouter(tags=["health"])


@router.get("/health/live")
async def health_live():
    return {"status": "ok"}