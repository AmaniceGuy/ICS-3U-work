import pygame
import random
import mySprites

def main():
   '''This function defines the 'mainline logic' for our game.'''
    
   # Display
   screen = pygame.display.set_mode((640, 480))
   pygame.display.set_caption("Lots Of Bricks")
     
   # Entities
   background = pygame.Surface(screen.get_size())
   background.fill((255, 255, 255))
   screen.blit(background, (0, 0))
 
   # Create 10 random bricks using a loop and a list
   bricks = []
   for i in range(25):
      bricks.append(mySprites.Brick(screen))
     
   # Add list of 10 Brick Sprites to one OrderedUpdates Sprite Group
   allSprites = pygame.sprite.OrderedUpdates(bricks)
     
   # ACTION
     
   # Assign 
   keepGoing = True
   clock = pygame.time.Clock()
    
   # Loop
   while keepGoing:
     
      # Time
      clock.tick(30)
     
      # Events
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            keepGoing = False
         
      # Refresh screen
      allSprites.clear(screen, background)
      # The Brick Sprite has NO update() method, so next line does nothing.
      allSprites.update()
      allSprites.draw(screen)
         
      pygame.display.flip()
 
   # Close the game window
   pygame.quit()     
       
# Call the main function
main()      
