import sqlite3
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS inventory (id INTEGER PRIMARY KEY, phone TEXT)')
    conn.commit()
    conn.close()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("البوت يعمل الآن بدون أخطاء!")

async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("تم استلام الملف")

# هنا استخدمنا طريقة بديلة للتشغيل لا تحتاج للشرطات
init_db()
TOKEN = "8886502478:AAFC-DJauBuaj3n-pRcfQ7qTE6sCuIfMRko"
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.Document.ALL, handle_document))

print("البوت جاهز ومنظم!")
app.run_polling()
