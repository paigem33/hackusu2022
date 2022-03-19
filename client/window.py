import pygame


class Window:
    def __init__(self, size, title, fullscreen, vsync):
        pygame.init()
        if fullscreen:
            flags = pygame.FULLSCREEN
        else:
            flags = 0
        pygame.display.set_caption(title)
        self.__size = size
        self.__display = pygame.display.set_mode(size, flags=flags, vsync=vsync)

    def get_screen_size(self):
        return self.__size

    def get_screen(self):
        return self.__display

    def display(self):
        pygame.display.flip()
