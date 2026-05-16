import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler

async def status(update, context):
    await update.message.reply_text("Aegant-AI: النظام يعمل بكفاءة. جميع الوكلاء في حالة نشطة.")

if __name__ == "__main__":
    app = ApplicationBuilder().token("YOUR_TOKEN_HERE").build()
    app.add_handler(CommandHandler("status", status))
    print("Aegant-AI Telegram Core: Online")
    app.run_polling()
