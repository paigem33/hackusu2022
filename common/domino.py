import pathlib
import sys
directory = pathlib.Path(__file__).resolve()
sys.path.append(str(directory.parent.parent))
from client import image

class Domino:
    def __init__(self, a, b, image):
        self.__a = a
        self.__b = b
        self.__image = image

    def get_a(self):
        return self.__a
    """
    returns the "first" value of the domino
    """

    def get_b(self):
        return self.__b
    """
    returns the "second" value of the domino
    """
    def draw(self, screen, pos, angle):
        rot = self.__image.rotate_center(pos, angle)
        screen.blit(rot.get_surface(), pos)
    """
        rot will rotate the image and blit will call the get_surface() function from client.image.py, this will then return the image
        
    """
    def is_double(self):
        if self.__a == self.__b:
            return True
        else:
            return False
    """
    is_double will determine whether or not the domino is a double and will return True or False based on if the numbers are the same
    """
    def get_image(self):
        return self.__image
    """
    get_image simply returns the image
    """