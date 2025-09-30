# main.py
from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# =========================
# CONFIG
# =========================
TOKEN = "8256075938:AAGelvhEM-0DnLCiGeJld49jc_8NWD3bTDU"  # Replace with your Telegram bot token
HELP_LINK = "https://help.coinbase.com/en/wallet"  # Replace with your help link

# =========================
# START COMMAND
# =========================
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Hello! I am CryptoHelperBot 🤖\n\n"
        "I help you troubleshoot your crypto wallet issues.\n"
        "Send me a message mentioning your problem, like 'wallet', 'USDT', or 'transfer failed',\n"
        "and I will give you step-by-step instructions.\n\n"
        "⚠️ Disclaimer:\n"
        "This bot is for guidance only. It does NOT access your private keys or funds."
    )

# =========================
# HELP COMMAND
# =========================
def help_command(update: Update, context: CallbackContext):
    update.message.reply_text(
        "CryptoHelperBot Help ⚙️\n\n"
        "Send a message mentioning your crypto wallet issue (wallet, USDT, transfer failed).\n"
        "You will receive step-by-step instructions with a clickable link.\n\n"
        "⚠️ Disclaimer:\n"
        "This bot is for guidance only. It does NOT access your private keys or funds."
    )

# =========================
# HANDLE MESSAGES
# =========================
def handle_message(update: Update, context: CallbackContext):
    text = update.message.text.lower()

    if "wallet" in text or "crypto" in text or "usdt" in text or "transfer failed" in text:
        update.message.reply_text(
            f"I see you have a crypto wallet issue. 🛠️\n\n"
            f"Step-by-step instructions are here: [Click Here]({HELP_LINK})",
            parse_mode=ParseMode.MARKDOWN
        )
    else:
        update.message.reply_text(
            "Sorry, I only handle crypto wallet issues. ❌\n"
            "Try using words like 'wallet', 'USDT', or 'transfer failed'."
        )

# =========================
# RUN THE BOT
# =========================
def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    print("Bot is running...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
