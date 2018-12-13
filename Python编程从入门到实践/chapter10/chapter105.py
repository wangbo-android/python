import json


class Chapter105:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def store_json():
        try:
            with open('number.json', 'w') as json_file:
                json.dump([2, 3, 4, 6, 8, 10], json_file)
        except FileNotFoundError:
            print('no file found')
        else:
            print('data json stored done')

    @staticmethod
    def load_json():
        try:
            with open('number.json', 'r') as json_file:
                numbers = json.load(json_file)
                print(numbers)
        except FileNotFoundError:
            print('no file found')
        else:
            print('success load json data')


Chapter105.store_json()
Chapter105.load_json()


def get_names(first, last):
    return first + ' ' + last
