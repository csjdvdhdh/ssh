hereimport os
from fastapi import FastAPI, WebSocket
import requests

app = FastAPI()

BOT_TOKEN = os.getenv("8712234813:AAElbQAXTvAk7riitnH76WeFQ_KA9gy15Us")
CHAT_ID = os.getenv("8650707600")

SSH_HOST = os.getenv("SSH_HOST")
SSH_PORT = os.getenv("SSH_PORT", "22")
SSH_USER = os.getenv("seifszx")
SSH_PASS = os.getenv("seifszxssh")

def send_to_telegram(text):
    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", data={
        "chat_id": CHAT_ID,
        "text": text
    })

@app.on_event("startup")
async def startup():
    domain = os.getenv("K_SERVICE_URL", "YOUR_DOMAIN")

    config = f"""
GET /app3 HTTP/1.1
Host: {domain}
Connection: Upgrade
Upgrade: websocket

SSH:
Host: {SSH_HOST}
Port: {SSH_PORT}
User: {SSH_USER}
Pass: {SSH_PASS}
"""
    send_to_telegram(config)

@app.websocket("/app3")
async def ws(ws: WebSocket):
    await ws.accept()
    while True:
        data = await ws.receive_text()
        await ws.send_text("ok")
