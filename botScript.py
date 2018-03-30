from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

getting = {}

id_array = []

updater = Updater(token = '530366823:AAHQTjKELJ80jEyoEd1QanGnw5eumUI_msc')
dispatcher = updater.dispatcher


def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text = 'Давай общаться?')

def helpCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text = '')

def textMessage(bot, update):
    if (update.message.chat_id not in id_array):
        id_array.append(update.message.chat_id)
        getting[update.message.chat_id] = []
    print(getting) 
    getting[update.message.chat_id].append(update.message.text)
    if (getting[update.message.chat_id][len(getting[update.message.chat_id]) - 1] == "Triangle"):
        bot.send_message(chat_id = update.message.chat_id, text = "Введите стороны треугольника")
    elif (getting[update.message.chat_id][len(getting[update.message.chat_id]) - 2] == "Triangle"):
        string = getting[update.message.chat_id][len(getting[update.message.chat_id]) - 1].split()
        a = int(string[0])
        b = int(string[1])
        c = int(string[2])
        if (a < b+c) and (b < c+a) and (c < b+a):
            bot.send_message(chat_id = update.message.chat_id, text = "Можно")
        else:
            bot.send_message(chat_id = update.message.chat_id, text = "Нельзя")
    elif (getting[update.message.chat_id][len(getting[update.message.chat_id]) - 1] == "реши"):
        bot.send_message(chat_id = update.message.chat_id, text = "Введите a b c")
    elif (getting[update.message.chat_id][len(getting[update.message.chat_id]) - 2] == "реши"):
        string = getting[update.message.chat_id][len(getting[update.message.chat_id]) - 1].split()
        a = int(string[0])
        b = int(string[1])
        c = int(string[2])
        d = b*b - 4*a*c
        x1 = (-b + d**(1/2))/(2*a)
        x2 = (-b - d**(1/2))/(2*a)
        res = "x1 = "+str(x1)+" x2 = "+str(x2)
        bot.send_message(chat_id = update.message.chat_id, text = res)
    elif (getting[update.message.chat_id][len(getting[update.message.chat_id]) - 1] == "Сложи"):
        bot.send_message(chat_id = update.message.chat_id, text = "Введите числа (2)")
    elif (getting[update.message.chat_id][len(getting[update.message.chat_id]) - 2] == "Сложи"):
        string = getting[update.message.chat_id][len(getting[update.message.chat_id]) - 1].split()
        a = int(string[0])
        b = int(string[1])
        res = a + b
        bot.send_message(chat_id = update.message.chat_id, text = str(res))
    else:
        res = 'Получил ваше сообщение: '+ update.message.text
        bot.send_message(chat_id = update.message.chat_id, text = res)
    
start_handler = CommandHandler('start', startCommand)
text_handler = MessageHandler(Filters.text, textMessage)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(text_handler)

updater.start_polling(clean=True)

updater.idle()
