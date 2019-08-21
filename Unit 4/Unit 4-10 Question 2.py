# I - Import and Initialize
import pygame
import mySprites
pygame.init()
 
def main():
    '''This function defines the 'mainline logic' for our game.'''
      
    # Display
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Move the circle with the mouse!")
     
    # Entities
    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))
    screen.blit(background, (0, 0))
     
    # Create a Circle sprite object and add to an OrderedUpdates Sprite Group
    colour = (255,12,255)
    circle = mySprites.Circle(colour)
    allSprites = pygame.sprite.OrderedUpdates(circle)

    # Add list of 10 Brick Sprites to one OrderedUpdates Sprite Group
    allSprites = pygame.sprite.OrderedUpdates(circle)
    pygame.mouse.set_visible(False)
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
