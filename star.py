import math
import sys

import pygame
from pygame.locals import QUIT

WHITE = (255, 255, 255)

pygame.init()
DISPLAYSURF = pygame.display.set_mode((500, 300))


def drawStar(screen, color, position, size, angle):
  points = []
  x, y = position

  for i in range(5):
    pointX = x - size * math.cos((2 * math.pi) * (i / 5) +
                                 (math.pi / 2) + angle * math.pi / 180)
    pointY = y - size * math.sin((2 * math.pi) * (i / 5) +
                                 (math.pi / 2) + angle * math.pi / 180)

    point = (pointX, pointY)
    points.append(point)

    innerPointX = x - size / 3 * math.cos(
        (2 * math.pi) * (i / 5) + (math.pi / 2) +
        (2 * math.pi / 10) + angle * math.pi / 180)
    innerPointY = y - size / 3 * math.sin(
        (2 * math.pi) * (i / 5) + (math.pi / 2) +
        (2 * math.pi / 10) + angle * math.pi / 180)

    innerPoint = (innerPointX, innerPointY)
    points.append(innerPoint)

  pygame.draw.polygon(screen, color, points)


while True:
  drawStar(DISPLAYSURF, WHITE, (150, 100), 50, 50)

  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  pygame.display.update()
