class Chapter104:

    @staticmethod
    def something_error():

        try:
            print(5 / 1)
        except ZeroDivisionError:
            print('You can not divide by zero')
        else:
            print('there is not exception occured')

    @staticmethod
    def not_found_file():

        try:
            with open('temp.txt') as file:
                print(file.read())
        except FileNotFoundError:
            print('file is not found')
        else:
            print('everything is ok')


Chapter104.something_error()
Chapter104.not_found_file()

