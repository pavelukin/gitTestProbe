from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import ephem
import datetime
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )
def calc (bot, update, args):
    if not args:
        update.message.reply_text('вы ничего не ввели, а следовало бы')
        return
    phrase = ' '.join(args)
    print (phrase)
    check_begin = phrase.startswith('"')
    check_end = phrase.endswith('"')
    num_1 = float (phrase[1])
    num_2 = float(phrase[3])
    print (num_2)
    if check_begin and check_end and len (phrase) == 6: 
        print ('попали в нужное место')
        check_move = str (phrase[2])
        try:
            if check_move == '+':
                result = num_1 + num_2
            elif check_move == '*':
                result = num_1 * num_2
            elif check_move == '-':
                result = num_1 - num_2
            elif check_move == '/':
                result = num_1 / num_2
            else:
                update.message.reply_text("не удалось распознать арифметическую операцию")
                return
        except:
            update.message.reply_text("неправильный формат чисел или деление на ноль, не надо так")
            return

    else: 
        update.message.reply_text("Введите по-человечески, будьте ж людьми")
        return   
    print (result)    
    update.message.reply_text(result)

def wordcount (bot, update, args):
    if not args:
        update.message.reply_text('вы ничего не ввели, а следовало бы')
        return
    phrase = ' '.join(args)
    print (phrase)
    check_begin = phrase.startswith('"')
    check_end = phrase.endswith('"')
    if check_begin and check_end and phrase [1] != " ":
        number_words = phrase.split(' ')
        print (number_words)
        update.message.reply_text(len(number_words))
        print ('попали в нужное место')
    else: 
        update.message.reply_text("Введите по-человечески, будьте ж людьми")
        return
def planet(bot, update, args):
   # user_text = update.message.text 
    date = datetime.datetime.now()
    print (args)  
    if not args:
        update.message.reply_text('вы не ввели название планеты')
        return 
    planet = getattr(ephem, args[0], None)
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
    dp.add_handler(CommandHandler("planet", planet, pass_args = True))
    dp.add_handler(CommandHandler("wordcount", wordcount, pass_args = True))
    dp.add_handler(CommandHandler("calc", calc, pass_args = True))
    dp.add_handler(MessageHandler(Filters.text, planet))
    updater.start_polling()
    updater.idle()

main()