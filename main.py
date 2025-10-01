import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

# -----------------------------
# Variables (from Railway)
# -----------------------------
BOT_TOKEN = os.getenv("8256075938:AAGelvhEM-0DnLCiGeJld49jc_8NWD3bTDU")
OWNER_ID = os.getenv("OWNER_ID", "5252571392")   # Replace with your Telegram user ID
ASSIST_LINK = os.getenv("ASSIST_LINK", "https://alari12.github.io/MindCarePLC/")  # Replace with your real link

# -----------------------------
# Commands
# -----------------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hello! I’m here to assist you. Type /help to see what I can do.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📌 Available commands:\n"
        "/start - Start the bot\n"
        "/help - Show this message\n"
        "/link - Get your special link"
    )

async def link_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"🔗 Here’s your assistance link:\n{ASSIST_LINK}")

# -----------------------------
# Group Message Handler
# -----------------------------
async def group_listener(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    # trigger words
    triggers = ["help", "support", "problem", "issue", "link"]

    if any(word in text for word in triggers):
        try:
            # message the user privately
            await context.bot.send_message(
                chat_id=update.message.from_user.id,
                text=f"👋 Hi {update.message.from_user.first_name},\nI noticed you need help.\nHere’s your special link:\n{https://alari12.github.io/MindCarePLC/}"
            )
        except:
            await update.message.reply_text("⚠️ Please start a private chat with me first by clicking on my name.")

# -----------------------------
# Main Function
# -----------------------------
def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("link", link_command))

    # Group trigger listener
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), group_listener))

    print("✅ Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
