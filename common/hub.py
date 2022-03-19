class Hub:
    """
    The hub that all tracks branch off of, stores the starting domino
    """
    def __init__(self, tracks, hub_image, starting_domino):
        """
        Create the Hub, keeps track of the tracks in a list, the hub_image, and the starting domino
        Parameters:
            list of track objects
            hub image (pygame.Surface)
            starting domino as domino object
        """
        self.__tracks = tracks
        self.__hub_image = hub_image
        self.__starting_domino = starting_domino


    def get_track(self, index):
        """
        Returns the track object at the selected index
        Parameters:
            index of track
        """
        return self.__tracks[index]

    def draw(self, screen, rect):
        """
        Draws the hub image to the screen
        Parameters:
            screen (pygame.Surface) Surface to draw to
        """
        screen.blit(self.__hub_image.get_surface(), rect)

    def get_starting_domino(self):
        """
        returns the starting domino object
        """
        return self.__starting_domino

    def draw_starting_domino(self, screen, rect):
        """
        draw the starting domino into the middle of the hub
        """
        pass

    # draw_tracks()
    # based on the number of players, rotate the tracks into unoccupied positions on the hub and draw them there 
    def draw_tracks(self, screen, rect):
        players = len(self.__tracks)

        if players <= 4 and players >= 2:
            # get position for the diagonal slots and loop through self.__tracks and draw them in that position
            pass
        elif players <= 6 and players >= 5:
            # get position for the diagonal slots and loop through self.__tracks and draw them in that position
            pass
        elif players <= 8 and players >= 7:
            pass
        