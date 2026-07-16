from fastapi import APIRouter

router = APIRouter(tags=["root"])


@router.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Instagram Automation Assistant API"}
