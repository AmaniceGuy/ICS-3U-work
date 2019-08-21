import pygame
pygame.init()

font = pygame.font.SysFont("corbel",50)
text = font.render("Frostblade Sivir",True,(0,0,0))
image = pygame.image.load("sivirr.png")
image.blit(text,(0,0))
pygame.image.save(image,"sivirr.png")
pygame.quit()