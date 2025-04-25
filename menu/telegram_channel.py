from telegram import Update
from telegram.ext import ContextTypes

# O'zbekcha Telegram kanal
async def send_telegram_channel_uz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📢 Bizning Telegram kanalimiz:\n"
        "🔹https://t.me/TuningSalon"
    )

# Ruscha Telegram kanal
async def send_telegram_channel_ru(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📢 Наши канал в Telegram:\n"
        "🔹https://t.me/TuningSalon"
    )
