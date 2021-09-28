import pygame, time, sys
from dialogdisp import disp_dialog
from backend import write, text_colors

def splash_loop(screen, active_pos):
    screen.fill((000,000,000))
    screen.blit(pygame.image.load("./lib/img/img_logo.png"),(150,50))
    screen.blit(pygame.font.SysFont("lucidasans", 35).render("PLAY", False, text_colors(active_pos)[1]), (70,370))
    screen.blit(pygame.font.SysFont("lucidasans", 35).render("QUIT", False, text_colors(active_pos)[0]), (470,370))
    pygame.display.flip()
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:   
                    if active_pos == 0:
                        pass
                    if active_pos == 1:
                        disp_dialog(screen, (000,000,000), "Not yet ready!", 0.05, 20, 300)
                        splash_loop(screen, active_pos)
                    if active_pos == 2:
                        sys.exit()
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if active_pos == 0 or active_pos == 2:
                        active_pos = 1
                    elif active_pos == 1:
                        active_pos = 2
                    splash_loop(screen, active_pos)
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if active_pos == 0 or active_pos == 1:
                        active_pos = 2
                    elif active_pos == 2:
                        active_pos = 1
                    splash_loop(screen, active_pos)

def WIP_loop(screen):
    for i in range(0, 256):
        screen.fill((i,i,i))
        time.sleep(0.0035)
        pygame.display.flip()
    d = ["...", "You're here early.", "This game's not quite ready.", "...", "Come check out this menu."]
    x = [0.05, 0.05, 0.05, 0.25, 0.05]
    for i in range(0, len(d)):
        time.sleep(0.15)
        disp_dialog(screen, (255,255,255), d[i], x[i], 20, 300)
    write(0,1)