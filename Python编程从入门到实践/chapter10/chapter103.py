class Chapter103:

    @staticmethod
    def write_into_file():
        with open(r'files\file1', 'w') as write_object:
            write_object.write('I am a programer.\n')
            write_object.write('I love code.\n')

    @staticmethod
    def write_into_afile():
        with open(r'files\file1', 'a') as write_object:
            write_object.write('I am a programer.\n')
            write_object.write('I love code.\n')


Chapter103.write_into_afile()
