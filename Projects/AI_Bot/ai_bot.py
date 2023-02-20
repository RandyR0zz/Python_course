#класс и модули для создания бота
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters 

#специальный класс и модуль для оценивания вопросов
from fuzzywuzzy import fuzz 

#модуль для загрузки и чтения json файлов
import json

#класс необходим для рандомного ответа пользователю
import random 

#токен
updater = Updater(token='')

#диспетчер
dispatcher = updater.dispatcher

#читаем json файл (так как текст русский добавляем режим encoding)
f = open('Python\data.json', 'r', encoding='utf-8')

#загрузка открытого json файла
data_base = json.load(f)

#функция для обработки start команды от бота
def start_message(update, context):
    context.bot.send_message(chat_id = update.message.chat_id, text='Доброго дня!')

#функция для обработки входящего сообщения
def in_message(message_string: str):
    data_log = {'message_string': '', 'percent': 0}
    for message in data_base["ask"]:
        for x in data_base["ask"][message]:
            middle_message = fuzz.ratio(message_string, x)
            if middle_message > data_log['percent']:
                data_log['message_string'] = message
                data_log['percent'] = middle_message
    return data_log

#функция для обработки ответа на обработанное входящее сообщение
def answer(key):
    return random.choice(data_base["answer"][key])

#функция для отправки сообщения пользователю
def text_message(update, context):
    choice = in_message(update.message.text)
    test_data = choice['percent']
    try:
        if test_data > 20:
            out_answer = answer(choice['message_string'])
            context.bot.send_message(chat_id = update.message.chat_id, text=f'{out_answer}')
        else:
            context.bot.send_message(chat_id = update.message.chat_id, text=f'Простите, я Вас не понял!')
    except KeyError:
        context.bot.send_message(chat_id = update.message.chat_id, text=f'Простите, я Вас не понял!')

#хэндлеры и отправка их в диспетчер
start_command_handler = CommandHandler('start', start_message)
text_message_handler = MessageHandler(Filters.text, text_message)

dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)

updater.start_polling()
updater.idle()