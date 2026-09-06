import os
from fastapi import FastAPI, HTTPException, Header, Depends
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from services.telegram import enviar_mensagem_telegram
from services.email import enviar_email_notificacao

load_dotenv()

app = FastAPI(
    title="Hub de notificações multicanais",
    description="API para recepção de webhooks e disparo de alertas automáticos."
)

TOKEN_SECRETO = os.getenv("WEBHOOK_SECRET_TOKEN", "meutokenseguro123")

class PayloadNotificacao(BaseModel):
    evento: str = Field(..., example="pagamento_aprovado")
    cliente: str = Field(..., example="Maria Silva")
    valor: float = Field(..., example=149.90)
    mensagem: str = Field(..., example="Pagamento confirmado com sucesso.")

def verificar_token(x_webhook_token: str = Header(...)):
    if x_webhook_token != TOKEN_SECRETO:
        raise HTTPException(status_code=401, detail="Token de autorização inválido.")

@app.post("/webhook/notificar", status_code=200)
async def receber_webhook(payload: PayloadNotificacao, autorizado: None = Depends(verificar_token)):
    texto_notificacao = (
        f"🚨 *Novo Evento Registrado*\n\n"
        f"• *Evento:* {payload.evento}\n"
        f"• *Cliente:* {payload.cliente}\n"
        f"• *Valor:* R$ {payload.valor:.2f}\n"
        f"• *Detalhes:* {payload.mensagem}"
    )
    
    sucesso_telegram = enviar_mensagem_telegram(texto_notificacao)
    assunto_email = f"Notificação de evento: {payload.evento}"
    sucesso_email = enviar_email_notificacao(assunto_email, texto_notificacao)
    
    return {
        "status": "sucesso",
        "envios": {
            "telegram": sucesso_telegram,
            "email": sucesso_email
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
