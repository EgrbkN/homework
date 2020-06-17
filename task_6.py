"""
6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.
"""

from chardet import detect

LINES_LIST = ['сетевое программирование', 'сокет', 'декоратор']
with open('test_file.txt', 'w') as file:
    for line in LINES_LIST:
        file.write(f'{line}\n')
file.close()

with open('test_file.txt', 'rb') as file:
    content = file.read()
encoding = detect(content)['encoding']
print(encoding)

with open('test_file.txt', 'r', encoding=encoding) as file:
    content = file.read()
print(content)
