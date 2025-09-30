# main.py
from telegram import Update
from telegram.constants import ParseMode   # Updated for newer versions
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# =========================
# CONFIG VARIABLES
# =========================
TOKEN = "8256075938:AAGelvhEM-0DnLCiGeJld49jc_8NWD3bTDU"      # Replace with your BotFather token
HELP_LINK = "https://help.coinbase.com/en/wallet"  # Replace with your help link

# =========================
# START COMMAND
# =========================
def start(update: Update, context: CallbackContext):
    """
    Sends a welcome message when the user sends /start
    Internal variables used: update, context
    """
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
    """
    Sends instructions and disclaimer when the user sends /help
    Internal variables used: update, context
    """
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
    """
    Checks the user message for keywords and replies with help link
    Internal variables used: update, context, text
    """
    text = update.message.text.lower()  # INTERNAL VARIABLE

    # Check for wallet-related keywords
    if "wallet" in text or "crypto" in text or "usdt" in text or "transfer failed" in text:
        update.message.reply_text(
            f"I see you have a crypto wallet issue. 🛠️\n\n"
            f"Step-by-step instructions are here: [Click Here]({HELP_LINK})",
            parse_mode=ParseMode.MARKDOWN
        )
    else:
        # Fallback for unrelated messages
        update.message.reply_text(
            "Sorry, I only handle crypto wallet issues. ❌\n"
            "Try using words like 'wallet', 'USDT', or 'transfer failed'."
        )

# =========================
# RUN THE BOT
# =========================
def main():
    """
    Initializes and runs the bot
    Internal variables used: updater, dp
    """
    updater = Updater(TOKEN)       # INTERNAL VARIABLE
    dp = updater.dispatcher         # INTERNAL VARIABLE

    # Register command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    # Register message handler
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    print("Bot is running...")
    updater.start_polling()
    updater.idle()

# Entry point
if __name__ == "__main__":
    main()
