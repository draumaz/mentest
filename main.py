import pygame
from backend import savesys, screen_fade
from gameloops import splash_loop_selector, WIP_loop

def main():
    savesys.exists()
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Mentest")
    screen = pygame.display.set_mode((640,480))
    if savesys.read()[0] == 0:
        WIP_loop(screen)
        screen_fade(screen, 0, 255, 0.005, True)
    splash_loop_selector(screen, 0)

if __name__ == "__main__":
    main()
