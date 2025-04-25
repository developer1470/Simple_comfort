from telegram import Update
from telegram.ext import ContextTypes

async def send_instagram_uz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
    "📸 <b>Instagram sahifalarimiz:</b>\n"
    "🔹 <a href='https://instagram.com/comfort_uzb.uz'>comfort_uzb.uz</a>\n"
    "🔹 <a href='https://instagram.com/comfort_sidenya'>comfort_sidenya</a>\n"
    "🔹 <a href='https://instagram.com/comfort_drive.uz'>comfort_drive.uz</a>\n"
    "🔹 <a href='https://instagram.com/sidenya_optom'>sidenya_optom</a>",
    parse_mode='HTML'
)


async def send_instagram_ru(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
    "📸 Наши страницы в Instagram:\n"
    "🔹 <a href='https://instagram.com/comfort_uzb.uz'>comfort_uzb.uz</a>\n"
    "🔹 <a href='https://instagram.com/comfort_sidenya'>comfort_sidenya</a>\n"
    "🔹 <a href='https://instagram.com/comfort_drive.uz'>comfort_drive.uz</a>\n"
    "🔹 <a href='https://instagram.com/sidenya_optom'>sidenya_optom</a>",
    parse_mode='HTML'
    )