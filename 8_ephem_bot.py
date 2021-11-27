"""
Домашнее задание №1
Использование библиотек: ephem
* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.
"""
import ephem
import keys_and_directories
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {'proxy_url': keys_and_directories.PROXY_URL,
    'urllib3_proxy_kwargs': {'username': keys_and_directories.PROXY_USERNAME, 'password': keys_and_directories.PROXY_PASSWORD}}



def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text('text')

def planet(update, context):
    planets = {
    'Mercury':ephem.Mercury(2021/11/27), 
    'Venus':ephem.Venus(2021/11/27), 
    'Earth':ephem.Earth(2021/11/27), 
    'Mars': ephem.Mars(2021/11/27), 
    'Jupiter':ephem.Jupiter(2021/11/27), 
    'Saturn':ephem.Saturn(2021/11/27), 
    'Uranus':ephem.Uranus(2021/11/27), 
    'Neptune':ephem.Neptune(2021/11/27)
    }

    user_text = update.message.text.split()
    print(user_text)
    user_planet = user_text[-1]
    print(user_planet)
    if user_planet in planets.keys():
        planet_place = planets[user_planet]
        update.message.reply_text(ephem.constellation(planet_place))

def main():
    mybot = Updater(keys_and_directories.API_KEY, request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
   # dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("planet", planet))
    dp.add_handler(MessageHandler(Filters.text, planet))
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()