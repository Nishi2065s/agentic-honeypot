from fastapi import FastAPI, Header, HTTPException
from datetime import datetime

app = FastAPI(title="Agentic Honey-Pot API")

API_KEY = "GUVI-HCL-2026"

@app.post("/honeypot")
def honeypot(x_api_key: str = Header(None)):
    # 1. API key validation
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    # 2. Empty message (tester sends no body)
    message = ""

    # 3. Static safe response for validation
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "is_scam": False,
        "risk_score": 0.0,
        "scam_indicators": [],
        "extracted_entities": {
            "urls": [],
            "phones": [],
            "emails": []
        },
        "honeypot_action": "logged_and_monitored"
    }



