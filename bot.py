from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # ترتيب الأزرار بالعرض (زرين في كل سطر) مع أيقونات ملونة
    keyboard = [
        [
            InlineKeyboardButton("🔵 شراء رقم", callback_data='buy'), 
            InlineKeyboardButton("🔴 الرصيد", callback_data='balance')
        ],
        [
            InlineKeyboardButton("🔵 طلباتي", callback_data='orders'), 
            InlineKeyboardButton("🔴 الإعدادات", callback_data='settings')
        ],
        [
            InlineKeyboardButton("🔵 المساعدة", callback_data='help')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("👋 أهلاً بك في بوت الأرقام، اختر خياراً:", reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(f"تم اختيار: {query.data}")

if name == 'main':
    TOKEN = "8886502478:AAFC-DJauBuaj3n-pRcfQ7qTE6sCuIfMRko"
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.run_polling()
