from time import time

import pygame

import fps
from window import Window
from image import Image
from os import getcwd
from scrollable import Scrollable
from asset_bank import ASSET_BANK


def main():
    window = Window([900, 900], "Mexican Train", False, False)
    load_assets()
    running = True
    fps_counter = fps.FpsCounter()
    image = ASSET_BANK.get_asset("1.png")
    angle = 0
    scroll = Scrollable(window.get_screen_size(), (0, 0))
    while running:
        screen = window.get_screen()
        screen.fill((255, 255, 255))
        start_time = time()
        fps_counter.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            scroll.events(event)
        rotated_image, bounding_box = image.rotate_center((100, 100), angle)
        scroll.blit_item(rotated_image, bounding_box)
        scroll.draw(screen)
        angle += 1
        if angle > 360:
            angle = 0
        window.display()
        fps.limit_fps(start_time, 60)
        #print(fps_counter.get_fps())
    pygame.quit()

def load_assets():
    ASSET_BANK.save_asset("1.png", Image("assets/Light theme/1.png"))
    ASSET_BANK.save_asset("hub.png", Image("assets/Mexican_Train_Game_Station.png"))


if __name__ == "__main__":
    main()
