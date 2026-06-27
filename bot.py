from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import requests

TOKEN = "8886502478:AAFC-DJauBuaj3n-pRcfQ7qTE6sCuIfMRko"
API_KEY = "rarZkIqvaTxhwFXupz45siAlA661512GoaOvXe2lEpvvzlS"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📱 شراء رقم", callback_data="buy")],
        [InlineKeyboardButton("💰 الرصيد", callback_data="balance")],
        [InlineKeyboardButton("📋 طلباتي", callback_data="orders")],
        [InlineKeyboardButton("⚙️ الإعدادات", callback_data="settings")],
        [InlineKeyboardButton("ℹ️ المساعدة", callback_data="help")]
    ]

    await update.message.reply_text(
        "👋 أهلاً بك في بوت الأرقام\n\nاختر أحد الخيارات:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "buy":
        keyboard = [
            [InlineKeyboardButton("📲 Telegram", callback_data="service_tg")],
            [InlineKeyboardButton("💬 WhatsApp", callback_data="service_wa")],
            [InlineKeyboardButton("🤖 ChatGPT", callback_data="service_chatgpt")],
            [InlineKeyboardButton("🔙 رجوع", callback_data="back")]
        ]

        await query.edit_message_text(
            "📱 اختر الخدمة:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "balance":
        url = f"https://sms-activation.net/stubs/handler_api.php?api_key={API_KEY}&action=getBalance"
        r = requests.get(url)
        await query.edit_message_text(f"💰 رصيد الموقع:\n\n{r.text}")

    elif query.data == "orders":
        await query.edit_message_text("📋 لا توجد طلبات حالياً.")

    elif query.data == "settings":
        await query.edit_message_text("⚙️ الإعدادات قريباً.")

    elif query.data == "help":
        await query.edit_message_text("ℹ️ المساعدة قريباً.")

    elif query.data == "service_tg":
        await query.edit_message_text("📲 قريباً شراء رقم Telegram")

    elif query.data == "service_wa":
        await query.edit_message_text("💬 قريباً شراء رقم WhatsApp")

    elif query.data == "service_chatgpt":
        await query.edit_message_text("🤖 قريباً شراء رقم ChatGPT")

    elif query.data == "back":
        keyboard = [
            [InlineKeyboardButton("📱 شراء رقم", callback_data="buy")],
            [InlineKeyboardButton("💰 الرصيد", callback_data="balance")],
            [InlineKeyboardButton("📋 طلباتي", callback_data="orders")],
            [InlineKeyboardButton("⚙️ الإعدادات", callback_data="settings")],
            [InlineKeyboardButton("ℹ️ المساعدة", callback_data="help")]
        ]

        await query.edit_message_text(
            "👋 أهلاً بك في بوت الأرقام\n\nاختر أحد الخيارات:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(buttons))

print("Bot is running...")

app.run_polling()
