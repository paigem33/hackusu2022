import domino
import pygame
import pathlib
import sys
directory = pathlib.Path(__file__).resolve()
sys.path.append(str(directory.parent.parent))
from client import image

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
        max_size = self.__dominoes[len(self.__dominoes)].get_size()
        width = 0
        height = 0
        for domino in self.__dominoes:
            if domino.is_double() == False:
                height += domino.get_size()[1]
                width = domino.get_size()[0]
            elif domino.is_double() == True:
                width += domino.get_size()[1]
                height = domino.get_size()[0]
        if max_size == 0:
            return width == 0
        size = width,height
        color = (0,0,0,0)
        surface = pygame.Surface(size, color)
        y = 0
        for domino in self.__dominoes:
            image = domino.get_image()
            if domino.isdouble() == False:
                x = height/3
            elif domino.isdouble() == True:
                x = 0
            image.blit(surface,(x,y))
            y += height


        return surface