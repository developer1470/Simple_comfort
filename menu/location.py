from telegram import Update
from telegram.ext import ContextTypes

# O'zbekcha Lokatsiya
async def send_location_uz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📍 Bizning joylashuvimiz:")
    await update.message.reply_location(latitude=41.270512, longitude=69.187479)

# Ruscha Lokatsiya
async def send_location_ru(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📍 Наша локация:")
    await update.message.reply_location(latitude=41.270512, longitude=69.187479)
