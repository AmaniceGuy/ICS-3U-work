import pygame
import mySprites
import random
pygame.init()
pygame.mixer.init()

def main():
    #Display
    screen = pygame.display.set_mode((480,640))
    pygame.display.set_caption("Pacman")

    #Entities
    background = pygame.Surface(screen.get_size())
    background.fill((255,255,255))
    screen.blit(background,(0,0))

    #Cherries
    cherries = []
    for i in range(10):
        cherries.append(mySprites.Cherry(screen))

    #Joysticks
    joysticks = []
    for joystick_no in range(pygame.joystick.get_count()):
        stick = pygame.joystick.Joystick(joystick_no)
        stick.init()
        joysticks.append(stick)

    #Pacman
    pac = mySprites.Pacman(screen.get_width()//2,screen.get_height()//2,screen)

    cherrySprites = pygame.sprite.OrderedUpdates(cherries)
    allSprites = pygame.sprite.OrderedUpdates(cherries,pac)
    #Action
    #Assign
    clock = pygame.time.Clock()
    run = True

    #loop
    while run:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.faeout(2000)
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key ==  pygame.K_UP:
                    pac.go_up()
                elif event.key ==  pygame.K_DOWN:
                    pac.go_down() 
                elif event.key ==  pygame.K_RIGHT:
                    pac.go_right()
                elif event.key ==  pygame.K_LEFT:
                    pac.go_left()
            elif event.type == pygame.JOYHATMOTION:
                x,y = event.value
                if x == 1:
                    pac.go_right()
                elif y == 1:
                    pac.go_up()
                elif x == -1:
                    pac.go_left()
                elif y == -1:
                    pac.go_down()

        allSprites.clear(screen,background)
        eaten = pygame.sprite.spritecollide(pac,cherrySprites,True)
        if eaten:
            sound.play(0)
        if not(cherrySprites):
            run = False
            print("you win now leave")
        allSprites.update()
        allSprites.draw(screen)
        pygame.display.flip()

    pygame.quit()
main()

        

            

        
