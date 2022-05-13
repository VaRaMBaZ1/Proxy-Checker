import requests
import threading
from datetime import datetime
import time

proxy_file = input("Введите название файла с прокси: ")
timeout = int(input("Введите задержку в секундах: "))
print(" ")
number_of_skolko = 0

def check1(proxy, timee):
    link = "https://www.google.com/"

    proxiessocks = {
        'http': f'socks5://{proxy}',
        'https': f'socks5://{proxy}'
    }

    try:
        requests.get(link, proxies=proxiessocks, timeout=timee)
        my_file = open("goodsocks.txt", "a+")
        my_file.write(proxy + "\n")
        my_file.close()
    except:
        pass


def check2(proxy, timee):
    link = "https://www.google.com/"

    proxieshttp = {
        'http': f'http://{proxy}',
        'https': f'http://{proxy}'
    }

    try:
        requests.get(link, proxies=proxieshttp, timeout=timee)
        my_file = open("goodhttp.txt", "a+")
        my_file.write(proxy + "\n")
        my_file.close()
    except:
        pass


with open(proxy_file) as file:
    proxy_base = ''.join(file.readlines()).strip().split('\n')

start_time = datetime.now()

for string in proxy_base:
    threading.Thread(target=check1, args=(string, timeout,)).start()
    threading.Thread(target=check2, args=(string, timeout,)).start()

    number_of_skolko += 1
    number_of_spisok = len(proxy_base)
    skolkotime = datetime.now() - start_time
    print("\rПроверенно " + str(number_of_skolko) + " из " + str(number_of_spisok) + " | Time: " + str(skolkotime), end='')

print("\n")
print("Завершение потоков...")
time.sleep(3)
print("Все потоки завершены! \n")
u = input("Нажмите Enter для выхода...")