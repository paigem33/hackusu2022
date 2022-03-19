import pygame
from image import Image
from asset_bank import ASSET_BANK
from game import Game


def main():
    pygame.init()
    game = Game()
    load_assets()
    game.run()
    pygame.quit()


def load_assets():
    ASSET_BANK.save_asset("1.png", Image("assets/Light theme/1.png"))
    ASSET_BANK.save_asset("hub.png", Image("assets/Mexican_Train_Game_Station.png"))


if __name__ == "__main__":
    main()
