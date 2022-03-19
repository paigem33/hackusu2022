

class Domino:
    def __init__(self, a, b, image):
        self.__a = a
        self.__b = b
        self.__image = image

    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

    def draw(self, screen, pos, angle):
        rot =
        screen.blit(self.__image, pos)

