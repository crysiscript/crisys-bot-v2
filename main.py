import os
from telegram import Bot
from keep_alive import keep_alive

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_USERNAME = os.getenv("CHANNEL_USERNAME")
MIN_USD = int(os.getenv("MIN_USD", 5000))

bot = Bot(token=BOT_TOKEN)

def start_bot():
    print("Bot iniciado...")
    print(f"Enviando alertas a: {CHANNEL_USERNAME}")
    # Aquí iría tu lógica de trading con gráficos/RSI

if __name__ == "__main__":
    keep_alive()
    start_bot()