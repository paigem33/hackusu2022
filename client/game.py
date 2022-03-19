import pathlib
import sys
import pygame
import fps
from asset_bank import ASSET_BANK
from window import Window
from scrollable import Scrollable
from time import time
#from client_net import ClientNet

directory = pathlib.Path(__file__).resolve()
sys.path.append(str(directory.parent.parent))
from asset_bank import init_assets
from common import hub
from common import track
from common import domino

class Game:
    """
    Encapsulates all the game data
    """

    def __init__(self):
        """
        Creates a new window and objects in the window
        """
        self.__window = Window([900, 900], "Mexican Train", False, False)
        init_assets()
        self.__running = True
        self.__fps_counter = fps.FpsCounter()
        self.__scroll = Scrollable(self.__window.get_screen_size(), (0, 0))
        self.__angle = 0
        self.__tracks = [] 
        self.__tracks.append(track.Track()) # will loop through and add based on number of players
        
        self.__hub = hub.Hub(self.__tracks, ASSET_BANK.get_asset("hub.png"), domino.Domino(12, 12, ASSET_BANK.get_asset("1.png"))) # needs list of tracks, hub image, starting_domino
        #self.__net = ClientNet()

    def __events(self):
        """
        Polls for events
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__running = False
            self.__scroll.events(event)

    def __update(self):
        """
        Updates objects
        """
        self.__fps_counter.update()
        self.__angle += 1
        #self.__net.update()

    def __draw(self):
        """
        Draws objects to display
        """
        screen = self.__window.get_screen()
        screen.fill((255, 255, 255))
        image = ASSET_BANK.get_asset("1.png")
        #rotated_image, bounding_box = image.rotate_center((100, 100), self.__angle)
        self.__hub.draw(self.__scroll, (100,100))
        # self.__scroll.blit_item(rotated_image, bounding_box)
        self.__scroll.draw(screen)
        self.__window.display()

    def run(self):
        """
        While running, poll events, update, and draw.
        """
        while self.__running:
            start_time = time()
            self.__events()
            self.__update()
            self.__draw()
            fps.limit_fps(start_time, 60)
