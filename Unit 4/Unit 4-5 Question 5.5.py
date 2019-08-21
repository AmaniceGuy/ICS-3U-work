import pygame
import math
pygame.init()

win = pygame.display.set_mode((640,480))
win.fill((255,255,255))
points = (155,210),(159,200,),(166,200),(166,280),(159,280),(155,270)
pygame.draw.circle(win,(0,0,0),(95,240),40,0)
pygame.draw.rect(win,(0,0,0),(95,200,55,80),0)
pygame.draw.rect(win,(0,0,0),(150,210,5,60),0)
pygame.draw.polygon(win,(0,0,0),(points),0)
pygame.draw.arc(win,(255,255,255),(65,214,23,23),5*math.pi/4,math.pi/4,5)
pygame.display.update()
while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()