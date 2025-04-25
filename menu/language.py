from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ContextTypes

# Til tanlashdagi menyu
uzbek_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("📍 Lokatsiya"), KeyboardButton("📸 Instagram")],
        [KeyboardButton("📞 Telefon"), KeyboardButton("📢 Telegram kanal")],
        [KeyboardButton("🔙 Orqaga")],
    ],
    resize_keyboard=True
)

russian_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("📍 Локация"), KeyboardButton("📸 Инстаграм")],
        [KeyboardButton("📞 Телефон"), KeyboardButton("📢 Телеграм канал")],
        [KeyboardButton("🔙 Назад")],
    ],
    resize_keyboard=True
)

# Tilni tanlash logikasi
async def handle_language(update: Update, context: ContextTypes.DEFAULT_TYPE, lang_text: str):
    if lang_text == "🇺🇿 O'zbek":
        context.user_data["lang"] = "uz"
        await update.message.reply_text("✅ Siz o'zbek tilini tanladingiz.\n\n Kerakli bo‘limni tanlang 👇", reply_markup=uzbek_menu)

    elif lang_text == "🇷🇺 Русский":
        context.user_data["lang"] = "ru"
        await update.message.reply_text("✅ Вы выбрали русский язык.\n\n Выберите нужный раздел 👇", reply_markup=russian_menu)
