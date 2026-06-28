from telegram.ext import ApplicationBuilder, CommandHandler

async def start(update, context):
    await update.message.reply_text("البوت يعمل الآن ومستعد لاستقبال أوامرك!")

if name == 'main':
    # التوكن الخاص بك
    TOKEN = "8886502478:AAFC-DJauBuaj3n-pRcfQ7qTE6sCuIfMRko"
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("البوت بدأ العمل")
    app.run_polling()
