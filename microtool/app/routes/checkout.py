from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import os
import json
import hashlib
import hmac
import time

router = APIRouter()

PAYSTACK_SECRET_KEY = os.getenv("PAYSTACK_SECRET_KEY", "")
PAYSTACK_PUBLIC_KEY = os.getenv("PAYSTACK_PUBLIC_KEY", "")

class CheckoutRequest(BaseModel):
    email: str
    amount: int  # in kobo (lowest currency unit)
    metadata: dict = {}

@router.post("/session")
def create_checkout_session(request: CheckoutRequest):
    """
    Create a Paystack transaction (returns authorization URL).
    In test mode, use Paystack test keys.
    """
    if not PAYSTACK_SECRET_KEY:
        raise HTTPException(status_code=500, detail="Paystack secret key not configured")
    # For simplicity, we simulate a Paystack transaction initialization.
    # In real integration, you would POST to https://api.paystack.co/transaction/initialize
    # Here we just return a mock URL.
    # NOTE: Replace with actual Paystack API call in production.
    tx_ref = f"ai-tools-{int(time.time())}"
    # Mock response
    return {
        "status": True,
        "message": "Checkout URL generated (mock)",
        "data": {
            "authorization_url": f"https://checkout.paystack.com/{tx_ref}",
            "access_code": tx_ref,
            "reference": tx_ref
        }
    }
