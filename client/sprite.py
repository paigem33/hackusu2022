import pygame


class Sprite:
    def __init__(self, image, position):
        self.image = image
        self.position = position

    def draw(self, screen):
        self.image.blit(screen)
