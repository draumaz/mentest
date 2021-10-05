import pygame, sys, time
from pygame.constants import QUIT
from dialogdisp import disp_dialog
from backend import savesys, text_colors_trip, screen_fade

class room_two():
    def collision(x, y, key):
        if key == "left":
            if x <= -5 and y >= 185 and y <= 225:
                v = False
            elif x <= 268 and y >= 230 and y <= 440:
                v = False
            elif x <= 330 and x >= 290 and y >= 180 and y <= 190:
                v = False
            else:
                v = True
        if key == "up":
            if y <= 185 and x >= 0 and x <= 620:
                v = False
            elif x >= 290 and x <= 320 and y <= 200:
                v = False
            else:
                v = True
        if key == "down":
            if y >= 225 and x >= 0 and x <= 260:
                v = False
            elif y >= 225 and x >= 350 and x <= 630:
                v = False
            elif y >= 430 and x >= 265 and x <= 345:
                v = False
            else:
                v = True
        if key == "right":
            if x >= 618 and y >= 180 and y <= 228:
                v = False
            elif x >= 342 and y >= 230 and y <= 440:
                v = False
            elif x >= 280 and x <= 290 and y >= 180 and y <= 200:
                v = False
            else:
                v = True
        if v == True:
            return 10
        elif v == False:
            return 0
    def refresh(screen, img, x, y, loop):
        screen.blit(pygame.image.load("./lib/img/br2.png"), (0,0))
        if loop > 59 and loop < 91:
            screen.blit(pygame.image.load("./lib/img/br2_bright.png"),(0,0))
        screen.blit(pygame.image.load("./lib/spr/spr_saveemblem.png"),(300,175))
        screen.blit(pygame.image.load(img),(x,y))
        pygame.display.flip()
    def events(k, screen, img, loop, loop2, x, y, clock):
        tck = clock.tick(60) / 75
        if k[pygame.K_ESCAPE]:
            pygame.time.delay(100)
            splash.board(screen)
        elif k[pygame.K_RETURN] or k[pygame.K_KP_ENTER]:
            if x >= 270 and x <= 340 and y >= 185 and y <= 215:
                if savesys.read()[1] == 0:
                    h = [
                        "You stare at the stars...", 
                        "You feel like...", 
                        "...everything'll be okay.", 
                        "Your game has been saved."
                    ]
                    b = [1, round(x), round(y)]
                    for k in range(0,len(h)):
                        if k == 3:
                            for n in range(1,len(h)):
                                savesys.write(n, b[n-1])
                        disp_dialog(screen, h[k], 0.05, 20, 300)
                        room_two.refresh(screen, img, x, y, loop2)
                else:
                    b = [round(x), round(y)]
                    for n in range(0, len(b)):
                        savesys.write(n+2, b[n])
                    disp_dialog(screen, "Your game has been saved.", 0.05, 20, 300)
                    room_two.refresh(screen, img, x, y, loop2)
                pygame.time.delay(100)
        elif k[pygame.K_LEFT] or k[pygame.K_a]:
            if k[pygame.K_UP] or k[pygame.K_w]:
                y -= room_two.collision(x, y, "up") * tck
            if k[pygame.K_DOWN] or k[pygame.K_s]:
                y += room_two.collision(x, y, "down") * tck
            if loop >= 0 and loop <= 15 or loop >= 30 and loop <= 45 or loop >= 60 and loop <= 75 or loop >= 90 and loop <= 105:
                img = "./lib/spr/spr_ph_lft2.png"
            else:
                img = "./lib/spr/spr_ph_lft1.png"
            x -= room_two.collision(x, y, "left") * tck
        elif k[pygame.K_RIGHT] or k[pygame.K_d]:
            if k[pygame.K_UP] or k[pygame.K_w]:
                y -= room_two.collision(x, y, "up") * tck
            if k[pygame.K_DOWN] or k[pygame.K_s]:
                y += room_two.collision(x, y, "down") * tck
            if loop >= 0 and loop <= 15 or loop >= 30 and loop <= 45 or loop >= 60 and loop <= 75 or loop >= 90 and loop <= 105:
                img = "./lib/spr/spr_ph_rght2.png"
            else:
                img = "./lib/spr/spr_ph_rght1.png"
            x += room_two.collision(x, y, "right") * tck
        elif k[pygame.K_UP] or k[pygame.K_w]:
            if loop >= 0 and loop <= 15 or loop >= 30 and loop <= 45 or loop >= 60 and loop <= 75 or loop >= 90 and loop <= 105:
                img = "./lib/spr/spr_ph_up2.png" 
            else:
                img = "./lib/spr/spr_ph_up1.png"
            y -= room_two.collision(x, y, "up") * tck
        elif k[pygame.K_DOWN] or k[pygame.K_s]:
            if loop >= 0 and loop <= 15 or loop >= 30 and loop <= 45 or loop >= 60 and loop <= 75 or loop >= 90 and loop <= 105:
                img = "./lib/spr/spr_ph_dwn2.png"
            else:
                img = "./lib/spr/spr_ph_dwn1.png"
            y += room_two.collision(x, y, "down") * tck
        else:
            loop = 0
        return [loop,loop2,img,x,y]
    def board(screen, x, y):
        game = True
        img = './lib/spr/spr_ph_dwn1.png'
        loop = 0
        loop2 = 0
        clock = pygame.time.Clock()
        while game:
            if loop > 120:
                loop = 0
            if loop2 > 120:
                loop2 = 0
            pygame.event.get()
            k = pygame.key.get_pressed()
            if x <= 10 and y >= 180 and y <= 226:
                room_one.board(screen, 590, y)
            events = room_two.events(k, screen, img, loop, loop2, x, y, clock)
            loop = events[0]
            loop2 = events[1]
            img = events[2]
            x = events[3]
            y = events[4]
            room_two.refresh(screen, img, x, y, loop2)
            print(round(x),round(y))
            #print(loop,loop2)
            loop += 1
            loop2 += 1

