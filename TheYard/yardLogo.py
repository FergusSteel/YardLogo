import pygame
import sys
from pygame.locals import *
from settings import settings
pygame.init()

#set up for scene objects
screen = pygame.display.set_mode((settings["screenX"], settings["screenY"]))
pygame.display.set_caption('The Yard')
fpsClock = pygame.time.Clock()


# Image Properties (actual image file and dimensions)
yardImage = pygame.image.load("TheYard.png")
yardImage = pygame.transform.scale(yardImage, (settings["dimensionX"], settings["dimensionY"]))
imgrect = yardImage.get_rect()



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    imgrect = imgrect.move(settings["speed"])
    if imgrect.left <= 0 or imgrect.right >= settings["screenX"]:
        settings["speed"][0] = -settings["speed"][0]
    if imgrect.top <= 0 or imgrect.bottom >= settings["screenY"]:
        settings["speed"][1] = -settings["speed"][1]

    screen.fill(settings["bgcolor"])
    screen.blit(pygame.transform.scale(yardImage, (settings["dimensionX"], settings["dimensionY"])), imgrect)
    pygame.display.flip()
    fpsClock.tick(settings["fps"])
