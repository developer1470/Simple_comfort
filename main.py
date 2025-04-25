from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from bot_token import TOKEN
from telegram import ReplyKeyboardMarkup, KeyboardButton
from menu.location import send_location_ru,send_location_uz
from menu.instagram import send_instagram_ru, send_instagram_uz
from menu.phone import send_phone_ru, send_phone_uz
from menu.telegram_channel import send_telegram_channel_ru, send_telegram_channel_uz
from menu.you_tube import send_youtube_channel_uz, send_youtube_channel_ru
from menu.narxlar import send_narxlar_ru, send_narxlar_uz

# Til tanlash menyusi
language_menu = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton("🇺🇿 O'zbek"), KeyboardButton("🇷🇺 Русский")]],
    resize_keyboard=True,
    one_time_keyboard=True
)

# O'zbekcha menyu
uzbek_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("📍 Lokatsiya"), KeyboardButton("📸 Instagram")],
        [KeyboardButton("📞 Telefon"), KeyboardButton("📢 Telegram kanal")],
        [KeyboardButton("📺You Tube"), KeyboardButton("💰 Narxlar")],
        [KeyboardButton("🔙 Orqaga")],
    ],
    resize_keyboard=True
)

# Ruscha menyu
russian_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("📍 Локация"), KeyboardButton("📸 Инстаграм")],
        [KeyboardButton("📞 Телефон"), KeyboardButton("📢 Телеграм канал")],
        [KeyboardButton("📺 Ютуб"), KeyboardButton("💰 Цены")],
        [KeyboardButton("🔙 Назад")],
    ],
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🌐 Iltimos, tilni tanlang: \n Пожалуйста, выберите язык:", reply_markup=language_menu)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    lang = context.user_data.get("lang", "uz")

    if text == "🇺🇿 O'zbek":
        context.user_data["lang"] = "uz"
        await update.message.reply_text("✅ Siz o'zbek tilini tanladingiz.\n\nKerakli bo‘limni tanlang 👇", reply_markup=uzbek_menu)

    elif text == "🇷🇺 Русский":
        context.user_data["lang"] = "ru"
        await update.message.reply_text("✅ Вы выбрали русский язык.\n\nВыберите нужный раздел 👇", reply_markup=russian_menu)

    elif text == "📍 Lokatsiya" or text == "📍 Локация":
        if lang == "uz":
            await send_location_uz(update, context)
        else:
            await send_location_ru(update, context)
    
    elif text == "📸 Instagram" or text == "📸 Инстаграм":
        if lang == "uz":
            await send_instagram_uz(update, context)
        else:
            await send_instagram_ru(update, context)

    elif text == "📞 Telefon" or text == "📞 Телефон":
        if lang == "uz":
            await send_phone_uz(update, context)
        else:
            await send_phone_ru(update, context)

    elif text == "📢 Telegram kanal" or text == "📢 Телеграм канал":
        if lang == "uz":
            await send_telegram_channel_uz(update, context)
        else:
            await send_telegram_channel_ru(update, context)

    elif "📺" in text and ("You" in text or "Ютуб" in text):
        if lang == "uz":
            await send_youtube_channel_uz(update, context)
        else:
            await send_youtube_channel_ru(update, context)

    elif text in ["💰 Narxlar", "💰 Цены"]:
        if lang == "uz":
            await send_narxlar_uz(update, context)
        else:
            
            await send_narxlar_ru(update, context)



    elif text in ["🔙 Orqaga", "🔙 Назад"]:
        await update.message.reply_text("⬅️ Tilni tanlang:\n Выберите язык", reply_markup=language_menu)

    else:
        if lang == "uz":
            await update.message.reply_text("Iltimos, menyudan tanlang.")
        else:
            await update.message.reply_text("Пожалуйста, выберите из меню.")



if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
















































# from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler
# from bot_token import TOKEN


# async def start(update: Update, context_type: ContextTypes.DEFAULT_TYPE):
#     keyboard = [
#         [
#         InlineKeyboardButton("Uz", callback_data="lang_uz"),
#         InlineKeyboardButton("Ru", callback_data="lang_ru"),
#         ]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)

#     await update.message.reply_text("Tilni tanlang !", reply_markup=reply_markup)

# async def language_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     query = update.callback_query
#     await query.answer()

#     if query.data == "lang_uz":
#         await query.edit_message_text("O'zbek tili.")
#     elif query.data == "lang_ru":
#         await query.edit_message_text("русский язык.")


# if __name__ == '__main__':
#     app = ApplicationBuilder().token(TOKEN).build()

#     app.add_handler(CommandHandler('start', start))
#     app.add_handler(CallbackQueryHandler(language_callback))

#     app.run_polling()














































# """Start command"""
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     """Lokatsiya jo'natish"""
#     await update.message.reply_text("📍Lokatsiyamiz :")
#     await update.message.reply_location(latitude=41.271279, longitude=69.187996)
#     text = (
#         "👋 Assalomu alekum Comfort Uzb rasmiy bo'tiga xush kelibsiz !\n\n"

#         "📸 Instagram: [Comfort_uzb.uz](https://instagram.com/comfort_uzb.uz)\n"
#         "📸 Instagram: [Comfort_sidenya](https://instagram.com/comfort_sindenya)\n"
#         "📸 Instagram: [Sidenya_optom](https://instagram.com/sidenya_optom)\n"
#         "📞 Telefon: +998 88 366 90 90\n"
#         "📞 Telefon: +998 33 555 90 90\n"
#         "📱 Telegram kanallar: [Telegram kanal](https://t.me/TuningSalon)\n"
#     )

#     await update.message.reply_text(text, parse_mode="Markdown")

# if __name__ == '__main__':
#     app = ApplicationBuilder().token(TOKEN).build()
#     app.add_handler(CommandHandler("start", start))
#     app.run_polling()