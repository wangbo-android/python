class OperateFile:

    @staticmethod
    def read_file():
        with open('pi_digits') as file_object:
            contents = file_object.read()
            print(contents.rstrip())

    @staticmethod
    def read_file_in_direction():
        with open(r'files\file1') as file_object:
            contents = file_object.read()
            print(contents.rstrip())

    @staticmethod
    def read_file_by_line():
        with open('pi_digits') as file_object:
            for line in file_object:
                print(line.rstrip())

    @staticmethod
    def read_file_into_list():
        with open('pi_digits') as file_object:
            lines = file_object.readlines()
        pi_string = ''
        for line in lines:
            pi_string += line.strip()

        print(pi_string)
        print(len(pi_string))


OperateFile.read_file()
OperateFile.read_file_in_direction()
OperateFile.read_file_by_line()
OperateFile.read_file_into_list()
