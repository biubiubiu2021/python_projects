import pygame
from pygame.locals import *
import sys

screenWidth = 822
screenHight = 199
FPS =30

def main_game():
    screenWidth = 822
    screenHight = 199
    FPS = 30
    score=0
    over=False
    global SCREEN, FPSCLOCK
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode((screenWidth,screenHight))
    pygame.display.set_caption("mama")

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main_game()