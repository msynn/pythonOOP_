import pygame, sys, time, random

# check error game
check_errors = pygame.init()
if check_errors[1] > 0:
    print('(!) Had {check errors} error game')
else :
    print('(+) Game successfully isntall')
    
# set up game window #
size_x = 720
size_y = 480
# tittle game
pygame.display.set_caption('My snake')
pygame.display.set_mode((size_x, size_y))