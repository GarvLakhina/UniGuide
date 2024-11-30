from telegram import Update
from telegram.ext import ContextTypes
from bot.nlp import process_input, share_resources

async def handle_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text.lower()

    # Check if the query is asking for resources
    if "resources" in query:
        topic = query.replace("resources", "").strip()
        response = share_resources(topic)
    else:
        # Otherwise, process it as a regular query (FAQ or general question)
        response = process_input(query)

    await update.message.reply_text(response)

async def handle_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo_file = await update.message.photo[-1].get_file()
    file_path = await photo_file.download()
    # For now, you can modify this to process the image as needed.
    await update.message.reply_text(f"Image received at {file_path}")
