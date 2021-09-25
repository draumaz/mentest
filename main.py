import os, sys, pygame, random, time

def text_cook(font, size, text, color):
    if color == "black":
        d = (000, 000, 000)
    elif color == "white":
        d = (255, 255, 255)
    elif color == "gray":
        d = (128, 128, 128)
    return pygame.font.SysFont(str(font), int(size)).render(str(text), False, (d))

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
    

def main_menu(ps):
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
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("mentest")
    #pygame.display.set_icon(pygame.image.load("./lib/img/icon.png")),(0,0)
    screen.fill((000,000,000))
    screen.blit(pygame.image.load("./lib/img/logo.png"),(160,50))
    screen.blit(text_cook("Comic Sans MS", 30, "PLAY", tx0),(100,350))
    screen.blit(text_cook("Comic Sans MS", 30, "OPTIONS", tx1),(400,350))
    pygame.display.flip()

def const_hold(pi):
    screen.blit(pygame.image.load("./lib/img/ovr_const.png"),(0,-160))
    pygame.display.flip()
    time.sleep(2)
    main_menu(pi)

def opt_swap(play_clr, opt_clr):
    screen.blit(text_cook("Comic Sans MS", 30, "OPTIONS", opt_clr),(400,350))
    screen.blit(text_cook("Comic Sans MS", 30, "PLAY", play_clr),(100,350))
    if play_clr == "white" and opt_clr == "gray":
        return 2
    elif play_clr == "gray" and opt_clr == "white":
        return 1

def main():
    main_menu(0)
    ms = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    if ms == 1:
                        pygame.mixer.music.load(snd_press())
                        pygame.mixer.music.play()
                        print("Play select")
                        const_hold(ms)
                    elif ms == 2:
                        pygame.mixer.music.load(snd_press())
                        pygame.mixer.music.play()
                        print("Options select")
                        const_hold(ms)
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if ms == 1:
                        ms = opt_swap("white", "gray")
                    else:
                        ms = opt_swap("gray", "white")
                    pygame.display.flip()
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if ms == 2:
                        ms = opt_swap("gray", "white")
                    else:
                        ms = opt_swap("white", "gray")
                    pygame.display.flip()

screen = screen_res(640,480)
if __name__ == "__main__":
    main()
