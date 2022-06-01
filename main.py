import pygame
import sys
from pygame.color import THECOLORS

pygame.init()
# создание экрана
screen = pygame.display.set_mode((1200, 800))
image = pygame.image.load("bin/03.png")
pygame.display.set_caption("my game")
bg = pygame.image.load("bin/05.png")
bg = pygame.transform.scale(bg, (1200, 800))

screen.blit(bg, (20,20))
image = pygame.transform.scale(image, (230, 230))
screen.blit(image, (20,20))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.flip()