class room_one():
    def collision(x, y, dir):
        if dir == "left":
            if x <= 40 and y >= 15 and y <= 407:
                v = False
            else:
                v = True
        if dir == "right":
            if x >= 575 and y >= 15 and y <= 185:
                v = False
            elif x >= 575 and y >= 230 and y <= 406:
                v = False
            elif x >= 610 and y >= 190 and y <= 225:
                v = False
            else:
                v = True
        if dir == "up":
            if y <= 18 and x >= 30 and x <= 580:
                v = False
            elif y <= 190 and x >= 580 and x <= 620:
                v = False
            else:
                v = True
        if dir == "down":
            if y >= 225 and x >= 580 and x <= 620:
                v = False
            elif y >= 405 and x <= 580 and x >= 30:
                v = False
            else:
                v = True
        if v == True:
            return 10
        elif v == False:
            return 0
    def refresh(screen, img, x, y):
        screen.blit(pygame.image.load("./lib/img/br1.png"), (0,0))
        screen.blit(pygame.image.load(img),(x,y))
        pygame.display.flip()
    def events(k, screen, loop, img, x, y, clock):
        tck = clock.tick(60) / 75
        if k[pygame.K_ESCAPE]:
            pygame.time.delay(100)
            splash.board(screen)
        elif k[pygame.K_LEFT] or k[pygame.K_a]:
            if k[pygame.K_UP] or k[pygame.K_w]:
                y -= room_one.collision(x, y, "up") * tck
            if k[pygame.K_DOWN] or k[pygame.K_s]:
                y += room_one.collision(x, y, "down") * tck
            if loop >= 0 and loop <= 15 or loop >= 30 and loop <= 45 or loop >= 60 and loop <= 75 or loop >= 90 and loop <= 105:
                img = "./lib/spr/spr_ph_lft2.png"
            else:
                img = "./lib/spr/spr_ph_lft1.png"
            x -= room_one.collision(x, y, "left") * tck
        elif k[pygame.K_RIGHT] or k[pygame.K_d]:
            if k[pygame.K_UP] or k[pygame.K_w]:
                y -= room_one.collision(x, y, "up") * tck
            if k[pygame.K_DOWN] or k[pygame.K_s]:
                y += room_one.collision(x, y, "down") * tck
            if loop >= 0 and loop <= 15 or loop >= 30 and loop <= 45 or loop >= 60 and loop <= 75 or loop >= 90 and loop <= 105:
                img = "./lib/spr/spr_ph_rght2.png"
            else:
                img = "./lib/spr/spr_ph_rght1.png"
            x += room_one.collision(x, y, "right") * tck
        elif k[pygame.K_UP] or k[pygame.K_w]:
            if loop >= 0 and loop <= 15 or loop >= 30 and loop <= 45 or loop >= 60 and loop <= 75 or loop >= 90 and loop <= 105:
                img = "./lib/spr/spr_ph_up2.png"
            else:
                img = "./lib/spr/spr_ph_up1.png"
            y -= room_one.collision(x, y, "up") * tck
        elif k[pygame.K_DOWN] or k[pygame.K_s]:
            if loop >= 0 and loop <= 15 or loop >= 30 and loop <= 45 or loop >= 60 and loop <= 75 or loop >= 90 and loop <= 105:
                img = "./lib/spr/spr_ph_dwn2.png"
            else:
                img = "./lib/spr/spr_ph_dwn1.png"
            y += room_one.collision(x, y, "down") * tck
        else:
            loop = 0
        return [loop,x,y,img]
    def board(screen, x, y):
        game = True
        img = './lib/spr/spr_ph_dwn1.png'
        loop = 0
        clock = pygame.time.Clock()
        while game:
            if loop > 120:
                loop = 0
            pygame.event.get()
            k = pygame.key.get_pressed()
            if x >= 600 and y >= 180 and y <= 225:
                room_two.board(screen, 30, y)
            events = room_one.events(k, screen, loop, img, x, y, clock)
            loop = events[0]            
            x = events[1]
            y = events[2]
            img = events[3]
            print(round(x),round(y))
            #print(loop)
            room_one.refresh(screen, img, x, y)
            loop += 1

