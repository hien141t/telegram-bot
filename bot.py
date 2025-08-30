from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Dán API Token lấy từ BotFather vào đây
TOKEN = "8403015506:AAEXoI8TqKTFSz9o08Vrf23G8tPvaWO_dJc"

# Xử lý lệnh /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Xin chào 👋! Tôi là bot Telegram test của bạn 🚀")

# Xử lý khi người dùng gửi tin nhắn thường
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(f"Bạn vừa gửi: {text}")

def main():
    app = Application.builder().token(TOKEN).build()

    # Đăng ký lệnh /start
    app.add_handler(CommandHandler("start", start))

    # Đăng ký trả lời cho mọi tin nhắn text
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("✅ Bot đang chạy... Nhắn /start trong Telegram để test")
    app.run_polling()

if __name__ == "__main__":
    main()
