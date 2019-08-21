import pygame
import random
 
class Brick(pygame.sprite.Sprite):
    '''A simple Sprite subclass to represent static Brick sprites.'''
    def __init__(self, screen):
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
 
        # Set the image and rect attributes for the bricks
        self.image = pygame.Surface((40,40))
        self.image.fill((random.randrange(256),random.randrange(256),random.randrange(256)))
        self.rect = self.image.get_rect()
        self.rect.top = random.randrange(0, screen.get_width()-50)
        self.rect.left = random.randrange(0, screen.get_height()-50)
        self.win = screen
        #set the y direction and x direction
        self.vel = 3
        if random.randrange(2) == 0:
            self.dx = 0-self.vel
        else:
            self.dx = self.vel
        if random.randrange(2) == 0:
            self.dy = 0- self.vel
        else:
            self.dy = self.vel
            
    def update(self):
        if self.rect.left > self.win.get_width() - 50 or self.rect.left <= 0:
            self.dx = -self.dx
        if self.rect.top > self.win.get_height()- 50 or self.rect.top <= 0:
            self.dy = -self.dy
        self.rect.left += self.dx
        self.rect.top += self.dy

class Circle(pygame.sprite.Sprite):
    '''Mouse-following Circle Sprite subclass.'''
    def __init__(self,colour):
        '''Initializer to set the image for our Circle Sprite.'''       
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
 
        # Customize the image and rect for the circle
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0,0,0))
        pygame.draw.circle(self.image, colour, (25, 25), 25, 0)
        self.rect = self.image.get_rect()
         
    def update(self):
        '''Move the center of the circle to where the mouse is pointing.'''
        self.rect.center = pygame.mouse.get_pos()

class Label(pygame.sprite.Sprite):
    '''An mutatable text Label Sprite subclass'''
    def __init__(self, message, x_y_center,font_Name,size,colour):
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont(font_Name, size)
        self.text = message
        self.colour = colour
        self.center = x_y_center
         
    def setText(self, message):
        '''Mutator for text to be displayed on the label.'''
        self.text = message
                 
    def update(self):
        '''Render and center the label text on each Refresh.'''
        self.image = self.font.render(self.text, True, self.colour)
        self.rect = self.image.get_rect()
        self.rect.center = self.center

class Pacman(pygame.sprite.Sprite):
    '''Pacman class'''
    def __init__(self,x,y,screen):
        '''Initializer'''
        pygame.sprite.Sprite.__init__(self)
        self.R_Image = pygame.image.load("pacman-right.png")
        self.L_Image = pygame.image.load("pacman-left.png")
        self.D_Image = pygame.image.load("pacman-down.png")
        self.U_Image = pygame.image.load("pacman-up.png")
        self.image = self.R_Image
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.win = screen
        self.dx = 5
        self.dy = 0

    def go_left(self):
        self.dx = -5
        self.dy = 0
        self.image = self.L_Image

    def go_right(self):
        self.dx = 5
        self.dy = 0
        self.image = self.R_Image

    def go_up(self):
        self.dx = 0
        self.dy = -5
        self.image = self.U_Image

    def go_down(self):
        self.dx = 0
        self.dy = 5
        self.image = self.D_Image

    def move(self,xy_change):
        self.dx,self.dy = xy_change

    def update(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        if self.rect.bottom < 0:
            self.rect.bottom = self.win.get_height()
        elif self.rect.top > self.win.get_height():
            self.rect.top = 0
        if self.rect.right < 0:
            self.rect.right = self.win.get_width()
        elif self.rect.left > self.win.get_width():
            self.rect.left = 0

class Cherry(pygame.sprite.Sprite):
    """cherry object class"""
    def __init__(self,screen):
        ''' initializer'''
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Cherry.png")
        self.rect = self.image.get_rect()
        self.rect.left = random.randrange(screen.get_width()-self.image.get_width())
        self.rect.top = random.randrange(screen.get_height()-self.image.get_height())
        self.screen = screen
