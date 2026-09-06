import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_email_notificacao(assunto: str, mensagem_corpo: str) -> bool:
    smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
    smtp_port = int(os.getenv("SMTP_PORT", 587))
    remetente = os.getenv("EMAIL_REMETENTE")
    senha = os.getenv("EMAIL_SENHA")
    destinatario = os.getenv("EMAIL_DESTINATARIO")
    
    if not remetente or not senha or not destinatario:
        print("[Aviso] Credenciais de e-mail não configuradas no arquivo .env")
        return False
        
    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = assunto
    
    msg.attach(MIMEText(mensagem_corpo, 'plain'))
    
    try:
        servidor = smtplib.SMTP(smtp_server, smtp_port)
        servidor.starttls()
        servidor.login(remetente, senha)
        servidor.send_message(msg)
        servidor.quit()
        return True
    except Exception as erro:
        print(f"Erro ao enviar e-mail: {erro}")
        return False
