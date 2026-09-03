#modules
import pygame, math, random, pygame.freetype, time



#setup
pygame.init()
pygame.freetype.init()
screen = pygame.display.set_mode((840,700))
clock = pygame.time.Clock() 
on = True



#var
font = pygame.freetype.SysFont("Arial", 30, False, False)
game_over_font = pygame.freetype.SysFont("Arial", 40, True, False)
highscore = 0
scroll = 0
car_speed = 4
car_max = 5
car_group = pygame.sprite.Group()
scroll_speed = 0.5

car_start_pos = [
    200,
    325,
    455,
    585,
]
player_start_pos = [
    200,
    325,
    455,
    585,
]
player_y = 560
player_pos = 3

bg = pygame.image.load("2d/spritesheets/bgs/background-1.png").convert_alpha()
car_image = [
    pygame.image.load("2d/spritesheets/cars/car1.png").convert_alpha(),
    pygame.image.load("2d/spritesheets/cars/car2.png").convert_alpha(),
    pygame.image.load("2d/spritesheets/cars/car3.png").convert_alpha(),
    pygame.image.load("2d/spritesheets/cars/car4.png").convert_alpha(),
    pygame.image.load("2d/spritesheets/cars/car5.png").convert_alpha(),
    pygame.image.load("2d/spritesheets/cars/car6.png").convert_alpha(),
    pygame.image.load("2d/spritesheets/cars/car7.png").convert_alpha(),
    pygame.image.load("2d/spritesheets/cars/car8.png").convert_alpha(),
    pygame.image.load("2d/spritesheets/cars/car9.png").convert_alpha(),
    pygame.image.load("2d/spritesheets/cars/car10.png").convert_alpha(),
    pygame.image.load("2d/spritesheets/cars/car11.png").convert_alpha(),
]
player_image = pygame.image.load("2d/spritesheets/cars/main.png").convert_alpha()

wait_time = 200
time_to_wait = 200
game_over = False
stopped = False


#classes
class Car(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)


class Player(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.height -= 30
        self.rect.center = (self.x, self.y)



#main
while on:
    if not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on = False 
            if event.type == pygame.KEYDOWN and not stopped:
                if event.key == pygame.K_RIGHT and not player_pos == 3:
                    player_pos += 1
                if event.key == pygame.K_LEFT and not player_pos == 0:
                    player_pos -= 1


        #scrolling        
        for i in range(0, -3, -1):
            screen.blit(bg, (0, i * 600 - scroll))
        scroll -= scroll_speed * 5 
        if abs(scroll) >= 600:
            scroll = 0

        #forward key
        key_down = pygame.key.get_pressed()
        if key_down[pygame.K_UP] and player_y >= 470 and not stopped:
            player_y -= 1
        elif not key_down[pygame.K_UP] and player_y <= 560 and not stopped:
            player_y += 2
        

        #player render
        player = Player(player_image, player_start_pos[player_pos], player_y)
        player.rect.center = (player.x, player.y)
        screen.blit(player.image, (player.x, player.y))
        player_group = pygame.sprite.GroupSingle(player)


        #check and spawn car
        if len(car_group) <= car_max and wait_time <= 0:
            wait_time = time_to_wait
            car = Car(car_image[random.randint(0,10)], car_start_pos[random.randint(0,3)], -100)
            car_group.add(car)
        

        #render cars
        for car in car_group:
            car.y += car_speed
            car.rect.center = (car.x, car.y)
            screen.blit(car.image, (car.x, car.y))
            
            if car.y > 720:
                car_group.remove(car)


        if pygame.sprite.groupcollide(car_group, player_group, False, False):
            stopped = True
            for n in range(0,2001,1):
                if n == 2000:
                    car_group.empty()
                    stopped = False
                    game_over = True


        #updates
        print(f"TTW: {time_to_wait}, TTR: {wait_time}, CS: {car_speed}, CM: {car_max}, SS: {scroll_speed}, CH: {player.rect}\n")
        if not stopped:
            highscore += 1 
            car_speed += 0.0005
            scroll_speed += 0.0001
            wait_time -= 2
            if not time_to_wait <= 5:
                time_to_wait -= 0.035
            car_max += 0.0015

        font.render_to(screen, (10,20), str(highscore), "White")
        pygame.display.update()
        dt = clock.tick(120)/1000

    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on = False 
            if event.type == pygame.KEYDOWN:
                game_over = False
                highscore = 0
                time_to_wait = 200
                wait_time = time_to_wait
                car_speed = 4
                car_max = 5
                scroll = 0
                scroll_speed = 0.5

        screen.fill("black")
        game_over_font.render_to(screen, (340,210), "Game Over", "White")
        font.render_to(screen, (340,300), f"Highscore: {str(highscore)}", "White")
        font.render_to(screen, (315,340), "Press key to restart:", "White")

        pygame.display.update()
        dt = clock.tick(120)/1000

    


pygame.quit()