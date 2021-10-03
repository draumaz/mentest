import pygame, sys, time
from pygame.constants import QUIT
from dialogdisp import disp_dialog
from backend import savesys, text_colors, text_colors_trip, screen_fade

class room_two():
    def collision(x, y, key):
        if key == "left":
            if x <= -5 and y >= 185 and y <= 225:
                v = 0
            elif x <= 265 and y >= 230 and y <= 440:
                v = 0
            elif x <= 330 and x >= 290 and y >= 185 and y <= 190:
                v = 0
            else:
                v = 5
        if key == "up":
            if y <= 185 and x >= 0 and x <= 620:
                v = 0
            elif x >= 290 and x <= 320 and y <= 200:
                v = 0
            else:
                v = 5
        if key == "down":
            if y >= 225 and x >= 0 and x <= 260:
                v = 0
            elif y >= 225 and x >= 350 and x <= 620:
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
            elif x >= 285 and x <= 290 and y >= 185 and y <= 200:
                v = 0
            else:
                v = 5
        return v
    def refresh(screen, img, x, y, loop):
        screen.blit(pygame.image.load("./lib/img/br2.png"), (0,0))
        if loop > 31 and loop < 61:
            screen.blit(pygame.image.load("./lib/img/br2_bright.png"),(0,0))
        screen.blit(pygame.image.load("./lib/spr/spr_saveemblem.png"),(300,175))
        screen.blit(pygame.image.load(img),(x,y))
        pygame.display.flip()
    def events(k, screen, img, loop, loop2, x, y):
        if k[pygame.K_ESCAPE]:
            pygame.time.delay(100)
            splash.board(screen)
        elif k[pygame.K_RETURN] or k[pygame.K_KP_ENTER]:
            if x >= 270 and x <= 340 and y >= 185 and y <= 215:
                h = ["You stare at the stars...", "You feel like...", "...everything'll be okay.", "Your game has been saved."]
                for k in range(0,4):
                    print(k)
                    if k == 2:
                        savesys.write(1, 1)
                        savesys.write(2, x)
                        savesys.write(3, y)
                    disp_dialog(screen, h[k], 0.05, 20, 300)
                    room_two.refresh(screen, img, x, y, loop2)
                pygame.time.delay(200)
                room_two.board(screen, x, y)
        elif k[pygame.K_LEFT] or k[pygame.K_a]:
            if k[pygame.K_UP] or k[pygame.K_w]:
                y -= room_two.collision(x, y, "up")
            if k[pygame.K_DOWN] or k[pygame.K_s]:
                y += room_two.collision(x, y, "down")
            if loop >= 0 and loop <= 15 or loop >= 30 and loop <= 45:
                img = "./lib/spr/spr_ph_lft2.png"
            else:
                img = "./lib/spr/spr_ph_lft1.png"
            x -= room_two.collision(x, y, "left")
        elif k[pygame.K_RIGHT] or k[pygame.K_d]:
            if k[pygame.K_UP] or k[pygame.K_w]:
                y -= room_two.collision(x, y, "up")
            if k[pygame.K_DOWN] or k[pygame.K_s]:
                y += room_two.collision(x, y, "down")
            if loop >= 0 and loop <= 15 or loop >= 30 and loop <= 45:
                img = "./lib/spr/spr_ph_rght2.png"
            else:
                img = "./lib/spr/spr_ph_rght1.png"
            x += room_two.collision(x, y, "right")
        elif k[pygame.K_UP] or k[pygame.K_w]:
            if loop >= 0 and loop <= 15 or loop >= 30 and loop <= 45:
                img = "./lib/spr/spr_ph_up2.png" 
            else:
                img = "./lib/spr/spr_ph_up1.png"
            y -= room_two.collision(x, y, "up")
        elif k[pygame.K_DOWN] or k[pygame.K_s]:
            if loop >= 0 and loop <= 15 or loop >= 30 and loop <= 45:
                img = "./lib/spr/spr_ph_dwn2.png"
            else:
                img = "./lib/spr/spr_ph_dwn1.png"
            y += room_two.collision(x, y, "down")
        else:
            loop = 0
        return [loop,loop2,img,x,y]
    def board(screen, x, y):
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
                room_one.board(screen, 590, y)
            loop = room_two.events(k, screen, img, loop, loop2, x, y)[0]
            loop2 = room_two.events(k, screen, img, loop, loop2, x, y)[1]
            img = room_two.events(k, screen, img, loop, loop2, x, y)[2]
            x = room_two.events(k, screen, img, loop, loop2, x, y)[3]
            y = room_two.events(k, screen, img, loop, loop2, x, y)[4]
            room_two.refresh(screen, img, x, y, loop2)
            print(x,y)
            loop += 1
            loop2 += 1

