"""
5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты
из байтовового в строковый тип на кириллице.
"""

import subprocess

import chardet

args = ['ping', 'youtube.com']
YA_PING = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in YA_PING.stdout:

    result = chardet.detect(line)
    data = line.decode(result['encoding']).encode('utf-8')
    print(data.decode('utf-8'))
