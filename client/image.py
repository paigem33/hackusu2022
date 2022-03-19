import pygame


class Image:
    def __init__(self, file):
        self.__image = pygame.image.load(file)
        self.__image = self.__image.convert_alpha()
        self.__size = self.__image.get_size()

    def duplicate(self):
        return pygame.Surface.copy(self.__image)

    def rotate(self, angle):  # need to test and make sure it doesn't rotate around (0,0)
        self.__image = pygame.transform.rotate(self.__image, angle)
        self.__size = self.__image.get_size()

    def rotate_pivot(self, pos, origin, angle):
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

        return rotated_image, rotated_image_rect

    def rotate_center(self, pos, angle):
        size = self.get_size()
        return self.rotate_pivot(pos, (size[0] / 2, size[1] / 2), angle)

    def resize(self, size):
        self.__image = pygame.transform.scale(self.__image, size)
        self.__size = self.__image.get_size()

    def resize_ratio(self, x_ratio, y_ratio):
        size = (self.__size[0] * x_ratio, self.__size[1] * y_ratio)
        self.resize(size)

    def flip(self, flip_x, flip_y):
        pygame.transform.flip(self.__image, flip_x, flip_y)
        self.__size = self.__image.get_size()

    def blit(self, screen, rect):
        # needs the first param to be of type pygame.Surface
        self.__image.blit(screen, rect)

    def bounding_box(self, screen):
        rect = self.__image.get_rect()
        pygame.draw.rect(screen, (255, 0, 0), rect)

    def get_surface(self):
        return self.__image

    def get_size(self):
        return self.__size
