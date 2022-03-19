import pygame
pygame.init()

class Window:
    pygame.init()
    __display = None

    def __init__(self):
        pass

    def screenSize(self):
        pygame.display.set_mode([500,500])
        screenOpen = True
        while screenOpen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    screenOpen = False
        #GTG? TODO: Use pygame.display.set_mode to create a screen drawing window

    def displayTitle(self, display):
        if self.__display == True:
            pygame.display.set_caption("Mexican Train")
        else:
            return None
        #TODO: Use pygame.display.set_caption("") to set the name of the window

    def isFullScreen(self):
        full = pygame.FULLSCREEN
        if self.__display == True:
            return full
        else:
            return None
        #TODO: Use if statements to set __display to True or False and return a full screen window for the user, use pygame.FULLSCREEN to set full screen
