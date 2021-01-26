from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard
import datetime
from datetime import date
import random
import json
import calendar
import requests

url = 'http://api.openweathermap.org/data/2.5/weather?q=moscow,ru&appid=f765a62486dd5839cfc0051699c8d603'
#"api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}"
#url = 'http://pro.openweathermap.org/data/2.5/forecast/hourly?q=moscow&appid=f765a62486dd5839cfc0051699c8d603'
response = requests.get(url)
jsonfile = response.json()
Kalvin = 273
JSKalvin = int(jsonfile['main']['temp'])
#temps = jsonfile['temp']
#json_obj_list = json.load(jsonfile)['temp']
print(JSKalvin-Kalvin)
