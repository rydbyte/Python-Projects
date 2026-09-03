#modules
import pygame, pygame.freetype as freetype, time, threading



#functions



#classes
class Button:
            def __init__(self, x, y, width, height, text, text_color, button_color):
                self.rect = pygame.Rect(x, y, width, height)
                self.text = text
                self.x = x
                self.y = y
                self.width = width
                self.height = height
                self.ogcol = button_color
                self.text_color = text_color
                self.button_color = button_color

            def draw(self, screen):
                self.button_draw = pygame.draw.rect(screen, self.button_color, self.rect)
                font = pygame.font.Font(None, 36)
                text_surface = font.render(self.text, True, self.text_color)
                text_rect = text_surface.get_rect(center=self.rect.center)
                screen.blit(text_surface, text_rect)

            def isOver(self, pos):
                
                #Pos is the mouse position or a tuple of (x,y) coordinates
                if pos[0] > self.x and pos[0] < self.x + self.width:
                    if pos[1] > self.y and pos[1] < self.y + self.height:
                        self.color = (128,128,128)
                    else:
                        self.color = self.ogcol
                else:
                    self.color = self.ogcol
               
                if pos[0] > self.x and pos[0] < self.x + self.width and pos[1] > self.y and pos[1] < self.y + self.height and pygame.MOUSEBUTTONDOWN:
                    return True


class Platform(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        global player_frames
        pygame.sprite.Sprite.__init__(self)
        self.image = player_frames["player_frame_1"]
        self.rect = self.image.get_rect()


    def render(self):
        global frame,side
        self.rect.center = (player_pos.x,player_pos.y)
        if action == "idle":
           if frame <= 20 and frame >= 1:
                self.image = player_frames["player_frame_1"]
                frame += 1
           if frame <=30 and frame >=21:
               self.image = player_frames["player_frame_2"]
               frame += 1
           if frame <=40 and frame >=31:
               self.image = player_frames["player_frame_3"]
               frame += 1
           if frame <=50 and frame >=41:
               self.image = player_frames["player_frame_4"]
               frame += 1
               if frame == 50:
                   frame = 1
            
        if action == "movement":
           if frame <= 10 and frame >= 1:
                self.image = player_frames["player_frame_5"]
                frame += 1
           if frame <=20 and frame >=11:
               self.image = player_frames["player_frame_6"]
               frame += 1
           if frame <=30 and frame >=21:
               self.image = player_frames["player_frame_7"]
               frame += 1
           if frame <=40 and frame >=31:
               self.image = player_frames["player_frame_8"]
               frame += 1
           if frame <= 50 and frame >= 41:
                self.image = player_frames["player_frame_9"]
                frame += 1
           if frame <=60 and frame >=51:
               self.image = player_frames["player_frame_10"]
               frame += 1
               if frame == 60:
                   frame = 1

    def move(self):
        global side
        if side == "left":
            player_pos.x -= 100 * dt
        if side == "right":

            player_pos.x += 100 * dt

    def jump_check(self, colliders):
        global jumping, Y_velocity, collider, gravity
        if jumping == True:
            player_pos.y -= Y_velocity
            if Y_velocity >= 0:
                Y_velocity -= 1
            if pygame.sprite.spritecollide(player, colliders, 0) and Y_velocity < 39:
                jumping = False
                Y_velocity = 40
                
            
class Lvl_1:
   def draw(self):

    sprite = Platform(platform_1, 50, 720)

    sprite2 = Platform(platform_1, 300, 720)
    colliders = pygame.sprite.Group(sprite, sprite2)
    colliders.draw(screen)

    return colliders

class Lvl_2:
    pass



#variables
current_lvl = 0
lvls = [
    "", 
    Lvl_1,
    Lvl_2,
    ]
gravity = True
action = "idle" 
jumping = False
side = "right"
Y_velocity = 40
frame = 1
player_pos = pygame.Vector2(0,500)



#setup
pygame.init()
freetype.init()
screen = pygame.display.set_mode((1080,720), pygame.RESIZABLE|pygame.DOUBLEBUF)
clock = pygame.time.Clock()
ftfont = freetype.SysFont("Arial", 40, True, False)
running = True

player_frames = {
    "player_frame_1": pygame.image.load("2d/spritesheets/player_frame_1.png").convert_alpha(),
    "player_frame_2": pygame.image.load("2d/spritesheets/player_frame_2.png").convert_alpha(),
    "player_frame_3": pygame.image.load("2d/spritesheets/player_frame_3.png").convert_alpha(),
    "player_frame_4": pygame.image.load("2d/spritesheets/player_frame_4.png").convert_alpha(),
    "player_frame_5": pygame.image.load("2d/spritesheets/player_frame_5.png").convert_alpha(),
    "player_frame_6": pygame.image.load("2d/spritesheets/player_frame_6.png").convert_alpha(),
    "player_frame_7": pygame.image.load("2d/spritesheets/player_frame_7.png").convert_alpha(),
    "player_frame_8": pygame.image.load("2d/spritesheets/player_frame_8.png").convert_alpha(),
    "player_frame_9": pygame.image.load("2d/spritesheets/player_frame_9.png").convert_alpha(),
    "player_frame_10": pygame.image.load("2d/spritesheets/player_frame_10.png").convert_alpha()}
platform_1 = pygame.image.load("2d/spritesheets/cave/platform-1.png").convert_alpha()


player = Player()
player_group = pygame.sprite.GroupSingle(player)



while running:
    screen.fill("black")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #movement; jumping and crouch
        if event.type == pygame.KEYDOWN and current_lvl != 0:
            if event.key == pygame.K_UP and jumping == False:
               jumping = True
        #set action to idle
        if event.type == pygame.KEYUP and current_lvl != 0:
               action="idle"
               frame = 1

   
    
    if current_lvl == 0:
        title = ftfont.render_to(screen, ((screen.get_width()/ 2)- 5, 50), "Test", "white")
        button_1 = Button(40, 70, 60,60,"lvl 1", "white", "red")
        button_1.draw(screen)

        if button_1.isOver(pygame.mouse.get_pos()) == True:
            current_lvl = 1
    else:

        #get level and draw level
        lvl = lvls[current_lvl]()
        colliders = lvl.draw()

        #get player, render player get collider and check 
        player.render()
        player.jump_check(colliders)
        player_group.draw(screen)

        #movement; left right
        key_listen = pygame.key.get_pressed()
        if key_listen[pygame.K_LEFT] and not key_listen[pygame.K_RIGHT]:
            player.move()
            side = "left"
            action="movement"
        if key_listen[pygame.K_RIGHT] and not key_listen[pygame.K_LEFT]:
            player.move()
            side = "right"
            action="movement"
       
        #gravity
        if gravity and not pygame.sprite.spritecollide(player, colliders, 0):
            player_pos.y += 900 * dt
        
        #fall check
        if player_pos.y >= 900:
            player_pos = pygame.Vector2(5,400)


    pygame.display.update()
    dt = clock.tick(60)/1000

pygame.quit()
