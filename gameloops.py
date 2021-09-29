import pygame, time, sys
from dialogdisp import disp_dialog
from backend import write, text_colors, screen_clear, screen_fade

def test_board_refresh(screen, img, x, y):
    screen.blit(pygame.image.load("./lib/img/ovr_base1.png"),(0,0))
    screen.blit(pygame.image.load('./lib/spr/spr_player.png'),(610,190))
    screen.blit(pygame.image.load('./lib/spr/spr_player.png'),(290,110))
    screen.blit(pygame.image.load(img),(x,y))
    pygame.display.flip()

def test_board_collision(x, y, key):
    v = 0
    if key == "left":
        if y >= -10 and y <= 190 and x == -10:
            v = 0
        elif y >= 210 and y <= 250 and x == 230:
            v = 0
        elif x == 230 and y == 110:
            v = 0
        else:
            v = 5
    elif key == "right":
        if y >= -10 and y <= 110 and x == 50:
            v = 0
        elif y >= 230 and y <= 250 and x == 390:
            v = 0
        elif y >= 110 and y <= 150 and x == 390:
            v = 0
        elif x >= 590 and y >= 170 and y <= 210:
            v = 0
        else:
            v = 5
    elif key == "up":
        if x >= -10 and x <= 50 and y == -10:
            v = 0
        elif x >= 70 and x <= 210 and y == 130:
            v = 0
        elif x >= 230 and x <= 390 and y == 110:
            v = 0
        elif x >= 410 and x <= 590 and y == 170:
            v = 0
        else:
            v = 5
    elif key == "down":
        if x >= -10 and x <= 210 and y == 190:
            v = 0
        elif x >= 230 and x <= 390 and y == 250:
            v = 0
        elif x >= 410 and x <= 590 and y == 210:
            v = 0
        else:
            v = 5
    return v

def test_board(screen):
    game = True
    img = "./lib/spr/spr_ph_dwn1.png"
    spr1p = 0
    spr2p = 0
    x = 30
    y = 30
    loop = 0
    while game:   
        pygame.time.delay(30)
        pygame.event.get()
        k = pygame.key.get_pressed()
        if k[pygame.K_RETURN] or k[pygame.K_KP_ENTER]:
            if x == 230 and y == 230 and spr1p > 0 and spr2p > 0:
                disp_dialog(screen, "im a secret (:", 0.05, 20, 300)
                test_board_refresh(screen, img, x, y)
            if x >= 570 and x <= 590 and y == 190:
                disp_dialog(screen, "hey man, this is all.", 0.05, 20, 300)
                test_board_refresh(screen, img, x, y)
                disp_dialog(screen, "more will come in time...", 0.05, 20, 300)
                test_board_refresh(screen, img, x, y)
                disp_dialog(screen, "also, the name's stickman.", 0.05, 20, 300)
                test_board_refresh(screen, img, x, y)
                spr1p += 1
                pygame.time.delay(40)
            if x == 290 and y >= 130 and y <= 150:
                disp_dialog(screen, "hey, pal!", 0.05, 20, 300)
                test_board_refresh(screen, img, x, y)
                disp_dialog(screen, "i am the great stickington.", 0.05, 20, 300)
                test_board_refresh(screen, img, x, y)
                spr2p += 1
                pygame.time.delay(40)
            continue
        if k[pygame.K_LEFT] or k[pygame.K_a]:
            if loop % 8 == 0:
                img = "./lib/spr/spr_ph_lft2.png"
            else:
                img = "./lib/spr/spr_ph_lft1.png"
            x -= test_board_collision(x,y,"left")
        if k[pygame.K_RIGHT] or k[pygame.K_d]:
            if loop % 8 == 0:
                img = "./lib/spr/spr_ph_rght2.png"
            else:
                img = "./lib/spr/spr_ph_rght1.png"
            x += test_board_collision(x,y,"right")
        if k[pygame.K_UP] or k[pygame.K_w]:
            if loop % 8 == 0:
                img = "./lib/spr/spr_ph_up2.png"
            else:
                img = "./lib/spr/spr_ph_up1.png"
            
            y -= test_board_collision(x,y,"up")
        if k[pygame.K_DOWN] or k[pygame.K_s]:
            if loop % 8 == 0:
                img = "./lib/spr/spr_ph_dwn2.png"
            else:
                img = "./lib/spr/spr_ph_dwn1.png"
            y += test_board_collision(x,y,"down")
        print(x,y)
        test_board_refresh(screen, img, x, y)
        loop += 1

def splash_loop_colorizer(screen, active_pos):
    screen.blit(pygame.font.SysFont("lucidasans", 35).render("PLAY", False, text_colors(active_pos)[1]), (70,370)) # Readying color switch when loop is reloaded
    screen.blit(pygame.font.SysFont("lucidasans", 35).render("QUIT", False, text_colors(active_pos)[0]), (470,370))
    
def splash_loop(screen, active_pos):
    screen.fill((000,000,000))
    screen.blit(pygame.image.load("./lib/img/img_logo.png"),(150,50))
    screen.blit(pygame.font.SysFont("lucidasans", 35).render("PLAY", False, text_colors(active_pos)[1]), (70,370)) # Text colors switch when function is reloaded
    screen.blit(pygame.font.SysFont("lucidasans", 35).render("QUIT", False, text_colors(active_pos)[0]), (470,370))
    pygame.display.flip()
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    return active_pos
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    pygame.mixer.music.load("./lib/snd/snd_menuinteract.ogg")
                    pygame.mixer.music.play()
                    if active_pos == 0 or active_pos == 2: # Color redirectors
                        active_pos = 1
                    elif active_pos == 1:
                        active_pos = 2
                    splash_loop_colorizer(screen, active_pos)
                    pygame.display.flip() # Flip display
                    continue # Reload loop
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    pygame.mixer.music.load("./lib/snd/snd_menuinteract.ogg")
                    pygame.mixer.music.play()
                    if active_pos == 0 or active_pos == 1:
                        active_pos = 2
                    elif active_pos == 2:
                        active_pos = 1
                    splash_loop_colorizer(screen, active_pos)
                    pygame.display.flip()
                    continue

def splash_loop_selector(screen, active_pos):
    l = True
    x = 0
    while l:
        x = splash_loop(screen, x)
        if x == 0:
            continue
        elif x == 1:
            pygame.mixer.music.load("./lib/snd/snd_menuselect.ogg")
            pygame.mixer.music.play()
            test_board(screen)
            #screen_clear(screen, (000,000,000)) # Draws over display with given color
            #disp_dialog(screen, "Not yet ready!", 0.05, 20, 300) # Feed sleep float and x,y init coords
            #screen_clear(screen, (000,000,000))
            #continue
        elif x == 2:
            pygame.mixer.music.load("./lib/snd/snd_quit.ogg")
            pygame.mixer.music.play()
            time.sleep(0.17)
            sys.exit()

def WIP_loop(screen):
    screen_fade(screen, 0, 256, 0.0035, False)
    d = ["...", "You're here early.", "This game's not quite ready.", "...", "Come check out this menu."]
    x = [0.05, 0.05, 0.05, 0.25, 0.05]
    for i in range(0, len(d)):
        time.sleep(0.15)
        disp_dialog(screen, d[i], x[i], 20, 300)
    write(0,1)