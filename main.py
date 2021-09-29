import pygame, time, gameloops, sys
from backend import exists, read, screen_fade, screen_clear
from dialogdisp import disp_dialog
from gameloops import splash_loop, splash_loop_selector

def main():
    exists()
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Mentest")
    screen = pygame.display.set_mode((640,480))
    if read()[0] == 0:
        gameloops.WIP_loop(screen)
        screen_fade(screen, 0, 255, 0.005, True)
    splash_loop_selector(screen, 0)
if __name__ == "__main__":
    main()
