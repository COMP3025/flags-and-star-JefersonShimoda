import sys

import pygame
from pygame.locals import QUIT

RED = (255, 0, 0)
AZUL = (13, 33, 79)
WHITE = (255, 255, 255)

pygame.init()
DISPLAYSURF = pygame.display.set_mode((500, 300))
pygame.display.set_caption('Reino Unido')

while True:
  DISPLAYSURF.fill(AZUL)

  pygame.draw.line(DISPLAYSURF, WHITE, (0, 0), (500, 300), 70) #X
  pygame.draw.line(DISPLAYSURF, WHITE, (0, 300), (500, 0), 70) #X

  pygame.draw.line(DISPLAYSURF, RED, (0, 0), (500, 300), 20) #X
  pygame.draw.line(DISPLAYSURF, RED, (0, 300), (500, 0), 20) #X
  # LINHAS BRANCAS
  pygame.draw.line(DISPLAYSURF, WHITE, (0, 150), (500, 150), 90) #HORIZONTAL
  pygame.draw.line(DISPLAYSURF, WHITE, (250, 0), (250, 300), 90) #VERTICAL
  
  # LINHAS VERMELHAS
  pygame.draw.line(DISPLAYSURF, RED, (0, 150), (500, 150), 55) #HORIZONTAL
  pygame.draw.line(DISPLAYSURF, RED, (250, 0), (250, 300), 55) #VERTICAL


  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

  pygame.display.update()
