import pygame,sys
from pygame.locals import *
from Menu import *
BLACK = (0,0,0)
pygame.init()
while_1 = True
while while_1:
    while puntuacion<60:
        menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                while_1 = False
                pygame.quit()
                sys.exit()
        pygame.display.flip()