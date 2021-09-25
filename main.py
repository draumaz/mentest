import os, sys, pygame, random, time
from backend import text_cook, screen_res, snd_press, const_hold, opt_swap, cook_strs
from scr_opt import option_menu
from splash import main_menu

def temp_func(screen):
    main_menu(0, screen)
    ms = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    if ms == 1:
                        pygame.mixer.music.load(snd_press())
                        pygame.mixer.music.play()
                        print("Play select")
                        const_hold(screen)
                        main_menu(1, screen)
                    elif ms == 2:
                        option_menu(2, screen, running)
                        #pygame.mixer.music.load(snd_press())
                        #pygame.mixer.music.play()
                        #print("Options select")
                        #const_hold(screen)
                        #main_menu(2, screen)
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if ms == 1:
                        ms = opt_swap("white", "gray", screen)
                    else:
                        ms = opt_swap("gray", "white", screen)
                    pygame.display.flip()
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if ms == 2:
                        ms = opt_swap("gray", "white", screen)
                    else:
                        ms = opt_swap("white", "gray", screen)
                    pygame.display.flip()


def main():
    temp_func(screen_res(640,480))

if __name__ == "__main__":
    main()
