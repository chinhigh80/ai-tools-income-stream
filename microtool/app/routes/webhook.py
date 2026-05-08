from fastapi import APIRouter, Request, HTTPException
import os
import hmac
import hashlib
import json

router = APIRouter()

PAYSTACK_SECRET_KEY = os.getenv("PAYSTACK_SECRET_KEY", "")

@router.post("/payment")
async def paystack_webhook(request: Request):
    """
    Verify Paystack webhook signature and process successful payment.
    For demo, we just log and return 200.
    """
    body = await request.body()
    signature = request.headers.get("x-paystack-signature")
    if not signature:
        raise HTTPException(status_code=400, detail="Missing Paystack signature")
    # Compute HMAC SHA512
    computed_signature = hmac.new(
        PAYSTACK_SECRET_KEY.encode('utf-8'),
        body,
        hashlib.sha512
    ).hexdigest()
    if not hmac.compare_digest(computed_signature, signature):
        raise HTTPException(status_code=400, detail="Invalid signature")
    payload = json.loads(body)
    event = payload.get("event")
    data = payload.get("data", {})
    if event == "charge.success":
        # Successful payment - unlock download or grant access
        # For demo, we just print
        print(f"Payment successful: {data}")
        # In a real app, you would update DB, send email, etc.
    return {"status": "success"}