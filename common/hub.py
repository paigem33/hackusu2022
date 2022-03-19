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

    def draw(self, scrollable, rect):
        """
        Draws the hub image to the screen
        Parameters:
            screen (pygame.Surface) Surface to draw to
        """
        scrollable.blit_item(self.__hub_image.get_surface(), rect)
        # TODO: draw starting domino into hub
        self.draw_tracks(scrollable, rect) # do the same thing as line 32

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

    def draw_tracks(self, scrollable, rect):

        rotations = [] # fill with the rotation needed for each track starting at 1
        positions = [] # take the rect and get the needed adjustments for each track starting at 1

        positions.append()

        item = 0
        for track in self.__tracks:
            track.rotate(rotations[item])
            scrollable.blit_item(self.__hub_image.get_surface(), rect)

        