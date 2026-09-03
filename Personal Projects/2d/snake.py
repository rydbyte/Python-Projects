#modules
import pygame, pygame.freetype as freetype, random



#classes
class Food:
    def __init__(self, window, x=None, y=None):
        self.window = window
        self.width = 25
        self.height = 25
        self.x, self.y = x, y
        if not x or not y: self.new_position()

    def draw(self):
        apple = pygame.draw.rect(self.window, (255,0,0), (self.x, self.y, 25, 25))
        return apple

    def new_position(self):
        self.x, self.y = random.choice(range(0, 500, 25)), random.choice(range(0, 500, 25))


#setup
pygame.init()
freetype.init()
pygame.display.set_caption("Snake")
score_font = freetype.SysFont("Berlin Sans FB DEMI", 30, True, False)
screen = pygame.display.set_mode((1080,720), pygame.RESIZABLE)
clock = pygame.time.Clock()

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height()/ 2)
food = Food(screen)
food.new_position()

running = True
started = False
side = ""
body = [[player_pos.x-25, player_pos.y-25]]
score = 0
apples = 0



#main
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                side = 'up'
            if event.key == pygame.K_DOWN:
                side = 'down'
            if event.key == pygame.K_LEFT:
                side = 'left'
            if event.key == pygame.K_RIGHT:
                side = 'right'
            started = True

    screen.fill("black")

    if started == False:
        score_font.render_to(screen,(screen.get_width()/2.5, 2) , "Press any arrow key:", "white")
       

    if started == True:
        score_font.render_to(screen,(screen.get_width()/ 2, 2) , str(score), "white")
        match side:
            case "up":
                player_pos.y -= 200 * dt
                player_pos.y -= 200 * dt
            case "down":
                player_pos.y += 200 * dt
                player_pos.y += 200 * dt
            case "left":
                player_pos.x -= 200 * dt
                player_pos.x -= 200 * dt
            case "right":
                player_pos.x += 200 * dt
                player_pos.x += 200 * dt
            case _:
                pass
        if head.colliderect(apple):
            score += 10
            food.new_position()


    head = pygame.draw.rect(screen, "green", (player_pos.x, player_pos.y, 25,25), 25)
    apple = food.draw()
    apple
    pygame.display.flip()   
    dt = clock.tick(30)/1000


pygame.quit()