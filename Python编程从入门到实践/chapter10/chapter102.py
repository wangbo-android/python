class Chapter102:

    @staticmethod
    def birthday_in_pi():
        with open(r'files\file1') as read_object:
            lines = read_object.readlines()
            pi_string = ''
            for line in lines:
                pi_string += line.strip()
            birthday = input('enter your birthday')
            if birthday in pi_string:
                print('yes')
            else:
                print('no')


Chapter102.birthday_in_pi()
