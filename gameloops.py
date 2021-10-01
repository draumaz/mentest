import pygame, time, sys
from dialogdisp import disp_dialog
from backend import savesys, text_colors, screen_fade
import loops

def test_board2_collision(x, y, key):
    v = 0
    if key == "left":
        if x == 280 and y >= -10 and y <= 170:
            v = 0
        elif x == 225 and y >= 295 and y <= 320:
            v = 0
        elif x == 225 and y >= 150 and y <= 230:
            v = 0
        else:
            v = 5
    if key == "right":
        if x == 340 and y >= -10 and y <= 155:
            v = 0
        else:
            v = 5
    if key == "down":
        if y == 170 and x >= 220 and x <= 280:
            v = 0
        
        else:
            v = 5
    if key == "up":
        if y >= 308 and x >= 220 and x <= 390:
            v = 0
        else:
            v = 5
    return v

def test_board2_refresh(screen, img, x, y): # Refresh sprite positions and flip display
    screen.blit(pygame.image.load("./lib/img/ovr_base2.png"),(0,0))
    screen.blit(pygame.image.load("./lib/spr/spr_saveemblem.png"),(-5, 255))
    #screen.blit(pygame.image.load('./lib/spr/spr_player.png'),(610,190))
    #screen.blit(pygame.image.load('./lib/spr/spr_player.png'),(290,110))
    screen.blit(pygame.image.load(img),(x,y))
    pygame.display.flip()

def test_board2(screen, x, y):
    game = True
    img = "./lib/spr/spr_ph_dwn1.png"
    spr1p = 0
    spr2p = 0
    loop = 0
    while game:
        pygame.time.delay(30)
        pygame.event.get()
        k = pygame.key.get_pressed()
        if x >= 280 and y <= -10:
            test_board(screen, 310, 400)
        if k[pygame.K_RETURN] or k[pygame.K_KP_ENTER]:
            if x == 230 and y == 230 and spr1p > 0 and spr2p > 0:
                disp_dialog(screen, "im a secret (:", 0.05, 20, 300)
                test_board2_refresh(screen, img, x, y)
                pygame.time.delay(200)
            if x >= 10 and x <= 35 and y >= 250 and y <= 260:
                disp_dialog(screen, "Saving.", 0.05, 20, 300)
                test_board2_refresh(screen, img, x, y)
                savesys.write(1, 1)
                savesys.write(2, x)
                savesys.write(3, y)
                pygame.time.delay(200)
        if k[pygame.K_LEFT] or k[pygame.K_a]:
            if loop % 10 == 0:
                img = "./lib/spr/spr_ph_lft2.png"
            else:
                img = "./lib/spr/spr_ph_lft1.png"
            x -= test_board2_collision(x, y, "left")
        if k[pygame.K_RIGHT] or k[pygame.K_d]:
            if loop % 10 == 0:
                img = "./lib/spr/spr_ph_rght2.png"
            else:
                img = "./lib/spr/spr_ph_rght1.png"
            x += test_board2_collision(x, y, "right")
        if k[pygame.K_UP] or k[pygame.K_w]:
            if loop % 10 == 0:
                img = "./lib/spr/spr_ph_up2.png"
            else:
                img = "./lib/spr/spr_ph_up1.png"
            y -= test_board2_collision(x, y, "down")
        if k[pygame.K_DOWN] or k[pygame.K_s]:
            if loop % 10 == 0:
                img = "./lib/spr/spr_ph_dwn2.png"
            else:
                img = "./lib/spr/spr_ph_dwn1.png"
            y += test_board2_collision(x, y, "up")
        print(x,y)
        test_board2_refresh(screen, img, x, y)
        loop += 1

def test_board_refresh(screen, img, x, y): # Refresh sprite positions and flip display
    screen.blit(pygame.image.load("./lib/img/ovr_base1.png"),(0,0))
    screen.blit(pygame.image.load('./lib/spr/spr_player.png'),(610,190))
    screen.blit(pygame.image.load('./lib/spr/spr_player.png'),(290,110))
    screen.blit(pygame.image.load(img),(x,y))
    pygame.display.flip()

