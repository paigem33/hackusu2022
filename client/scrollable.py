import pygame


class Scrollable:
    """
    Scrollable allows for drawing items to an area where you can move around and zoom in and out.
    """
    def __init__(self, size, pos):
        """
        Creates a new scrollable area with the size.
        Parameters:
            size (Vector) Size of the area to use
        """
        self.__size = size  # Size of the scrollable area
        self.__offset = [0, 0]  # Offset to display the scrollable area
        self.__zoom = 1  # Zoom value between 0.0 .. inf. 1.0 being the initial size
        self.__draw_list = []  # Items to draw to the scrollable area
        self.__scrolling = False  # Whether we are currently scrolling or not
        self.__start_mouse_pos = (0, 0)  # The starting mouse position for scrolling
        self.__zoom_factor = 0.03  # Factor to scale the zoom by.
        self.__offset_factor = 0.01  # Factor to scale the offset by
        self.__pos = pos  # Position to draw at

    def resize(self, size):
        """
        Sets the size of the scrollable area.
        Parameters:
            size (Vector) New size of the area.
        """
        self.__size = size

    def get_size(self):
        """
        Returns the size of the scrollable area.
        """
        return self.__size

    def get_pos(self):
        """
        Returns the position to draw at
        """
        return self.__pos

    def set_pos(self, pos):
        """
        Sets the position to draw to
        Parameters:
            pos (Vector)
        """
        self.__pos = pos

    def blit_item(self, surf, rect):
        """
        Adds a new item to the draw list.
        Parameters:
            surf (pygame.Surface) Surface to draw
            rect (pygame.Rect) Rect of the surface
        """
        self.__draw_list.append((surf, rect))

    def draw(self, screen):
        """
        Draws the scrollable area the screen at pos.
        Parameters:
            screen (pygame.Surface) Surface to draw to
        """
        display = pygame.Surface(self.__size)
        display.fill((0, 0, 0, 0))
        for i in range(len(self.__draw_list)):
            surf, rect = self.__draw_list[i]
            # Move the position of the object by the current offset and scale that by the zoom
            item_pos = [(rect[0] + self.__offset[0]) * self.__zoom, (rect[1] + self.__offset[1]) * self.__zoom]
            # Change the zoom to zoom from the offset point not the origin
            item_pos[0] += self.__offset[0] / 2 - (self.__offset[0] / 2 * self.__zoom) * 2
            item_pos[1] += self.__offset[1] / 2 - (self.__offset[1] / 2 * self.__zoom) * 2
            # Scale the size of the surface
            item_size = (rect[2] * self.__zoom, rect[3] * self.__zoom)
            if item_size[0] < 0 or item_size[1] < 0:
                continue
            surf = pygame.transform.scale(surf, item_size)
            display.blit(surf, item_pos)
        self.__draw_list = []
        screen.blit(display, self.__pos)

    def events(self, event):
        """
        Parse an event
        Parameters:
            event (pygame.Event)
        """
        if event.type == pygame.MOUSEWHEEL:
            if event.y == 1:
                # Zoom in by the factor
                self.__zoom += self.__zoom_factor
            else:
                # Zoom out by the factor
                if self.__zoom - self.__zoom_factor > 0:
                    self.__zoom -= self.__zoom_factor
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (event.pos[0] <= self.__size[0] and event.pos[0] >= self.__pos[0]) and (
                    event.pos[1] <= self.__size[1] and event.pos[1] >= self.__pos[1]):
                # If we click inside the scrolling area, say that we are scrolling and get the inital position.
                self.__scrolling = True
                self.__start_mouse_pos = event.pos
        if event.type == pygame.MOUSEBUTTONUP:
            # If we are scrolling, stop scrolling.
            self.__scrolling = False
        if event.type == pygame.MOUSEMOTION:
            if self.__scrolling:
                # Update the offset by the offset from the initial position.
                self.__offset[0] += (event.pos[0] - self.__start_mouse_pos[0]) * self.__offset_factor
                self.__offset[1] += (event.pos[1] - self.__start_mouse_pos[1]) * self.__offset_factor
