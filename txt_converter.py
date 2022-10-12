import dictionary as d


def converter(data):
    with open('catalog.txt', 'a') as file:
        file.write(f'{data}\n')
