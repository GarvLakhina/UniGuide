from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from handlers import handle_query, handle_image, handle_voice
from config.config import BOT_TOKEN

async def start(update, context):
    await update.message.reply_text("Hi! I'm UniGuide, your student assistant. How can I help you today?")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_query))
    app.add_handler(MessageHandler(filters.PHOTO, handle_image))
    app.add_handler(MessageHandler(filters.VOICE, handle_voice))
    
    app.run_polling()
