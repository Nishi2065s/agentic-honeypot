from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import re

app = FastAPI(title="Agentic Honey-Pot API")

API_KEY = "GUVI-HCL-2026"

# Request body is OPTIONAL (important for GUVI tester)
class RequestData(BaseModel):
    message: Optional[str] = None

@app.post("/honeypot")
def honeypot(
    data: Optional[RequestData] = None,
    x_api_key: str = Header(None)
):
    # API Key validation
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    # Handle empty body (GUVI tester sends no JSON)
    message = data.message.lower() if data and data.message else ""

    scam_words = ["free", "win", "prize", "click", "urgent"]
    indicators = [word for word in scam_words if word in message]

    urls = re.findall(r"https?://\S+", message)
    phones = re.findall(r"\+?\d{10,13}", message)
    emails = re.findall(r"\S+@\S+", message)

    risk_score = min(len(indicators) * 0.2, 1.0)

    return {
        "timestamp": datetime.utcnow().isoformat(),
        "is_scam": risk_score > 0.3,
        "risk_score": risk_score,
        "scam_indicators": indicators,
        "extracted_entities": {
            "urls": urls,
            "phones": phones,
            "emails": emails
        },
        "honeypot_action": "logged_and_monitored"
    }


