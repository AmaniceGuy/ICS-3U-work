import pygame
pygame.init()

#Display
screen = pygame.display.set_mode((900,100))
pygame.display.set_caption("pink box")

#Entities
background = pygame.Surface(screen.get_size()).convert()
background.fill((0,0,0))

#make pink box
box = pygame.Surface((30,30)).convert()
box.fill((248,24,148))

boxX = 0
boxY = 0
boxLR = True
boxUpDown = True

#Time
clock = pygame.time.Clock()
run = True

while run:
   clock.tick(60)
   
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         run = False
   
   if boxLR:
      boxX += 6
   else:
      boxX -= 6
   if boxUpDown:
      boxY += 6
   else:
      boxY -= 6
   if boxX + box.get_width() > screen.get_width() or boxX < 0:
      boxLR = not(boxLR)
   if boxY + box.get_height() > screen.get_height() or boxY < 0:
      boxUpDown = not(boxUpDown)
   
   screen.blit(background, (0,0))
   screen.blit(box, (boxX, boxY))
   pygame.display.flip()
   
pygame.quit()