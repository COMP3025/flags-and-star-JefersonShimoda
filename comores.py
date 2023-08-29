import sys

import pygame
from pygame.locals import QUIT

AMARELO = (255, 209, 0)
BRANCO = (255, 255, 255)
VERMELHO = (239, 51, 64)
AZUL = (0, 61, 165)
VERDE = (0, 151, 57)

pygame.init()
DISPLAYSURF = pygame.display.set_mode((350, 300))
pygame.display.set_caption('COMORES')
while True:
   pygame.draw.rect(DISPLAYSURF, AMARELO, pygame.Rect(0, 0, 400, 50))
   pygame.draw.rect(DISPLAYSURF, BRANCO, pygame.Rect(0, 50, 400, 50))
   pygame.draw.rect(DISPLAYSURF, VERMELHO, pygame.Rect(0, 100, 400, 50))
   pygame.draw.rect(DISPLAYSURF, AZUL, pygame.Rect(0, 150, 400, 50))
   pygame.draw.polygon(DISPLAYSURF, VERDE, [(0, 0), (100, 100), (0, 200)])
  
   for event in pygame.event.get():
       if event.type == QUIT:
           pygame.quit()
           sys.exit()
   pygame.display.update()