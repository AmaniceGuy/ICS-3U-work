# Initialize
import pygame
pygame.init()
 
# Display
screen = pygame.display.set_mode((900, 900))
pygame.display.set_caption("move a box")
 
# Entities
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))    # yellow background

#music
pygame.mixer.music.load("canon in d.mp3")
pygame.mixer.music.set_volume(0.6)
pygame.mixer.music.play(-1)
boing = pygame.mixer.Sound("piano.mp3")
 
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

win =pygame.image.load("win.png")
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
        boing.play()
    if box2_x < 0:
        boing.play()
        box2_x = screen.get_width()
    if box3_x > screen.get_width():
        box3_x = 0
        boing.play()
    if box4_x < 0:
        boing.play()
        box4_x = screen.get_width()
        
    if box1_y > screen.get_height():
        box1_y = 0
        boing.play()
    if box2_y > screen.get_height():
        box2_y = 0
        boing.play()
    if box3_y < 0:
        boing.play()
        box3_y = screen.get_height()
    if box4_y < 0:
        boing.play()
        box4_y = screen.get_height()      
 
    # Refresh screen
    screen.blit(background, (0, 0))
    screen.blit(win, (box1_x, box1_y))
    screen.blit(win, (box2_x, box2_y))
    screen.blit(win, (box3_x, box3_y))
    screen.blit(win, (box4_x, box4_y))
    pygame.display.flip()
 
# Close the game window
pygame.quit()
