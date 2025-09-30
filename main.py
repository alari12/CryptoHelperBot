# main.py
from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# =========================
# CONFIG
# =========================
TOKEN = "YOUR_BOT_TOKEN"  # Replace with your Telegram bot token
HELP_LINK = "https://example.com"  # Replace with your single link

# =========================
# START COMMAND
# =========================
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Hello! I am CryptoHelperBot.\n"
        "Send me your crypto wallet issue, and I will guide you step by step."
    )

# =========================
# HANDLE MESSAGES
# =========================
def handle_message(update: Update, context: CallbackContext):
    text = update.message.text.lower()

    # Check for wallet-related keywords
    if "wallet" in text or "crypto" in text or "usdt" in text or "transfer failed" in text:
        update.message.reply_text(
            f"I see you have a crypto wallet issue.\n\n"
            f"Step-by-step instructions are here: [Click Here]({HELP_LINK})",
            parse_mode=ParseMode.MARKDOWN
        )
    else:
        update.message.reply_text(
            "Sorry, I only handle crypto wallet issues.\n"
            "Try using words like 'wallet', 'USDT', or 'transfer failed'."
        )

# =========================
# RUN THE BOT
# =========================
def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    print("Bot is running...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
