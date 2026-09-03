import pygame, pygame.freetype


#setup
pygame.init()
pygame.freetype.init()
screen = pygame.display.set_mode((1080, 720))
clock = pygame.time.Clock()


#var
running = True
started = False
stopped = False
score = 0


#functions



#classes
class player(pygame.sprite.Sprite):



#main
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and not stopped:
            if event.key == pygame.K_UP:
    
    screen.fill("black")
    pygame.display.update()
    dt = clock.tick(120)/1000


pygame.quit()