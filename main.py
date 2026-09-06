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
    evento: str = Field(...,The visible file structure shows a repetitive directory nesting issue: **`services/services/services/main.py`**.

In `main.py`, lines 5–6 attempt to import modules using `from services.telegram` and `from services.email`. Because Python looks for a top-level `services` directory relative to the project root or the Python path, these imports will raise a `ModuleNotFoundError` when executing `main.py`.

**Solutions**

* **Fix the directory tree:** Move `main.py` up to `services/main.py` so that subfolders like `services/telegram.py` (or `services/telegram/`) sit at the same level relative to it.
* **Fix the imports:** If `main.py` is intended to stay inside the `services/` directory alongside `telegram.py` and `email.py`, change the imports to relative or sibling paths:
  ```python
  from telegram import enviar_mensagem_telegram
  from email_notificacao import enviar_email_notificacao  # or from .telegram / .email
