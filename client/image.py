import pygame


class Image:
    """
    Abstraction over a surface for higher level actions.
    """

    def __init__(self, image):
        """
        Create a new image from a file path
        Parameters:
            image (string or pygame.Surface) Path of the image to open or a Surface
        """
        if isinstance(image, pygame.Surface):
            self.__image = image
            self.__size = self.__image.get_size()
        else:
            self.__image = pygame.image.load(image)
            self.__image = self.__image.convert_alpha()
            self.__size = self.__image.get_size()

    def duplicate(self):
        """
        Returns a copy of this image
        """
        return Image(pygame.Surface.copy(self.__image))

    def rotate(self, angle):
        """
        Rotates the image around (0, 0)
        """
        return Image(pygame.transform.rotate(self.__image, angle))

    def rotate_pivot(self, pos, origin, angle):
        """
        Rotates the image around the origin point and returns it
        Parameters:
            pos (Vector) Position that you are going to draw it at
            origin (Vector) Point to rotate around
            angle (float) Angle in degrees to rotate to
        """
        # offset from pivot to center
        image_rect = self.__image.get_rect(topleft=(pos[0] - origin[0], pos[1] - origin[1]))
        offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center

        # roatated offset from pivot to center
        rotated_offset = offset_center_to_pivot.rotate(-angle)

        # roatetd image center
        rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

        # get a rotated image
        rotated_image = pygame.transform.rotate(self.__image, angle)
        rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)

        return Image(rotated_image), rotated_image_rect

    def rotate_center(self, pos, angle):
        """
        Rotates the image around the center and returns it
        Parameters:
            pos (Vector) Position to draw at
            angle (float) Angle to rotate to
        """
        size = self.get_size()
        return self.rotate_pivot(pos, (size[0] / 2, size[1] / 2), angle)

    def resize(self, size):
        """
        Resizes the image to the size.
        Parameters:
            size (Vector) New size of the image
        """
        return Image(pygame.transform.scale(self.__image, size))

    def resize_ratio(self, x_ratio, y_ratio):
        """
        Resizes the image based off of a ratio
        Parameters:
            x_ratio (float) Ratio to scale the x size by
            y_ratio (float) Ratio to scale the y size by
        """
        size = (self.__size[0] * x_ratio, self.__size[1] * y_ratio)
        return self.resize(size)

    def flip(self, flip_x, flip_y):
        """
        Flips the image and returns the flipped version
        Parameters:
            flip_x (bool) To flip the x or not
            flip_y (bool) To flip the y or not
        """
        return Image(pygame.transform.flip(self.__image, flip_x, flip_y))

    def blit(self, screen, rect):
        """
        Blits the image to the screen
        Parameters:
            screen (pygame.Surface) Surface to draw to
            rect (pygame.Rect) Rect to draw by
        """
        screen.blit(self.__image, rect)

    def bounding_box(self, screen):
        """
        Draws the bounding box for this image. Usefull for debugging.
        Parameters:
            screen (pygame.Surface) Surface to draw to
        """
        rect = self.__image.get_rect()
        pygame.draw.rect(screen, (255, 0, 0), rect)

    def get_surface(self):
        """
        Returns a reference to the pygame surface
        """
        return self.__image

    def get_size(self):
        """
        Returns the size of the image
        """
        return self.__size
