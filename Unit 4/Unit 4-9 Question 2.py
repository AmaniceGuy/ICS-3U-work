import pygame
import random
pygame.init()
 
class Box(pygame.sprite.Sprite):
    '''Our Box class inherits from the Sprite class'''
    def __init__(self, screen,colour,x,y):
        '''Initializer to set the image, position, and direction for a Box Sprite.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
         
        # Keep track of the screen so we can call get_witdth()
        self.window = screen
         
        # Define a red Surface for our Box Sprite
        self.image = pygame.Surface((25, 25))
        self.image = self.image.convert()
        self.image.fill(colour)
         
        # Define the position of our Box using it's rect
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        if random.randrange(2) == 1:
            self.dx = -10
        else:
            self.dx = 10
        if random.randrange(2) == 1:
            self.dy = -10
        else:
            self.dy = 10
 
    def update(self):
        '''Automatically called in the Refresh section to update our Box Sprite's position.'''
        self.rect.left += self.dx
        self.rect.top += self.dy
        if (self.rect.left < 0) or (self.rect.right > self.window.get_width()):
            self.dx = -self.dx
        if (self.rect.top < 0) or (self.rect.bottom > self.window.get_height()):
            self.dy = -self.dy
             
def main():
    '''This function defines the 'mainline logic' for our game.'''
    # Display
    screen = pygame.display.set_mode((0, 0))
    pygame.display.set_caption("Basic Sprite Demo")
     
    # Entities
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 0))
    screen.blit(background, (0,0))
     
    # create a Box sprite object from our mySprites module
    boxes = []
    for i in range(100):
        r = random.randrange(256)
        g = random.randrange(256)
        b = random.randrange(256)
        colour = (r,g,b)
        x = random.randrange(screen.get_width())
        y = random.randrange(screen.get_height())
        boxes.append(Box(screen,colour,x,y))
    # add our Box sprite to an OrderedUpdates Sprite Group to keep Refresh section simple
    allSprites = pygame.sprite.OrderedUpdates(boxes)
     
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
 
        # Refresh screen
        allSprites.clear(screen, background)
        # The next line calls the update() method for any sprites in the allSprites group.
        allSprites.update()
        allSprites.draw(screen)
     
        pygame.display.flip()
 
    # Close the game window
    pygame.quit()        
 
# Call the main function
main()
