import telebot
from yt_dlp import YoutubeDL
import os

# ضع التوكن الخاص بك مكان النص العربي بين العلامتين ' '
API_TOKEN = '8511125466:AAHGMq4uVT86-T7yay-iRB0ImiYxpWsNDsY'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "مرحباً بك في أنظمة أثينا.\nأرسل رابط تيك توك للتحميل.")

@bot.message_handler(func=lambda message: True)
def download_video(message):
    url = message.text
    if 'tiktok.com' in url:
        bot.reply_to(message, "جاري المعالجة...")
        try:
            ydl_opts = {'outtmpl': 'video.mp4'}
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            with open('video.mp4', 'rb') as video:
                bot.send_video(message.chat.id, video)
            os.remove('video.mp4')
        except Exception as e:
            bot.reply_to(message, "حدث خطأ في التحميل.")
    else:
        bot.reply_to(message, "الرجاء إرسال رابط صحيح.")

bot.polling()
