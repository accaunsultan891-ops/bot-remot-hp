import telebot
import os
from flask import Flask, request

# Mengambil token dari Environment Variables Render
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

# Respon untuk perintah /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Halo! Bot kamu berhasil aktif 24 jam lewat Render.")

# Respon untuk perintah /lock
@bot.message_handler(commands=['lock'])
def ask_lock(message):
    bot.reply_to(message, "Perintah kunci layar diterima! Menghubungkan ke Termux HP...")

# Respon untuk perintah /foto
@bot.message_handler(commands=['foto'])
def ask_photo(message):
    bot.reply_to(message, "Perintah ambil foto diterima! Membuka kamera depan...")

@app.route('/' + BOT_TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://' + request.host + '/' + BOT_TOKEN)
    return "Bot Remote HP is Running!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
    
