from telegram import Update
from telegram.ext import ContextTypes

# O'zbekcha kanalni yuborish funksiyasi
async def send_youtube_channel_uz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📺 <b>YouTube kanalimiz:</b>\n"
        "▶️ <a href='https://youtube.com/@tuning_salon'>YouTube'da bizni kuzating!</a>",
        parse_mode='HTML'
    )

# Ruscha kanalni yuborish funksiyasi
async def send_youtube_channel_ru(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📺 <b>Наш YouTube канал:</b>\n"
        "▶️ <a href='https://youtube.com/@tuning_salon'>Следите за нами на YouTube!</a>",
        parse_mode='HTML'
    )
