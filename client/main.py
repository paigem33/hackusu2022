from time import time

import pygame

import fps
from window import Window
from image import Image
from os import getcwd


def main():
    print(getcwd())
    window = Window([800, 800], "Mexican Train", False, False)
    running = True
    fps_counter = fps.FpsCounter()
    image = Image(open(getcwd() + "/assets/Light theme/1.png"))
    angle = 0
    while running:
        screen = window.get_screen()
        screen.fill((255, 255, 255))
        start_time = time()
        fps_counter.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        rotated_image, bounding_box = image.rotate_center((screen.get_width() / 2, screen.get_height() / 2), angle)
        screen.blit(rotated_image, bounding_box)

        angle += 1
        if angle > 360:
            angle = 0
        window.display()
        fps.limit_fps(start_time, 60)
        print(fps_counter.get_fps())
    pygame.quit()


if __name__ == "__main__":
    main()
