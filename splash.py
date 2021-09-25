import pygame
from backend import text_cook, cook_strs

def main_menu(ps, screen):
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("mentest")
    #pygame.display.set_icon(pygame.image.load("./lib/img/icon.png")),(0,0)
    screen.fill((000,000,000))
    screen.blit(pygame.image.load("./lib/img/logo.png"),(160,50))
    screen.blit(text_cook("Comic Sans MS", 30, "PLAY", cook_strs(ps)[0]),(100,350))
    screen.blit(text_cook("Comic Sans MS", 30, "OPTIONS", cook_strs(ps)[1]),(400,350))
    pygame.display.flip()