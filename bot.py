import sqlite3
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

# 1. إعداد قاعدة البيانات
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS inventory (id INTEGER PRIMARY KEY, phone TEXT)')
    conn.commit()
    conn.close()

# 2. القائمة الرئيسية
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔵 شراء رقم", callback_data='buy'), InlineKeyboardButton("🔴 رصيدي", callback_data='balance')],
        [InlineKeyboardButton("🔵 طلباتي", callback_data='orders'), InlineKeyboardButton("🔴 الإعدادات", callback_data='settings')],
        [InlineKeyboardButton("🔵 المساعدة", callback_data='help')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("👋 أهلاً بك في بوت الأرقام، اختر خياراً:", reply_markup=reply_markup)

# 3. معالج الأزرار
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == 'buy':
        await query.edit_message_text("📱 جاري البحث عن أرقام متاحة في المخزن...")
    else:
        await query.edit_message_text(f"تم اختيار: {query.data} (قيد التطوير)")

# 4. معالج رفع الملفات
async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📂 تم استلام الملف! (سأقوم ببرمجة حفظ الأرقام هنا لاحقاً).")

if name == 'main':
    init_db()
    TOKEN = "8886502478:AAFC-DJauBuaj3n-pRcfQ7qTE6sCuIfMRko"
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.add_handler(MessageHandler(filters.Document.ALL, handle_document))
    
    print("البوت جاهز ومنظم!")
    app.run_polling()
