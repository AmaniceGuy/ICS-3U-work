# Initialize
import pygame
pygame.init()
 
# Display
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("move a box")
 
# Entities
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((136, 64, 0))    # yellow background
 
# make a red 25 x 25 box
box = pygame.Surface((25, 25))
box = box.convert()
box.fill((0, 255, 0))
 
# upper-left coordinates for box
box_x = 200
box_y = 0
 
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
 
    #modify box value
    box_y += 7
    #check boundaries
    if box_y > screen.get_height():
        box_y = 0
 
    # Refresh screen
    screen.blit(background, (0, 0))
    screen.blit(box, (box_x, box_y))
    pygame.display.flip()
 
# Close the game window
pygame.quit()