class Track:
    def __init__(self):
        self.__dominoes = []
        self.__is_public = False

    def push(self, domino):
        self.__dominoes.append(domino)

    def get_all_except_end(self):
        output = self.__dominoes[:-1]
        self.__dominoes = self.__dominoes[-1:]
        return output

    def get_public(self):
        return self.__is_public

    def set_public(self, public):
        self.__is_public = public

    def draw(self):
        max_size =

