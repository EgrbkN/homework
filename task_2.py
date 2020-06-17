"""
2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность
кодов (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.
"""

STR_1 = b'class'
STR_2 = b'function'
STR_3 = b'method'

STR_LIST = [STR_1, STR_2, STR_3]

for el in STR_LIST:
    print(type(el))
    print(el)
    print(len(el))
