#modules
import pygame, random, time
from pygame import freetype


#setup
pygame.init()
freetype.init()
ftfont = freetype.SysFont("Arial", 80, True, False)

score_font = freetype.SysFont("Berlin Sans FB DEMI", 56, True, False)
screen = pygame.display.set_mode((1080,720), pygame.RESIZABLE)
clock = pygame.time.Clock()

running = True
started = False
ball_side = [1, "up"]

#1 left, 2 right, 3 up, 4 down
ball_side[0] = random.randint(1,2)
ball_side[1] = random.randint(3,4)
dt = 0
score = {
    "left": 0,
    "right": 0
}

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height()/ 2)
left_pos = pygame.Vector2(180,  screen.get_height()/2 - 50)
left_pos_end = pygame.Vector2(180,  screen.get_height()/2 + 50)
right_pos = pygame.Vector2(screen.get_width()-180,  screen.get_height()/2 - 50)
right_pos_end = pygame.Vector2(screen.get_width()-180,  screen.get_height()/2 + 50)



#functions
def draw_parts():
    ball = pygame.draw.circle(screen, "white", player_pos, 15)
    left = pygame.draw.line(screen, "white",left_pos,left_pos_end, 15 )
    right = pygame.draw.line(screen, "white",right_pos,right_pos_end, 15 )


def drawGrid():
    blockSize = 100 #Set the size of the grid block
    for x in range(0, screen.get_width(), blockSize):
        for y in range(0, screen.get_height(), blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, "white", rect, 1)



#main
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and started == False:
            started = True
    

    screen.fill("black")
   

    if started == False:
        if score["left"] == 3:
                score_font.render_to(screen, (screen.get_width() /2.218 , screen.get_height()/13), f"{score['left']} : {score['right']}\tLeft won!", "white")  
                draw_parts() 
                drawGrid()
        if score["right"] == 3:
                score_font.render_to(screen, (screen.get_width() /2.218 , screen.get_height()/13), f"{score['left']} : {score['right']}\tRight won!", "white")
                draw_parts() 
                drawGrid()
        else:
            ftfont.render_to(screen, (screen.get_width()-800, screen.get_height()/4), "Press a key to start: ", "white")
            draw_parts() 
            drawGrid()
    
  


    if started == True:
        if score["left"] == 3 or score["right"] == 3:
             score["left"] = 0
             score["right"] = 0
        score_font.render_to(screen, (screen.get_width() /2.218 , screen.get_height()/13), f"{score['left']} : {score['right']}", "white")
        left_collider = pygame.Rect(188, left_pos.y+10, 6, 95)
        right_collider = pygame.Rect(screen.get_width()-185, right_pos.y+10, 6, 95)
        ball_collider = pygame.Rect(player_pos.x, player_pos.y, 15, 15)

        keys_left = pygame.key.get_pressed()
        if keys_left[pygame.K_w] and left_pos.y > 0:
            left_pos.y -= 800 * dt
            left_pos_end.y -= 800 * dt
        if keys_left[pygame.K_s]and left_pos_end.y < screen.get_height():
            left_pos.y += 800 * dt
            left_pos_end.y += 800 * dt


        keys_right = pygame.key.get_pressed()
        if keys_right[pygame.K_UP] and right_pos.y > 0:
            right_pos.y -= 800 * dt
            right_pos_end.y -= 800 * dt
        if keys_right[pygame.K_DOWN]and right_pos_end.y < screen.get_height():
            right_pos.y += 800 * dt
            right_pos_end.y += 800 * dt

        if ball_side[0] == 1:
            player_pos.x -= 600 * dt
            if ball_collider.colliderect(left_collider):
                ball_side[0] = 2
            if player_pos.x <= 0:
                started = False
                ball_side[0] = random.randint(1,2)
                ball_side[1] = random.randint(3,4)
                score["right"] += 1
                player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height()/ 2)
                left_pos = pygame.Vector2(180,  screen.get_height()/2 - 50)
                left_pos_end = pygame.Vector2(180,  screen.get_height()/2 + 50)
                right_pos = pygame.Vector2(screen.get_width() - 180,  screen.get_height()/2 - 50)
                right_pos_end = pygame.Vector2(screen.get_width() -180,  screen.get_height()/2 + 50)
                draw_parts()

        if ball_side[0] == 2:
            player_pos.x += 600 * dt
            if ball_collider.colliderect(right_collider):
                ball_side[0] = 1
            if player_pos.x >= screen.get_width():
                started = False
                ball_side[0] = random.randint(1,2)
                ball_side[1] = random.randint(3,4)
                score["left"] += 1
                player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height()/ 2)
                left_pos = pygame.Vector2(180,  screen.get_height()/2 - 50)
                left_pos_end = pygame.Vector2(180,  screen.get_height()/2 + 50)
                right_pos = pygame.Vector2(screen.get_width() - 180,  screen.get_height()/2 - 50)
                right_pos_end = pygame.Vector2(screen.get_width()- 180,  screen.get_height()/2 + 50)
                draw_parts()

        if ball_side[1] == 3:
            player_pos.y -= 600 * dt
            if player_pos.y < 1:
                ball_side[1] = 4
        if ball_side[1] == 4:
            player_pos.y += 600 * dt
            if player_pos.y > screen.get_height():
                ball_side[1] = 3

        draw_parts()
        drawGrid()
    
    pygame.display.flip()
    dt = clock.tick(60)/1000



pygame.quit()