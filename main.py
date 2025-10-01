# main.py
from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# =========================
# CONFIG VARIABLES
# =========================
TOKEN = "8256075938:AAGelvhEM-0DnLCiGeJld49jc_8NWD3bTDU"       # 🔴 Replace this with your BotFather token
HELP_LINK = "https://alari12.github.io/MindCarePLC/"  # 🔴 Replace this with your help link

# =========================
# START COMMAND
# =========================
def start(update: Update, context: CallbackContext):
    """Reply when a user types /start"""
    update.message.reply_text(
        "👋 Hello! I’m CryptoHelperBot.\n\n"
        "I help with wallet issues.
    )

# =========================
# HELP COMMAND
# =========================
def help_command(update: Update, context: CallbackContext):
    update.message.reply_text(
        "📌 How to use me:\n"
        "- Add me to a group.\n"
        "- Say 'wallet', 'crypto', 'USDT', or 'transfer failed'.\n"
        "- I’ll DM you with assistance + a link.\n\n"
        f"➡️ Support link: {https://alari12.github.io/MindCarePLC/}"
    )

# =========================
# HANDLE GROUP MESSAGES
# =========================
def handle_message(update: Update, context: CallbackContext):
    """Detect trigger words in groups and message the user privately"""
    if not update.message:
        return

    text = update.message.text.lower()
    user = update.message.from_user

    triggers = ["wallet", "crypto", "usdt", "transfer failed"]

    if any(word in text for word in triggers):
        try:
            context.bot.send_message(
                chat_id=user.id,
                text=(
                    f"👋 Hi {user.first_name}, I noticed you mentioned a crypto issue.\n\n"
                    "Here’s what you can do step by step:\n"
                    "1️⃣ Check your wallet connection.\n"
                    "2️⃣ Make sure you have enough network gas fees.\n"
                    "3️⃣ If the issue persists, follow this link:\n\n"
                    f"[Click Here for Help]({HELP_LINK})"
                ),
                parse_mode=ParseMode.MARKDOWN
            )
        except:
            update.message.reply_text(
                f"⚠️ {user.first_name}, I tried to DM you but your privacy settings block it.\n"
                "Please start me privately: /start"
            )

# =========================
# RUN BOT
# =========================
def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    # Message handler (for groups)
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    print("✅ Bot is running...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
