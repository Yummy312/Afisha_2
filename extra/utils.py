class RandomCode:

    def __init__(self):
        self.__code = None

    @property
    def generate_code(self):
        import string
        import random
        data = ','.join(string.ascii_letters + string.digits).split(',')
        random.shuffle(data)
        self.__code = ','.join(data[0:6]).replace(',', '')
        return self.__code