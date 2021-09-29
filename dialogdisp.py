import pygame
import time

def disp_dialog_pause(screen):
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER: # Wait until user confirms to hide dialog panel
                    screen.fill((255,255,255))
                    screen.blit(pygame.image.load("./lib/img/img_dialog.png"), (0,0))
                    pygame.display.flip()
                    return 0
                else:
                    continue # If the key wasn't valid, don't do anything


def disp_dialog(screen, text, sleep_time, init_pos_x, init_pos_y):
    t = list(text) # Convert text into string array
    screen.blit(pygame.image.load("./lib/img/img_dialog.png"), (0,0))
    pygame.display.flip()
    pygame.mixer.init()
    pygame.font.init() 
    for i in range(0, len(t)):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == event.key == pygame.K_KP_ENTER or event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT: # If valid key is hit, skip LBL and print string immediately
                    sleep_time = 0
        screen.blit(pygame.font.SysFont("lucidasans", 25).render(t[i], False, (255,255,255)), (init_pos_x,init_pos_y)) # Loop print with x,y vars
        time.sleep(sleep_time)
        mus = "./lib/snd/"
        if sleep_time <= 0:
            mus += "snd_silence.ogg"
        else:
            mus += "snd_speech.ogg"
        pygame.mixer.music.load(mus)
        pygame.mixer.music.play()
        pygame.display.flip()
        init_pos_x += 21.5 # Modify x position for next loop
    disp_dialog_pause(screen)
        
                        
