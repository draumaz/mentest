import pygame, time, gameloops, sys
from backend import exists, read, screen_fade, screen_clear
from dialogdisp import disp_dialog
from gameloops import splash_loop

def main():
    exists()
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Mentest")
    screen = pygame.display.set_mode((640,480))
    if read()[0] == 0:
        gameloops.WIP_loop(screen)
        screen_fade(screen, 0, 255, 0.005, True)
    x = gameloops.splash_loop(screen, 0)
    if x == 0:
        main() # Restart menu. TEMP
    elif x == 1:
        pygame.mixer.music.load("./lib/snd/snd_menuselect.ogg")
        pygame.mixer.music.play()
        screen_clear(screen, (000,000,000)) # Draws over display with given color
        disp_dialog(screen, "Not yet ready!", 0.05, 20, 300) # Feed sleep float and x,y init coords
        screen_clear(screen, (000,000,000))
        main()
    elif x == 2:
        pygame.mixer.music.load("./lib/snd/snd_quit.ogg")
        pygame.mixer.music.play()
        time.sleep(0.17)
        sys.exit()
if __name__ == "__main__":
    main()
