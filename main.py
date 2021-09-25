import os, sys, pygame, random, time
from backend import text_cook, screen_res, snd_press, const_hold, opt_swap, cook_strs
from scr_opt import option_menu

def main_menu(ps, screen):
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("mentest")
    #pygame.display.set_icon(pygame.image.load("./lib/img/icon.png")),(0,0)
    screen.fill((000,000,000))
    screen.blit(pygame.image.load("./lib/img/logo.png"),(160,50))
    screen.blit(text_cook("Comic Sans MS", 30, "PLAY", cook_strs(ps)[0]),(100,350))
    screen.blit(text_cook("Comic Sans MS", 30, "OPTIONS", cook_strs(ps)[1]),(400,350))
    pygame.display.flip()

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
