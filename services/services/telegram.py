import os
import requests

def enviar_mensagem_telegram(texto: str) -> bool:
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    
    if not bot_token or not chat_id:
        print("[Aviso] Credenciais do Telegram não configuradas no arquivo .env")
        return False
        
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": texto,
        "parse_mode": "Markdown"
    }
    
    try:
        resposta = requests.post(url, json=payload, timeout=10)
        return resposta.status_code == 200
    except Exception as erro:
        print(f"Erro ao enviar mensagem para o Telegram: {erro}")
        return False
