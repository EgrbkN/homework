import yaml

data_in = {
    'items': ['TV', 'Microphone', 'PC', 'Notebook'],
    'items_quantity': 4,
    'items_price': {
        'TV': '100-1000€',
        'Microphone': '50-200€',
        'PC': '300-2000€',
        'Notebook': '500-2500€'
    }
}

with open('file.yaml', 'w', encoding='utf-8') as file_in:
    yaml.dump(data_in, file_in, default_flow_style=False, allow_unicode=True)

with open('file.yaml', 'r', encoding='utf-8') as file_out:
    data_out = yaml.load(file_out, Loader=yaml.SafeLoader)

print(data_in == data_out)