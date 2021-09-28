import pygame
import time

def disp_dialog_pause(screen):
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    screen.fill((255,255,255))
                    screen.blit(pygame.image.load("./lib/img/img_dialog.png"), (0,0))
                    pygame.display.flip()
                    return 0
                else:
                    continue


def disp_dialog(screen, screen_color, text, sleep_time, init_pos_x, init_pos_y):
    t = list(text)
    screen.fill(screen_color)
    screen.blit(pygame.image.load("./lib/img/img_dialog.png"), (0,0))
    pygame.display.flip()
    pygame.mixer.init()
    pygame.font.init() 
    for i in range(0, len(t)):
        screen.blit(pygame.font.SysFont("lucidasans", 25).render(t[i], False, (255,255,255)), (init_pos_x,init_pos_y))
        time.sleep(sleep_time)
        pygame.mixer.music.load("./lib/snd/snd_speech.ogg")
        pygame.mixer.music.play()
        pygame.display.flip()
        init_pos_x += 18
    disp_dialog_pause(screen)
        
                        