class room_one():
    def collision(x, y, dir):
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
    def refresh(screen, img, x, y):
        screen.blit(pygame.image.load("./lib/img/br1.png"), (0,0))
        screen.blit(pygame.image.load(img),(x,y))
        pygame.display.flip()
    def events(k, screen, loop, img, x, y):
        if k[pygame.K_ESCAPE]:
            pygame.time.delay(100)
            splash.board(screen)
        elif k[pygame.K_LEFT] or k[pygame.K_a]:
            if k[pygame.K_UP] or k[pygame.K_w]:
                y -= room_one.collision(x, y, "up")
            if k[pygame.K_DOWN] or k[pygame.K_s]:
                y += room_one.collision(x, y, "down")
            if loop >= 0 and loop <= 15 or loop >= 30 and loop <= 45:
                img = "./lib/spr/spr_ph_lft2.png"
            else:
                img = "./lib/spr/spr_ph_lft1.png"
            x -= room_one.collision(x, y, "left")
        elif k[pygame.K_RIGHT] or k[pygame.K_d]:
            if k[pygame.K_UP] or k[pygame.K_w]:
                y -= room_one.collision(x, y, "up")
            if k[pygame.K_DOWN] or k[pygame.K_s]:
                y += room_one.collision(x, y, "down")
            if loop >= 0 and loop <= 15 or loop >= 30 and loop <= 45:
                img = "./lib/spr/spr_ph_rght2.png"
            else:
                img = "./lib/spr/spr_ph_rght1.png"
            x += room_one.collision(x, y, "right")
        elif k[pygame.K_UP] or k[pygame.K_w]:
            if loop >= 0 and loop <= 15 or loop >= 30 and loop <= 45:
                img = "./lib/spr/spr_ph_up2.png"
            else:
                img = "./lib/spr/spr_ph_up1.png"
            y -= room_one.collision(x, y, "up")
        elif k[pygame.K_DOWN] or k[pygame.K_s]:
            if loop >= 0 and loop <= 15 or loop >= 30 and loop <= 45:
                img = "./lib/spr/spr_ph_dwn2.png"
            else:
                img = "./lib/spr/spr_ph_dwn1.png"
            y += room_one.collision(x, y, "down")
        else:
            loop = 0
        return [loop,x,y,img]
    def board(screen, x, y):
        game = True
        img = './lib/spr/spr_ph_dwn1.png'
        loop = 0
        while game:
            if loop > 60:
                loop = 0
            pygame.time.delay(30)
            pygame.event.get()
            k = pygame.key.get_pressed()
            if x >= 600 and y >= 180 and y <= 225:
                room_two.board(screen, 30, 200)
            loop = room_one.events(k, screen, loop, img, x, y)[0]            
            x = room_one.events(k, screen, loop, img, x, y)[1]
            y = room_one.events(k, screen, loop, img, x, y)[2]
            img = room_one.events(k, screen, loop, img, x, y)[3]
            print(x,y)
            room_one.refresh(screen, img, x, y)
            loop += 1

class splash():
    def refresh(screen, active_pos):
        screen.fill((000,000,000))
        screen.blit(pygame.image.load("./lib/img/img_logo.png"),(150,50))
        screen.blit(pygame.font.SysFont("lucidasans", 35).render("PLAY", False, text_colors_trip(active_pos)[0]), (70,370)) # Text colors switch when function is reloaded
        screen.blit(pygame.font.SysFont("lucidasans", 35).render("FULLSCREEN", False, text_colors_trip(active_pos)[1]), (210,370))
        screen.blit(pygame.font.SysFont("lucidasans", 35).render("QUIT", False, text_colors_trip(active_pos)[2]), (470,370))
        pygame.display.flip()
    def events(screen, active_pos):
        (screen, active_pos)
        loop = True
        while loop:
            pygame.event.get()
            k = pygame.key.get_pressed()
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
                    screen = pygame.display.set_mode((640,480)) # Fullscreen
                continue
            elif x == 3:
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