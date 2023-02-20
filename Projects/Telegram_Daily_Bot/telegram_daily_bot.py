import telebot
from telebot import types
from urllib.request import urlopen
from bs4 import BeautifulSoup
import decimal

bot = telebot.TeleBot("")

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_1 = types.KeyboardButton("Exchange Rates")
    item_2 = types.KeyboardButton("Weather Forecast")
    markup.add(item_1)
    markup.add(item_2)
    name = message.from_user.first_name
    bot.send_message(message.chat.id, f'Hello {name}! My name is Randy_Rozz_Bot and I am a your personal bot! What do you want to know? Type "/info" for more information', reply_markup=markup)

@bot.message_handler(commands=['info'])
def start_message(message):
    bot.send_message(message.chat.id, "Exchange rates - to check today`s rates \nWeather Forecast - to check today`s forecast")

@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == "Exchange Rates":

        html_bg = urlopen("https://myfin.by/bank/belgazprombank/usd")
        soup_bg = BeautifulSoup(html_bg)
        tags = soup_bg.findAll("td")
        buy_bg = tags[1].text
        sell_bg = tags[2].text

        bot.send_message(message.chat.id, f"In Belgazprombank: buying rate - {buy_bg} BYN, selling rate - {sell_bg} BYN")

        html_pr = urlopen("https://myfin.by/bank/priorbank/usd")
        soup_pr = BeautifulSoup(html_pr)
        tags = soup_pr.findAll("td")
        buy_pr = tags[1].text
        sell_pr = tags[2].text
    
        bot.send_message(message.chat.id, f"In Priorbank: buying rate - {buy_pr} BYN, selling rate - {sell_pr} BYN")

        buying_pr = decimal.Decimal(buy_pr)
        selling_pr = decimal.Decimal(sell_pr)
        buying_bg = decimal.Decimal(buy_bg)
        selling_bg = decimal.Decimal(sell_bg)

        if buying_pr - buying_bg > 0:
            bot.send_message(message.chat.id, f"Best buying rate in Priorbank - {buy_pr} BYN!")
        elif buying_pr - buying_bg == 0:
            bot.send_message(message.chat.id, f"Buying rates are equal!")
        else:
            bot.send_message(message.chat.id, f"Best buying rate in Belgazprombank - {buy_bg} BYN!")
        
        if selling_pr - selling_bg > 0:
            bot.send_message(message.chat.id, f"Best selling rate in Belgazprombank - {sell_bg} BYN!")
        elif selling_pr - selling_bg == 0:
            bot.send_message(message.chat.id, f"Selling rates are equal!")
        else:
            bot.send_message(message.chat.id, f"Best selling rate in Priorbank - {sell_pr} BYN!")
    
    if message.text == "Weather Forecast":

        html_weather = urlopen("https://mogilev.online/2022/11/16/252495.html")
        soup_weather = BeautifulSoup(html_weather)
        tags_weather = soup_weather.findAll("li", {"class": "weather-temp"})
        weather = tags_weather[0].text
        now = int(weather)

        if now <= 10:
            bot.send_message(message.chat.id, f"Temperature now is {weather}, please, dress warmly!")
        elif now > 10 and now <= 15:
            bot.send_message(message.chat.id, f"Temperature now is {weather}, it`s a pleasant!")
        elif now > 15 and now <= 25:
            bot.send_message(message.chat.id, f"Temperature now is {weather}, welcome to spring!")
        elif now > 25:
            bot.send_message(message.chat.id, f"Temperature now is {weather}, dress up it`s will be hot")

bot.polling()
