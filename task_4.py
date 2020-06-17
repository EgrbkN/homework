"""
4. Преобразовать слова «разработка», «администрирование», «protocol», «standard»
из строкового представления в байтовое и выполнить обратное преобразование (используя методы encode и decode).
"""

VAR_1 = 'разработка'
VAR_2 = 'администрирование'
VAR_3 = 'protocol'
VAR_4 = 'standard'

VAR_LIST = [VAR_1, VAR_2, VAR_3, VAR_4]

ELEMS_B = []
for el in VAR_LIST:
    el_b = el.encode('utf-8')
    ELEMS_B.append(el_b)

ELEMS_STR = []
for el in ELEMS_B:
    el_s = el.decode('utf-8')
    ELEMS_STR.append(el_s)

print(ELEMS_B)
print(ELEMS_STR)
