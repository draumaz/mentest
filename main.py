import pygame, time, gameloops
from backend import exists, read

def main():
    exists()
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Mentest")
    screen = pygame.display.set_mode((640,480))
    if read()[0] == 0:
        gameloops.WIP_loop(screen)
        for i in range(0, 255):
            v = 255-i
            screen.fill((v,v,v))
            time.sleep(0.005)
            pygame.display.flip()
    gameloops.splash_loop(screen, 0)

if __name__ == "__main__":
    main()
