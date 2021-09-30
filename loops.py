import pygame
from dialogdisp import disp_dialog
from backend import savesys

def board_roomtwo_collision(x, y, key):
    if key == "left":
        if x <= -5 and y >= 185 and y <= 225:
            v = 0
        elif x <= 265 and y >= 230 and y <= 440:
            v = 0
        else:
            v = 5
    if key == "up":
        if y <= 185 and x >= 0 and x <= 620:
            v = 0
        else:
            v = 5
    if key == "down":
        if y >= 225 and x >= 0 and x <= 260 or y >= 225 and x >= 350 and x <= 620:
            v = 0
        elif y >= 440 and x >= 265 and x <= 345:
            v = 0
        else:
            v = 5
    if key == "right":
        if x >= 620 and y >= 185 and y <= 620:
            v = 0
        elif x >= 345 and y >= 230 and y <= 440:
            v = 0
        else:
            v = 5
    return v

def board_roomtwo_refresh(screen, img, x, y, loop):
    screen.blit(pygame.image.load("./lib/img/br2.png"), (0,0))
    if loop > 31 and loop < 61:
        screen.blit(pygame.image.load("./lib/img/br2_bright.png"),(0,0))
    screen.blit(pygame.image.load(img),(x,y))
    pygame.display.flip()

def board_roomtwo(screen, x, y):
    game = True
    img = './lib/spr/spr_ph_dwn1.png'
    loop = 0
    loop2 = 0
    while game:
        if loop > 60:
            loop = 0
        if loop2 > 60:
            loop2 = 0
        pygame.time.delay(30)
        pygame.event.get()
        k = pygame.key.get_pressed()
        if x == 0 and y >= 185 and y <= 225:
            board_roomone(screen, 590, 200)
        elif k[pygame.K_RETURN ] or k[pygame.K_KP_ENTER]:
            if x >= 290 and x <= 320 and y >= 185 and y <= 195:
                disp_dialog(screen, "You stare at the stars...", 0.05, 20, 300)
                board_roomtwo_refresh(screen, img, x, y, loop2)
                disp_dialog(screen, "You feel like...", 0.05, 20, 300)
                board_roomtwo_refresh(screen, img, x, y, loop2)
                disp_dialog(screen, "...everything'll be OK.", 0.05, 20, 300)
                board_roomtwo_refresh(screen, img, x, y, loop2)
                savesys.write(1, 1)
                savesys.write(2, x)
                savesys.write(3, y)
                disp_dialog(screen, "Your game has been saved.", 0.025, 20, 300)
                board_roomtwo_refresh(screen, img, x, y, loop2)
                pygame.time.delay(200)
        elif k[pygame.K_LEFT] or k[pygame.K_a]:
            if loop >= 0 and loop <= 15 or loop >= 30 and loop <= 45:
                img = "./lib/spr/spr_ph_lft2.png"
            else:
                img = "./lib/spr/spr_ph_lft1.png"
            x -= board_roomtwo_collision(x, y, "left")
        elif k[pygame.K_RIGHT] or k[pygame.K_d]:
            if loop >= 0 and loop <= 15 or loop >= 30 and loop <= 45:
                img = "./lib/spr/spr_ph_rght2.png"
            else:
                img = "./lib/spr/spr_ph_rght1.png"
            x += board_roomtwo_collision(x, y, "right")
        elif k[pygame.K_UP] or k[pygame.K_w]:
            if loop >= 0 and loop <= 15 or loop >= 30 and loop <= 45:
                img = "./lib/spr/spr_ph_up2.png" 
            else:
                img = "./lib/spr/spr_ph_up1.png"
            y -= board_roomtwo_collision(x, y, "up")
        elif k[pygame.K_DOWN] or k[pygame.K_s]:
            if loop >= 0 and loop <= 15 or loop >= 30 and loop <= 45:
                img = "./lib/spr/spr_ph_dwn2.png"
            else:
                img = "./lib/spr/spr_ph_dwn1.png"
            y += board_roomtwo_collision(x, y, "down")
        else:
            loop = 0
        print(x,y)
        board_roomtwo_refresh(screen, img, x, y, loop2)
        loop += 1
        loop2 += 1

def board_roomone_collision(x, y, dir):
    if dir == "left":
        if x <= 40 and y >= 20 and y <= 405:
            v = 0
        else:
            v = 5
    if dir == "right":
        if x >= 575 and y >= 20 and y <= 170:
            v = 0
        elif x >= 575 and y >= 230 and y <= 400:
            v = 0
        elif x >= 610 and y >= 190 and y <= 225:
            v = 0
        else:
            v = 5
    if dir == "up":
        if y <= 20 and x >= 30 and x <= 580:
            v = 0
        elif y <= 190 and x >= 580 and x <= 620:
            v = 0
        else:
            v = 5
    if dir == "down":
        if y >= 225 and x >= 580 and x <= 620:
            v = 0
        elif y >= 405 and x <= 580 and x >= 30:
            v = 0
        else:
            v = 5
    return v

def board_roomone_refresh(screen, img, x, y):
    screen.blit(pygame.image.load("./lib/img/br1.png"), (0,0))
    screen.blit(pygame.image.load(img),(x,y))
    pygame.display.flip()

def board_roomone(screen, x, y):
    game = True
    img = './lib/spr/spr_ph_dwn1.png'
    loop = 0
    while game:
        if loop > 60:
            loop = 0
        pygame.time.delay(30)
        pygame.event.get()
        k = pygame.key.get_pressed()
        if x >= 600 and y >= 190 and y <= 225:
            board_roomtwo(screen, 30, 200)
        elif k[pygame.K_RETURN] or k[pygame.K_KP_ENTER]:
            pass
        elif k[pygame.K_LEFT] or k[pygame.K_a]:
            if loop >= 0 and loop <= 15 or loop >= 30 and loop <= 45:
                img = "./lib/spr/spr_ph_lft2.png"
            else:
                img = "./lib/spr/spr_ph_lft1.png"
            x -= board_roomone_collision(x, y, "left")
        elif k[pygame.K_RIGHT] or k[pygame.K_d]:
            if loop >= 0 and loop <= 15 or loop >= 30 and loop <= 45:
                img = "./lib/spr/spr_ph_rght2.png"
            else:
                img = "./lib/spr/spr_ph_rght1.png"
            x += board_roomone_collision(x, y, "right")
        elif k[pygame.K_UP] or k[pygame.K_w]:
            if loop >= 0 and loop <= 15 or loop >= 30 and loop <= 45:
                img = "./lib/spr/spr_ph_up2.png"
            else:
                img = "./lib/spr/spr_ph_up1.png"
            y -= board_roomone_collision(x, y, "up")
        elif k[pygame.K_DOWN] or k[pygame.K_s]:
            if loop >= 0 and loop <= 15 or loop >= 30 and loop <= 45:
                img = "./lib/spr/spr_ph_dwn2.png"
            else:
                img = "./lib/spr/spr_ph_dwn1.png"
            y += board_roomone_collision(x, y, "down")
        else:
            loop = 0
        print(x,y)
        board_roomone_refresh(screen, img, x, y)
        loop += 1