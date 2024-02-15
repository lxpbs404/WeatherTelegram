import telebot
import requests
import json

bot = telebot.TeleBot('BOT_TOKEN')
api = 'OPENWEATHERMAP_API'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '<b>Hi!\nThis is bot for weather checking.</b>\n\n<b><i>Please, type a city name.</i></b>', parse_mode='html')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city_name = message.text.strip()
    url = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api}&units=metric')
    if url.status_code == 200:
        data = json.loads(url.text)
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        wind = data["wind"]["speed"]
        pressure = data["main"]["pressure"]
        humidity = data["main"]["humidity"]
        bot.reply_to(message,
                f'<u><b>Weather in {city_name}</b></u>\n'
                f'<b>Temperature:</b> {temp} <b>°C (Feels like</b> {feels_like} <b>°C)</b>\n'
                f'<b>Wind:</b> {wind} <b>mps</b>\n'
                f'<b>Pressure:</b> {pressure} <b>мм.рт.ст</b>\n'
                f'<b>Humidity:</b> {humidity}<b>%</b>\n'
                f'<b>Developer: @lxpbs</b>',
                parse_mode='html'
                )
    else:
        bot.reply_to(message, '<b>Invalid city name!</b>', parse_mode='html')


bot.infinity_polling()
