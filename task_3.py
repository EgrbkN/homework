"""
3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
"""

VAR_1 = 'attribute'
VAR_2 = 'класс'
VAR_3 = 'функция'
VAR_4 = 'type'

VAR_LIST = [VAR_1, VAR_2, VAR_3, VAR_4]


for el in VAR_LIST:
    try:
        el.encode('ascii')
    except UnicodeEncodeError:
        print(f'Слово "{el}" невозможно записать в виде байтовой строки.')
