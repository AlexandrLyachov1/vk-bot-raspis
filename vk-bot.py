from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard
import datetime
from datetime import date
import random
import json
import calendar


import data
time = datetime.datetime.now()
c = calendar.TextCalendar(calendar.MONDAY)
string = c.formatmonth(time.year, time.month)
day = 0
now = datetime.datetime.now()
my_date = date.today()
photo = 'photo-202020100_457239018'

def getDATAS():
    firstDay = 2
    firstMonth = 9
    countDayInWeek = 1
    currentWeek = 1
    while (firstDay != time.day or firstMonth != time.month):
       # print('\n' + str(time.day) + ' = ' + str(firstDay))
        #print(str(time.month) + ' = ' + str(firstMonth))
        if (firstMonth >= 1 and firstMonth <= 6):
            if (firstDay < 28 and (firstDay != time.day or firstMonth != time.month)):
                    firstDay += 1
                    countDayInWeek += 1
                    if (countDayInWeek >= 7):
                        currentWeek += 1
                        countDayInWeek = 0
            if (firstMonth == 2):
                if (firstDay >= 28):
                    firstDay = 1
                    if (firstMonth == 12):
                        firstMonth = 1
                    else:
                        firstMonth += 1
            if (firstMonth % 2 == 0):
                if (firstDay < 30 and (firstDay != time.day or firstMonth != time.month)):
                    firstDay += 1
                    countDayInWeek += 1
                    if (countDayInWeek >= 7):
                        currentWeek += 1
                        countDayInWeek = 0
                if (firstDay >= 30):
                    firstDay = 1
                    if (firstMonth == 12):
                        firstMonth = 1
                    else:
                        firstMonth += 1
            else:
                if (firstDay < 31 and (firstDay != time.day or firstMonth != time.month)):
                    firstDay += 1
                    countDayInWeek += 1
                    if (countDayInWeek >= 7):
                        currentWeek += 1
                        countDayInWeek = 0
                if (firstDay >= 31):
                    firstDay = 1
                    if (firstMonth == 12):
                        firstMonth = 1
                    else:
                        firstMonth += 1
        if (firstMonth >= 9 and firstMonth <= 12):
            if (firstMonth % 2 == 0):
                if (firstDay < 31 and (firstDay != time.day or firstMonth != time.month)):
                    firstDay += 1
                    countDayInWeek += 1
                    if (countDayInWeek >= 7):
                        currentWeek += 1
                        countDayInWeek = 0
                if (firstDay >= 31):
                    firstDay = 1
                    if (firstMonth == 12):
                        firstMonth = 1
                    else:
                        firstMonth += 1
            else:
                if (firstDay < 30 and (firstDay != time.day or firstMonth != time.month)):
                    firstDay += 1
                    countDayInWeek += 1
                    if (countDayInWeek >= 7):
                        currentWeek += 1
                        countDayInWeek = 0
                if (firstDay >= 30):
                    firstDay = 1
                    if (firstMonth == 12):
                        firstMonth = 1
                    else:
                        firstMonth += 1
    if (currentWeek % 2 == 0):
        return day == 1
    else:
        return day == 0
    print('Получившаяся Дата: ' + str(firstDay) + '.' + str(firstMonth) + '\nНеделя: ' + week)
def naSegodnya():
    daySg = datetime.datetime.today().weekday()
    print(daySg)
    if(daySg== 0):
        return 'photo-202020100_45723902'+str(0)
    elif(daySg == 1):
        return 'photo-202020100_45723902'+str(1)
    elif(daySg == 2):
        return'photo-202020100_45723902'+str(2)
    elif(daySg == 3):
        return 'photo-202020100_45723902'+str(3)
    elif(daySg == 4):
        return 'photo-202020100_45723902'+str(4)
    elif(daySg == 5):
        return 'photo-202020100_457239026'
        print(photo)
    elif(daySg == 6):
        return'photo-202020100_457239026'

def naZavtra():
    daySg = datetime.datetime.today().weekday()
    daySg = daySg + 1
    print(daySg)
    if (daySg >= 7):
        daySg = 0
    if(daySg== 0):
        return 'photo-202020100_45723902'+str(0)
    elif(daySg == 1):
        return 'photo-202020100_45723902'+str(1)
    elif(daySg == 2):
        return'photo-202020100_45723902'+str(2)
    elif(daySg == 3):
        return 'photo-202020100_45723902'+str(3)
    elif(daySg == 4):
        return 'photo-202020100_45723902'+str(4)
    elif(daySg == 5):
        return 'photo-202020100_457239026'
        print(photo)
    elif(daySg == 6):
        return'photo-202020100_457239026'
'''def naVchera():
    daySg = datetime.datetime.today().weekday() - 1
    if(daySg== 1):
    elif(daySg == 2):
    elif(daySg == 3):
    elif(daySg == 4):
    elif(daySg == 5):
    elif(daySg == 4):
    elif(daySg == 5):'''
vk_session = VkApi(token='05938bdc29f60e19e5324bb73483305261029221daee6429b903bb2167c1aeb1f26860a5bd8de05ff1270')
vk = vk_session.get_api()
def vksSend():
    keyboard = VkKeyboard(inline=True)
   # keyboard.add_button('На вчера')
    keyboard.add_button('На сегодня')
    keyboard.add_button('На завтра')
    if ( getDATAS() == 1):
        week = "Четная"
    else:
        week = "Нечетная"

    timed= str(calendar.day_name[my_date.weekday()])
    timeday = str(now.day)
    timeMo = str(now.month)
    print(peer_id)
    vk.messages.send(
            peer_id=peer_id,
            message="Сегодня день: "+timeday+ "  месяц:"+timeMo+" неделя "+ week+"\n"+"Какое расписание вам нужно",
            random_id=get_random_id(),
            attachment=naSegodnya(),
            keyboard=keyboard.get_keyboard(),
            )
def zavtra():
    keyboard = VkKeyboard(inline=True)
   # keyboard.add_button('На вчера')
    keyboard.add_button('На сегодня')
    keyboard.add_button('На завтра')
    if ( getDATAS() == 1):
        week = "Четная"
    else:
        week = "Нечетная"

    timed= str(calendar.day_name[my_date.weekday()])
    dv = now.day+1
    timeday = str(dv)
    timeMo = str(now.month)
    print(peer_id)
    vk.messages.send(
            peer_id=peer_id,
            message="Завтра день: "+timeday+ "  месяц:"+timeMo+" неделя "+ week+"\n"+"Какое расписание вам нужно",
            random_id=get_random_id(),
            attachment=naZavtra(),
            keyboard=keyboard.get_keyboard(),
            )

longpoll = VkBotLongPoll(vk_session, 202020100)
while True:
    
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            message = event.obj['message']

            peer_id = message['peer_id']
            text = message['text']

            if text.lower() == 'start':
                vksSend()
            elif text.lower() == 'на сегодня':
                vksSend()
            elif text.lower() == 'на завтра':  
                zavtra()
            else:
                vk.messages.send(
                peer_id=peer_id,
                message='Напиши Start',
                random_id=get_random_id(),
                )
