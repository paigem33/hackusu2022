import pygame
from asset_bank import init_assets
from game import Game


def main():
    pygame.init()
    game = Game()

    game.run()
    pygame.quit()


if __name__ == "__main__":
    main()
