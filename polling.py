from telegram.ext import Updater
from telegram.ext import CommandHandler
from services.telegram.TelegramBase import *

global_config = get_config()

updater = Updater(token=global_config['TG']['TOKEN'], use_context=True)

dispatcher = updater.dispatcher


def tagav8d(update, context):
    t = TelegramBase()
    t.tag_av8d(update.message.chat_id)
    # dump(update)
    # dump(context)
    # context.bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


start_handler = CommandHandler('tagav8d', tagav8d)
dispatcher.add_handler(start_handler)

updater.start_polling()
