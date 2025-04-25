from telegram import Update
from telegram.ext import ContextTypes

# O'zbekcha Telefon raqam
async def send_narxlar_uz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "\n"
        "🔹100$ dan 3000$ gacha istalgan avtomobilga sidenya topishingiz mumkin\n"
    )

# Ruscha Telefon raqam
async def send_narxlar_ru(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "\n"
        "Вы можете найти сиденья для любого автомобиля стоимостью от 100 до 3000 долларов.\n"
    )