import os, pygame
from backend import text_cook, cook_strs
from splash import main_menu

def option_menu(ps, screen, running):
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("mentest")
    screen.fill((000,000,000))
    screen.blit(text_cook("Comic Sans MS", 30, "mentest settings", "white"),(20,10))
    screen.blit(text_cook("Comic Sans MS", 30, "BACK", cook_strs(ps)[1]),(20,420))
    pygame.display.flip()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    running = False
                    main_menu(2, screen)
