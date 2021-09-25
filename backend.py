import pygame, random, time

def cook_strs(ps):
    if ps == 0:
        tx0 = "white"
        tx1 = "white"
    elif ps == 1:
        tx0 = "gray"
        tx1 = "white"
    elif ps == 2:
        tx0 = "white"
        tx1 = "gray"
    elif ps == 3:
        tx0 = "gray"
        tx1 = "white"
    return tx0,tx1

def text_cook(font, size, text, color):
    if color == "black":
        d = (000,000,000)
    elif color == "white":
        d = (255,255,255)
    elif color == "gray":
        d = (128,128,128)
    return pygame.font.SysFont(str(font), int(size)).render(str(text),False,(d))

def screen_res(x,y):
    wdh = x
    hgt = y
    return pygame.display.set_mode((wdh,hgt))

def snd_press():
    s = "./lib/snd/"
    i = random.randint(0, 1)
    if i == 0:
        s += "snd_vthud.ogg"
    elif i == 1:
        s += "snd_bruh.ogg"
    return s

def const_hold(screen):
    screen.blit(pygame.image.load("./lib/img/ovr_const.png"),(0,-160))
    pygame.display.flip()
    time.sleep(2)

def opt_swap(play_clr, opt_clr, screen):
    screen.blit(text_cook("Comic Sans MS", 30, "OPTIONS", opt_clr),(400,350))
    screen.blit(text_cook("Comic Sans MS", 30, "PLAY", play_clr),(100,350))
    if play_clr == "white" and opt_clr == "gray":
        return 2
    elif play_clr == "gray" and opt_clr == "white":
        return 1
