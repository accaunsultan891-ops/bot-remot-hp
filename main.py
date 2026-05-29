import os
import telebot
from flask import Flask

# Mengambil Token dari pengaturan Render (aman & rahasia)
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot Telegram Aktif!"

# Balasan saat mengetik /start atau /help di Telegram
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Halo! Bot kamu berhasil aktif 24 jam lewat Render.")

# Balasan otomatis yang meniru teks kamu (echo)
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Kamu mengirim pesan: {message.text}")

if __name__ == "__main__":
    import threading
    threading.Thread(target=bot.infinity_polling).start()
    
    # Menjalankan server agar Render tidak mendeteksi bot mati
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
  
