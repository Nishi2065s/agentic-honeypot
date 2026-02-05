# Agentic Honey-Pot API

This project is built for the **GUVI–HCL Hackathon 2026**.

It is an **Agentic Honey-Pot API** that detects scam messages, extracts useful intelligence, and logs suspicious activity.

---

## 🚀 Features
- API key–based authentication
- Scam message detection
- Risk scoring
- Scam indicators extraction
- URL, phone, and email extraction
- Honeypot logging behavior

---

## 🛠 Tech Stack
- Python
- FastAPI
- Uvicorn

---

## 🔐 Authentication
All requests must include the API key in headers:

x-api-key: GUVI-HCL-2026
---
## 📡 API Endpoint

POST /honeypot

Request Body:
```json
{
  "message": "Congratulations! You won a free prize. Click http://scam.com"
}

So it becomes:
```markdown
```json
{
  "message": "Congratulations! You won a free prize. Click http://scam.com"
}

