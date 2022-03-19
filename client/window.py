import pygame


class Window:
    """
    Window abstraction class.
    """

    def __init__(self, size, title, fullscreen, vsync):
        """
        Creates a new window.
        Parameters:
            size (Vector) Size of the window in pixels
            title (String) Title to show at the top
            fullscreen (bool) Whether to be fullscreen
            vsync (bool) Whether to use vsync
        """
        if fullscreen:
            flags = pygame.FULLSCREEN
        else:
            flags = 0
        pygame.display.set_caption(title)
        self.__size = size
        self.__display = pygame.display.set_mode(size, flags=flags, vsync=vsync)

    def get_screen_size(self):
        """
        Returns the size of the screen
        """
        return self.__size

    def get_screen(self):
        """
        Returns a reference to the drawing window
        """
        return self.__display

    def display(self):
        """
        Flops the internal buffer for the window and displays the frame.
        """
        pygame.display.flip()
