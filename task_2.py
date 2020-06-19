# Задание на закрепление знаний по модулю json.
# Есть файл orders в формате JSON с информацией о заказах.
# Написать скрипт, автоматизирующий его заполнение данными.

import json

def write_order_to_json(item, quantity, price, buyer, date):

    with open('orders.json', 'r', encoding='utf-8') as file_out:
        data = json.load(file_out)

    with open('orders.json', 'w', encoding='utf-8') as file_in:
        orders_list = data['orders']
        order_info = {
            'item': item,
            'quantity': quantity,
            'price': price,
            'buyer': buyer,
            'date': date
        }
        orders_list.append(order_info)
        json.dump(data, file_in, ensure_ascii=False, indent=4)

write_order_to_json('Гречка', '5', '140', 'Петрова А.В.', '18.06.2020')
write_order_to_json('Мука', '10', '100', 'Иванова В.А.', '17.06.2020')
write_order_to_json('Шашлык', '2','350','Аратунян Г.Н.', '01.06.2020')