import pygame
pygame.init()

win = pygame.display.set_mode((1215,717))
pygame.display.set_caption("image")
image = pygame.image.load("sivir.png").convert()
image2 = pygame.image.load("sivirr.png").convert()
image3 = pygame.image.load("ssivir.png").convert()
image4 = pygame.image.load("Sivir_4.png").convert()
box = pygame.Surface((image.get_width(),image.get_height()))
pix = 1


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    for x in range(0,image.get_width(),pix):
        for y in range(0,image.get_height(),pix):
            r,g,b = image.get_at((x,y))[0],image.get_at((x,y))[1],image.get_at((x,y))[2]
            if r == 0:
                r = 164
            elif r < 125:
                r = r*2
            else:
                r -= 125
            if g == 0:
                r = 164            
            elif g < 125:
                g = g*2
            else:
                g -= 125
            if b == 0:
                b = 84             
            elif b < 125:
                b = b*2
            else:
                b -= 125
            box.set_at((x,y),(r,g,b))   

    win.blit(box,(0,0))
    pygame.display.update()
pygame.image.save(box,"myImage.png")