from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import ephem
import datetime
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def planet(bot, update):
    user_text = update.message.text 
    date = datetime.datetime.now()
    planet = getattr(ephem, user_text, None)
    if not planet:
        update.message.reply_text('Название планеты введено неверно')
       
    else:
        answer = ephem.constellation(planet(date))
        update.message.reply_text(answer)
       
def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)
def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)
def main():
    updater = Updater("412093939:AAEQ--i8ZxBcX2KfX3pFfDidYxS6j6qSy1c")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet))
    dp.add_handler(MessageHandler(Filters.text, planet))
    updater.start_polling()
    updater.idle()

main()