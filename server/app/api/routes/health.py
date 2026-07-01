from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "LIFE-OS",
        "version": "0.1.0"
    }