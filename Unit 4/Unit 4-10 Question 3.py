# I - Import and Initialize
import pygame
import mySprites
pygame.init()
            
def main():
    '''This function defines the 'mainline logic' for our game.'''
      
    # Display
    screen = pygame.display.set_mode((640, 480))    
    pygame.display.set_caption("Label demo")
     
    # Entities
    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))
    screen.blit(background, (0, 0))
     
    # Create 3 Label sprites and add to an OrderedUpdates Sprite Group
    label1 = mySprites.Label("Hi. I'm a label.", (100,100), "None",30,(0,255,123))
    label2 = mySprites.Label("I'm another label.", (400,400),"None",30,(255,123,0))
    # Will update labelEvent.text during mouse Event Handling
    labelEvent = mySprites.Label("", (320,200),"None",40,(123,0,255))
    allSprites = pygame.sprite.OrderedUpdates(label1, label2, labelEvent)
         
    # ACTION
     
    # Assign 
    clock = pygame.time.Clock()
    keepGoing = True
 
    # Loop
    while keepGoing:
     
        # Time
        clock.tick(30)
     
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.MOUSEMOTION:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                labelEvent.setText("mouse: (%d, %d)" % (mouseX, mouseY))
            elif event.type == pygame.MOUSEBUTTONDOWN:
                labelEvent.setText("button press: " + str(pygame.mouse.get_pressed()))
            elif event.type == pygame.KEYDOWN:
                labelEvent.setText("key down: " + str(pygame.key.name(event.key)))
         
        # Refresh screen
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
         
        pygame.display.flip()
 
    # Close the game window
    pygame.quit()    
         
# Call the main function
main()
