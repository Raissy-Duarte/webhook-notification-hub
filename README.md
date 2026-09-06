# Hub de Notificações Multicanais via Webhook

API assíncrona para recepção de webhooks e disparo automatizado de alertas para múltiplos canais de comunicação, incluindo Telegram e e-mail.

---

## Sumário

* [Visão Geral](#visão-geral)
* [Tecnologias Utilizadas](#tecnologias-utilizadas)
* [Arquitetura e Estrutura](#arquitetura-e-estrutura)
* [Configuração e Instalação](#configuração-e-instalação)
* [Documentação da API](#documentação-da-api)

---

## Visão Geral

O projeto consiste em um microsserviço desenvolvido com FastAPI para centralizar o recebimento de notificações originadas de eventos externos (como confirmações de pagamento, status de pedidos e alertas de sistema). Ao receber a requisição, a aplicação valida a autenticidade da chamada via token e encaminha os alertas de forma simultânea.

---

## Tecnologias Utilizadas

* **Linguagem:** Python 3.10+
* **Framework Web:** FastAPI
* **Servidor ASGI:** Uvicorn
* **Validação de Dados:** Pydantic
* **Requisições HTTP:** Requests
* **Gerenciamento de Variáveis:** Python-Dotenv

---

## Arquitetura e Estrutura

```text
webhook-notification-hub/
├── main.py              # Inicialização e endpoints da API
├── requirements.txt     # Dependências do projeto
├── .env.example         # Modelo de variáveis de ambiente
└── services/
    ├── __init__.py
    ├── telegram.py      # Módulo de integração com a API do Telegram
    └── email.py         # Módulo de envio de e-mails via SMTP
