from fastapi import APIRouter, Request

router = APIRouter(prefix="/webhooks", tags=["webhooks"])


@router.post("/meta")
async def receive_meta_webhook(request: Request) -> dict[str, str]:
    # TODO: Validate Meta signature and process inbound payloads.
    payload = await request.json()
    return {"status": "received", "payload": str(payload)[:200]}
