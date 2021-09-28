import pygame, time, gameloops
from backend import exists, read, screen_fade

def main():
    exists()
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Mentest")
    screen = pygame.display.set_mode((640,480))
    if read()[0] == 0:
        gameloops.WIP_loop(screen)
        screen_fade(screen, 0, 255, 0.005, True)
    gameloops.splash_loop(screen, 0)

if __name__ == "__main__":
    main()
