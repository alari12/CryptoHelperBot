# main.py
from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# =========================
# CONFIG
# =========================
TOKEN = "YOUR_BOT_TOKEN"  # Replace with your Telegram bot token

# Define links for different issues
LINKS = {
    "wallet": "https://example.com/wallet",
    "usdt": "https://example.com/usdt",
    "transfer failed": "https://example.com/transfer"
}

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

    # Check for keywords and send the proper link
    for keyword, link in LINKS.items():
        if keyword in text:
            update.message.reply_text(
                f"I see you have a {keyword} issue.\n\n"
                f"Step-by-step instructions are here: [Click Here]({link})",
                parse_mode=ParseMode.MARKDOWN
            )
            return

    # Default reply
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
