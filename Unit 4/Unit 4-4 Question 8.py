# Initialize
import pygame
pygame.init()
 
# Display
screen = pygame.display.set_mode((480, 480))
pygame.display.set_caption("move a box")
 
# Entities
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))    # yellow background
 
# make a red 25 x 25 box
box1 = pygame.Surface((25, 25)).convert()
box1.fill((255, 0, 0))
box1_x = 0
box1_y = 0

box2 = pygame.Surface((25, 25)).convert()
box2.fill((255, 0, 255))
box2_x = screen.get_width() - box1.get_width()
box2_y = 0

box3 = pygame.Surface((25, 25)).convert()
box3.fill((2,100,255))
box3_x = 0
box3_y = screen.get_height() - box3.get_height()

box4 = pygame.Surface((25, 25)).convert()
box4.fill((255, 255,255))
box4_x = screen.get_width() - box4.get_width()
box4_y = screen.get_height() - box4.get_height()

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
 
    #modify box_x value
    box1_x += 7
    box2_x -= 7
    box3_x += 7
    box4_x -= 7
    
    #modify box_y values
    box1_y += 7
    box2_y += 7
    box3_y -= 7
    box4_y -= 7
    
    #check boundaries
    if box1_x > screen.get_width():
        box1_x = 0
    if box2_x < 0:
        box2_x = screen.get_width()
    if box3_x > screen.get_width():
        box3_x = 0
    if box4_x < 0:
        box4_x = screen.get_width()
        
    if box1_y > screen.get_height():
        box1_y = 0
    if box2_y > screen.get_height():
        box2_y = 0
    if box3_y < 0:
        box3_y = screen.get_height()
    if box4_y < 0:
        box4_y = screen.get_height()      
 
    # Refresh screen
    screen.blit(background, (0, 0))
    screen.blit(box1, (box1_x, box1_y))
    screen.blit(box2, (box2_x, box2_y))
    screen.blit(box3, (box3_x, box3_y))
    screen.blit(box4, (box4_x, box4_y))
    pygame.display.flip()
 
# Close the game window
pygame.quit()