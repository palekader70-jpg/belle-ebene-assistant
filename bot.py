
import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌹 Bonjour ! Bienvenue chez Belle Ébène Assistante.\n\n"
        "Je suis ton assistante pour les pronostics sportifs.\n"
        "Envoie-moi un message pour commencer."
    )

async def recevoir_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Merci pour ton message ! ❤️\n"
        "Je prépare encore mes fonctions d'analyse des matchs."
    )

def main():
    token = os.environ["BOT_TOKEN"]

    application = Application.builder().token(token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, recevoir_message)
    )

    application.run_polling()

if __name__ == "__main__":
    main()
