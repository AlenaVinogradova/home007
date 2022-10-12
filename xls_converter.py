import dictionary as d

def converter(data):
    with open('catalog.csv', 'a') as file:
        file.write(f'{data.keys()};{data.values()}\n')
