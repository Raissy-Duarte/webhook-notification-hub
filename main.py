import os
import sys
from fastapi import FastAPI, Header, HTTPException, Depends
from pydantic import BaseModel
from dotenv import load_dotenv

# Adiciona o diretório atual ao PATH para garantir a importação do pacote services
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from services.telegram import send_telegram_message
from services.email import send_email_notification

load_dotenv()

app = FastAPI(title="Webhook Notification Hub")

WEBHOOK_SECRET_TOKEN = os.getenv("WEBHOOK_SECRET_TOKEN")

class NotificationPayload(BaseModel):
    title: str
    message: str

def verify_token(x_webhook_token: str = Header(...)):
    if x_webhook_token != WEBHOOK_SECRET_TOKEN:
        raise HTTPException(status_code=401, detail="Token invalido")
    return x_webhook_token

@app.get("/")
def read_root():
    return {"message": "API de Notificacoes ativa!"}

@app.post("/webhook/notificar")
def receive_webhook(payload: NotificationPayload, token: str = Depends(verify_token)):
    telegram_sent = send_telegram_message(payload.title, payload.message)
    email_sent = send_email_notification(payload.title, payload.message)
    
    return {
        "status": "sucesso",
        "telegram_enviado": telegram_sent,
        "email_enviado": email_sent
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
