import pygame

def board_roomtwo_collision(x, y, key):
    if key == "left":
        if x <= -5 and y >= 185 and y <= 225:
            v = 0
        else:
            v = 5
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
    while game:
        if loop > 60:
            loop = 0
        pygame.time.delay(30)
        pygame.event.get()
        k = pygame.key.get_pressed()
        if x == 0 and y >= 185 and y <= 225:
            board_roomone(screen, 590, 200)
        if k[pygame.K_RETURN ] or k[pygame.K_KP_ENTER]:
            pass
        if k[pygame.K_LEFT] or k[pygame.K_a]:
            if loop % 10 == 0:
                img = "./lib/spr/spr_ph_lft2.png"
            else:
                img = "./lib/spr/spr_ph_lft1.png"
            x -= board_roomtwo_collision(x, y, "left")
        if k[pygame.K_RIGHT] or k[pygame.K_d]:
            if loop % 10 == 0:
                img = "./lib/spr/spr_ph_rght2.png"
            else:
                img = "./lib/spr/spr_ph_rght1.png"
            x += board_roomtwo_collision(x, y, "right")
        if k[pygame.K_UP] or k[pygame.K_w]:
            if loop % 10 == 0:
                img = "./lib/spr/spr_ph_up2.png"
            else:
                img = "./lib/spr/spr_ph_up1.png"
            y -= board_roomtwo_collision(x, y, "up")
        if k[pygame.K_DOWN] or k[pygame.K_s]:
            if loop % 10 == 0:
                img = "./lib/spr/spr_ph_dwn2.png"
            else:
                img = "./lib/spr/spr_ph_dwn1.png"
            y += board_roomtwo_collision(x, y, "down")
        print(x,y)
        board_roomtwo_refresh(screen, img, x, y, loop)
        loop += 1

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
        pygame.time.delay(30)
        pygame.event.get()
        k = pygame.key.get_pressed()
        if x >= 600 and y >= 190 and y <= 225:
            board_roomtwo(screen, 30, 200)
        if k[pygame.K_RETURN] or k[pygame.K_KP_ENTER]:
            pass
        if k[pygame.K_LEFT] or k[pygame.K_a]:
            if loop % 10 == 0:
                img = "./lib/spr/spr_ph_lft2.png"
            else:
                img = "./lib/spr/spr_ph_lft1.png"
            x -= board_roomone_collision(x, y, "left")
        if k[pygame.K_RIGHT] or k[pygame.K_d]:
            if loop % 10 == 0:
                img = "./lib/spr/spr_ph_rght2.png"
            else:
                img = "./lib/spr/spr_ph_rght1.png"
            x += board_roomone_collision(x, y, "right")
        if k[pygame.K_UP] or k[pygame.K_w]:
            if loop % 10 == 0:
                img = "./lib/spr/spr_ph_up2.png"
            else:
                img = "./lib/spr/spr_ph_up1.png"
            y -= board_roomone_collision(x, y, "up")
        if k[pygame.K_DOWN] or k[pygame.K_s]:
            if loop % 10 == 0:
                img = "./lib/spr/spr_ph_dwn2.png"
            else:
                img = "./lib/spr/spr_ph_dwn1.png"
            y += board_roomone_collision(x, y, "down")
        print(x,y)
        board_roomone_refresh(screen, img, x, y)
        loop += 1