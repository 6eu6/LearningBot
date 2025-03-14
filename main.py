import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# الحصول على توكن البوت من متغيرات البيئة
TOKEN = os.getenv("‏7534651038:AAGzEC6nEx0XQVi6Yqv-WuBtFqfYev5GrTM")

# تعريف أمر /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("مرحبًا! البوت يعمل بنجاح 🎉")

# تشغيل البوت
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    
    # إضافة الأمر /start
    dp.add_handler(CommandHandler("start", start))

    # بدء تشغيل البوت
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
