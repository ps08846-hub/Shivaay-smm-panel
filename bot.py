"""Shivaay SMM Telegram bot starter (demo only).
No supplier/API integration and no payments are processed.
Requires Python 3.10+ and python-telegram-bot 21.x.
"""
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
SERVICES = {
    "instagram": "Instagram content audit / legitimate promotion help",
    "youtube": "YouTube channel audit / promotion campaign help",
    "facebook": "Facebook Page promotion assistance",
    "telegram": "Telegram channel setup assistance",
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("📋 Services", callback_data="services")],
                [InlineKeyboardButton("ℹ️ About", callback_data="about")]]
    await update.message.reply_text(
        "Welcome to Shivaay SMM!\n\nThis is a demo bot. No real orders or payments are processed.",
        reply_markup=InlineKeyboardMarkup(keyboard))

async def services(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "Available demo categories:\n" + "\n".join(f"• {name}: {desc}" for name, desc in SERVICES.items())
    text += "\n\nSend /order to see the demo order instructions."
    if update.callback_query:
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(text)
    else:
        await update.message.reply_text(text)

async def order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Demo order flow only. No payment or supplier order is created.\n"
        "Next production steps: add a database, admin review, verified service provider API, "
        "and an approved payment gateway. Never share your bot token.")

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    await update.callback_query.edit_message_text(
        "Shivaay SMM is a prototype. Prices, wallet balance, payments, and supplier delivery are not connected.")

async def main():
    if not BOT_TOKEN:
        raise RuntimeError("Set TELEGRAM_BOT_TOKEN in your environment; do not paste it into source code.")
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("services", services))
    app.add_handler(CommandHandler("order", order))
    app.add_handler(CallbackQueryHandler(services, pattern="^services$"))
    app.add_handler(CallbackQueryHandler(about, pattern="^about$"))
    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    print("Shivaay SMM demo bot is running. Press Ctrl+C to stop.")
    import asyncio
    try:
        await asyncio.Event().wait()
    finally:
        await app.updater.stop()
        await app.stop()
        await app.shutdown()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