def test_board_collision(x, y, key): # Rudimentary collision physics
    v = 0
    if key == "left":
        if x == -10 and y <= 185 and y >= -10:
            v = 0
        elif x == 225 and y >= 115 and y <= 130:
            v = 0
        elif y >= 185 and y <= 275 and x == 225:
            v = 0
        elif x == 280 and y >= 270 and y <= 440:
            v = 0
        else:
            v = 5
    elif key == "right":
        if x == 50 and y <= 135 and y >= -10:
            v = 0
        elif x == 390 and y >= 115 and y <= 175:
            v = 0
        elif x == 395 and y >= 225 and y <= 260:
            v = 0
        elif x == 340 and y >= 270 and y <= 440:
            v = 0
        elif x == 600 and y >= 185:
            v = 0
        else:
            v = 5
    elif key == "up":
        if y == -10 and x >= -10 and x <= 50:
            v = 0
        elif y == 135 and x >= 60 and x <= 220:
            v = 0
        elif y == 115 and x >= 225 and x <= 395:
            v = 0
        elif y == 185 and x >= 395 and x <= 600:
            v = 0
        else:
            v = 5
    elif key == "down":
        if y == 185 and x <= 225 and x >= -10:
            v = 0
        elif x >= 225 and x <= 280 and y == 265:
            v = 0
        elif x >= 340 and x <= 395 and y == 260:
            v = 0
        elif y == 215 and x >= 395 and x <= 600:
            v = 0
        elif y == 435 and x >= 280:
            v = 0
        else:
            v = 5
    return v

def test_board(screen, x, y):
    game = True
    img = "./lib/spr/spr_ph_dwn1.png"
    spr1p = 0
    spr2p = 0
    loop = 0
    while game:   
        if x >= 280 and y >= 425:
            test_board2(screen, 310, 20) #pass # next world portal
        pygame.time.delay(30)
        pygame.event.get()
        k = pygame.key.get_pressed()
        if k[pygame.K_RETURN] or k[pygame.K_KP_ENTER]:
            if x == 230 and y == 230 and spr1p > 0 and spr2p > 0:
                disp_dialog(screen, "im a secret (:", 0.05, 20, 300)
                test_board_refresh(screen, img, x, y)
                pygame.time.delay(200)
            if x >= 440 and x <= 460 and y <= 0:
                disp_dialog(screen, "how did you get here?", 0.05, 20, 300)
                test_board_refresh(screen, img, x, y)
                pygame.time.delay(200)
            if x >= 570 and x <= 590 and y >= 190 and y <= 210:
                disp_dialog(screen, "hey man, this is all.", 0.05, 20, 300)
                test_board_refresh(screen, img, x, y)
                disp_dialog(screen, "more will come in time...", 0.05, 20, 300)
                test_board_refresh(screen, img, x, y)
                disp_dialog(screen, "also, the name's stickman.", 0.05, 20, 300)
                test_board_refresh(screen, img, x, y)
                spr1p += 1
                pygame.time.delay(200)
            if x >= 200 and x <= 300 and y >= 120 and y <= 150:
                disp_dialog(screen, "hey, pal!", 0.05, 20, 300)
                test_board_refresh(screen, img, x, y)
                disp_dialog(screen, "i am the great stickington.", 0.05, 20, 300)
                test_board_refresh(screen, img, x, y)
                spr2p += 1
                pygame.time.delay(200)
        if k[pygame.K_LEFT] or k[pygame.K_a]:
            if loop % 10 == 0:
                img = "./lib/spr/spr_ph_lft2.png"
            else:
                img = "./lib/spr/spr_ph_lft1.png"
            x -= test_board_collision(x,y,"left")
        if k[pygame.K_RIGHT] or k[pygame.K_d]:
            if loop % 10 == 0:
                img = "./lib/spr/spr_ph_rght2.png"
            else:
                img = "./lib/spr/spr_ph_rght1.png"
            x += test_board_collision(x,y,"right")
        if k[pygame.K_UP] or k[pygame.K_w]:
            if loop % 10 == 0:
                img = "./lib/spr/spr_ph_up2.png"
            else:
                img = "./lib/spr/spr_ph_up1.png"
            y -= test_board_collision(x,y,"up")
        if k[pygame.K_DOWN] or k[pygame.K_s]:
            if loop % 10 == 0:
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

def splash_loop_selector(screen):
    l = True
    x = 0
    while l:
        x = splash_loop(screen, x)
        if x == 0:
            continue
        elif x == 1:
            pygame.mixer.music.load("./lib/snd/snd_menuselect.ogg")
            pygame.mixer.music.play()
            pygame.time.delay(200)
            if savesys.read()[1] == 0: # No save
                loops.board_roomone(screen, 300,200)
            elif savesys.read()[1] == 1: # Stars save
                loops.board_roomtwo(screen, savesys.read()[2], savesys.read()[3])
        elif x == 2:
            pygame.mixer.music.load("./lib/snd/snd_quit.ogg")
            pygame.mixer.music.play()
            time.sleep(0.17)
            sys.exit()

def WIP_loop(screen):
    pygame.event.get()
    screen_fade(screen, 0, 256, 0.0035, False)
    d = ["...", "You're here early.", "This game's not quite ready.", "The graphics suck, but...", "Here's what I've got!"]
    x = [0.05, 0.05, 0.05, 0.05, 0.05]
    for i in range(0, len(d)):
        time.sleep(0.15)
        disp_dialog(screen, d[i], x[i], 20, 300)
    savesys.write(0,1)
