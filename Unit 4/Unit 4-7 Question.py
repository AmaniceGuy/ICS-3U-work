# I - Import and Initialize
import pygame
pygame.init()
 
def statusSurface(drawColor, lineWidth):
    """ creates a Surface object for status text """
    myFont = pygame.font.SysFont("Courier", 20)
    status_string = "color: %s, width: %d" % (drawColor, lineWidth)
    status = myFont.render(status_string, True, (0,0,0))
    return status

def disNoFile():
    """creates a Surface object to tell the user the painting file was not found"""
    myFont = pygame.font.SysFont("courier",15)
    noFileText = myFont.render("File not found",True,(255,0,0))
    return noFileText

def main():
    '''This function defines the 'mainline logic' for our paint program.'''
     
    # D - Display configuration
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Paint:  (w)hite, blac(k), (c)lear, (q)uit")
     
    # E - Entities
    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))
    pygame.mixer.music.load("piano.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    # A - Action (broken into ALTER steps)
     
    # A - Assign values to key variables
    clock = pygame.time.Clock()
    keepGoing = True
    lineStart = (0, 0)
    drawColor = (0, 0, 0)
    lineWidth = 3
    noFileCount = 0
     
    # L - Loop
    while keepGoing:
    
        # T - Timer to set frame rate
        clock.tick(30)
     
        # E - Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.fadeout(2000)
                keepGoing = False
            elif event.type == pygame.MOUSEMOTION:
                lineEnd = pygame.mouse.get_pos()
        # Check if left mouse button is down
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    pygame.draw.line(background, drawColor, lineStart, lineEnd, lineWidth)
                lineStart = lineEnd
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    #quit    
                    keepGoing = False
                elif event.key == pygame.K_s:
                    #save
                    pygame.image.save(background,"painting.bmp")
                elif event.key == pygame.K_l:
                    #load painting.bmp
                    try:
                        paintFile = pygame.image.load("painting.bmp").convert()
                        background.blit(paintFile,(0,0))
                    except:
                        #if the file doesn't exist and user tries to load it
                        noFileCount = 90
                elif event.key == pygame.K_c:
                    #clear screen
                    background.fill((255, 255, 255))
                elif event.key == pygame.K_w:
                    #white
                    drawColor = (255, 255, 255)
                elif event.key == pygame.K_k:
                    #black
                    drawColor = (0, 0, 0)
                elif event.key == pygame.K_r:
                    #red
                    drawColor = (255,0,0)
                elif event.key == pygame.K_g:
                    #green
                    drawColor = (0,255,0)
                elif event.key == pygame.K_b:
                    #blue
                    drawColor = (0,0,255)
                else:
                    try:
                        if int(pygame.key.name(event.key)) in range(1,10):
                            #line width
                            lineWidth = int(pygame.key.name(event.key))
                    except ValueError:
                        lineWidth = lineWidth
                    
        # R - Refresh display
        screen.blit(background, (0, 0))
        myLabel = statusSurface(drawColor, lineWidth)
        screen.blit(myLabel, (screen.get_width() - myLabel.get_width(), 450))
        if noFileCount != 0:
            screen.blit(disNoFile(),(0,0))
            noFileCount -= 1
        pygame.display.flip()
     
    # Close the game window
    pygame.time.delay(2500)
    pygame.quit()    
    
        
# Call the main function
main()