from telegram import Update
from telegram.ext import ContextTypes

# O'zbekcha Telefon raqam
async def send_phone_uz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📞 Telefon raqamlarimiz:\n"
        "🔹 +998 88 366 90 90\n"
        "🔹 +998 97 404 99 29\n"
        "🔹 +998 33 555 90 90\n"
        "🔹 +998 88 124 33 55"
    )

# Ruscha Telefon raqam
async def send_phone_ru(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📞 Наши телефонные номера:\n"
        "🔹 +998 88 366 90 90\n"
        "🔹 +998 97 404 99 29\n"
        "🔹 +998 33 555 90 90\n"
        "🔹 +998 88 124 33 55"
    )

