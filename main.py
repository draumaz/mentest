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
    

def main_menu():
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("mentest")
    #pygame.display.set_icon(pygame.image.load("./lib/img/icon.png")),(0,0)
    screen.fill((000,000,000))
    screen.blit(pygame.image.load("./lib/img/logo.png"),(160,50))
    screen.blit(text_cook("Comic Sans MS", 30, "PLAY", "white"),(100,350))
    screen.blit(text_cook("Comic Sans MS", 30, "OPTIONS", "white"),(400,350))
    pygame.display.flip()

def const_hold():
    screen.blit(pygame.image.load("./lib/img/ovr_const.png"),(0,-160))
    pygame.display.flip()
    time.sleep(2)
    main_menu()

def main():
    main_menu()
    ms = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if ms == 1:
                        pygame.mixer.music.load(snd_press())
                        pygame.mixer.music.play()
                        print("Play select")
                        const_hold()
                    elif ms == 2:
                        pygame.mixer.music.load(snd_press())
                        pygame.mixer.music.play()
                        print("Options select")
                        const_hold()
                if event.key == pygame.K_LEFT:
                    screen.blit(text_cook("Comic Sans MS", 30, "OPTIONS", "white"),(400,350))
                    screen.blit(text_cook("Comic Sans MS", 30, "PLAY", "gray"),(100,350))
                    ms = 1
                    pygame.display.flip()
                if event.key == pygame.K_RIGHT:
                    screen.blit(text_cook("Comic Sans MS", 30, "OPTIONS", "gray"),(400,350))
                    screen.blit(text_cook("Comic Sans MS", 30, "PLAY", "white"),(100,350))
                    ms = 2
                    pygame.display.flip()

screen = screen_res(640,480)
if __name__ == "__main__":
    main()
