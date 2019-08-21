# I - Import and Initialize
import pygame, myBoxjoy
pygame.init()
     
def main():
    '''This function defines the 'mainline logic' for our game.'''
      
    # Display
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Move the rectangle with the joystick!")
     
    # Entities
    # Create a list of Joystick objects.
    joysticks = []
    for joystick_no in range(pygame.joystick.get_count()):
        stick = pygame.joystick.Joystick(joystick_no)
        stick.init()
        joysticks.append(stick)    
 
    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))
    screen.blit(background, (0, 0))
     
    # Create a Box sprite object
    box = myBoxjoy.Box(screen,20,20)
    box2 = myBoxjoy.Box(screen,300,300)
    boxes = pygame.sprite.OrderedUpdates(box2)
    allSprites = pygame.sprite.OrderedUpdates(box,box2)

    #bullets
    p1_bullets,p2_bullets = [],[]
 
    # ACTION
     
    # Assign 
    clock = pygame.time.Clock()
    keepGoing = True
 
    # Hide the mouse pointer
    pygame.mouse.set_visible(False)
 
    # Loop
    while keepGoing:
     
        # Time
        clock.tick(30)
     
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.JOYHATMOTION:
                if event.joy == 0:
                    box.changeDirection(event.value)
                elif event.joy == 1:
                    box2.changeDirection(event.value)
            elif event.type == pygame.JOYBUTTONDOWN:
                if event.joy == 0 and event.button == 1:
                    p1_bullets.append(myBoxjoy.Bullet(screen,box.rect.centerx,box.rect.centery))
                elif event.joy == 1 and event.button == 1:
                    p2_bullets.append(myBoxjoy.Bullet(screen,box2.rect.centerx,box2.rect.centery))    
                
        # Refresh screen
        allSprites.clear(screen, background)
        allSprites = pygame.sprite.OrderedUpdates(box,box2,p1_bullets,p2_bullets)

        allSprites.update()
        allSprites.draw(screen)
        pygame.display.flip()
         
    # Unhide mouse pointer
    pygame.mouse.set_visible(True)
 
    # Close the game window
    pygame.quit()    
     
# Call the main function
main()    