class splash():
    def refresh(screen, active_pos):
        screen.fill((000,000,000))
        screen.blit(pygame.image.load("./lib/img/img_logo.png"),(150,50))
        h = ["PLAY", "FULLSCREEN", "QUIT"]
        b = [70, 210, 470]
        for i in range(0, 3):
            screen.blit(pygame.font.SysFont("lucidasans", 35).render(h[i], False, text_colors_trip(active_pos)[i]), (b[i],370)) # Text colors switch when function is reloaded
        pygame.display.flip()
    def events(screen, active_pos):
        loop = True
        while loop:
            pygame.event.get()
            k = pygame.key.get_pressed()
            if k[pygame.K_ESCAPE]:
                sys.exit()
            if k[pygame.K_RETURN] or k[pygame.K_KP_ENTER]:
                return active_pos
            if k[pygame.K_LEFT] or k[pygame.K_a]:
                pygame.mixer.music.load("./lib/snd/snd_menuinteract.ogg")
                pygame.mixer.music.play()
                if active_pos == 0:
                    active_pos = 1
                else:
                    active_pos -= 1
                    if active_pos < 1:
                        active_pos = 3
                splash.refresh(screen, active_pos)
                pygame.time.delay(150)
                continue # Reload loop
            if k[pygame.K_RIGHT] or k[pygame.K_d]:
                pygame.mixer.music.load("./lib/snd/snd_menuinteract.ogg")
                pygame.mixer.music.play()
                if active_pos == 0:
                    active_pos = 3
                else:
                    active_pos += 1
                    if active_pos > 3:
                        active_pos = 1
                splash.refresh(screen, active_pos)
                pygame.time.delay(150)
                continue
    def board(screen):
        l = True
        x = 0
        splash.refresh(screen, x)
        while l:
            x = splash.events(screen, x)
            if x == 0:
                continue
            elif x == 1:
                pygame.mixer.music.load("./lib/snd/snd_menuselect.ogg")
                pygame.mixer.music.play()
                pygame.time.delay(200)
                if savesys.read()[1] == 0: # No save
                    room_one.board(screen, 300,200)
                elif savesys.read()[1] == 1: # Stars save
                    room_two.board(screen, savesys.read()[2], savesys.read()[3])
            elif x == 2:
                pygame.mixer.music.load("./lib/snd/snd_menuselect.ogg")
                pygame.mixer.music.play()
                pygame.time.delay(200)
                if savesys.read()[4] == 0:
                    savesys.write(4,1)
                    screen = pygame.display.set_mode((640,480),pygame.FULLSCREEN)
                elif savesys.read()[4] == 1:
                    savesys.write(4,0)
                    screen = pygame.display.set_mode((640,480))
                continue
            elif x == 3:
                pygame.mixer.music.load("./lib/snd/snd_quit.ogg")
                pygame.mixer.music.play()
                time.sleep(0.17)
                sys.exit()

def WIP_loop(screen):
    pygame.event.get()
    screen_fade(screen, 0, 256, 0.0035, False)
    d = [
        "...",
        "You're here early.",
        "This game's not quite ready.",
        "The graphics suck, but...",
        "Here's what I've got!"
    ]
    x = [0.05, 0.05, 0.05, 0.05, 0.05]
    for i in range(0, len(d)):
        time.sleep(0.15)
        disp_dialog(screen, d[i], x[i], 20, 300)
    savesys.write(0,1)