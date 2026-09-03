#modules
import mysql.connector as connector, pygame, pygame.freetype, sys, pymunk



#setup
pygame.init()
pygame.freetype.init()
screen = pygame.display.set_mode((1080, 720))
clock = pygame.time.Clock()
usfont = pygame.freetype.SysFont("Arial", 20)
passfont = pygame.freetype.SysFont("Arial", 20)
bartext = pygame.freetype.SysFont("Arial", 20)
bartext2 = pygame.freetype.SysFont("Arial", 20)
submittext = pygame.freetype.SysFont("Arial", 20)

connection = connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Tweedinosdiedansen2!",
    database = "flipper"
)
cursor = connection.cursor()
connection.autocommit = True

space = pymunk.Space()
space.gravity = 0,-10
body = pymunk.Body()
body.position = 50,100
poly = pymunk.Poly.create_box(body)
poly.mass = 10
space.add(body,poly)


#var
running = True
logged_in = False
typinguser = False
typingpass = False
exists = False
usertext = ""
passtext = ""
user = ""
ball_launched = False
balls_left = 3
score = 0
highscore = 0



#classes



#functions
def loginscreen():
    screen.fill("black")
    usfont.render_to(screen, (540,50), "Username:", "white")
    passfont.render_to(screen, (540,200), "Password:", "white")
    pygame.draw.rect(screen, "white", (505,100,150,40), 100)
    bartext.render_to(screen, (513,115), usertext, "black")
    pygame.draw.rect(screen, "white", (505,250,150,40), 100)  
    bartext2.render_to(screen, (513,265), passtext, "black")
    urect = pygame.Rect(505,100,150,40)
    prect = pygame.Rect(505,250,150,40)
    pygame.draw.rect(screen, "white", (505,500,150,40), 100)
    submittext.render_to(screen, (555,510), "Login", "black")
    srect = pygame.Rect(505,500,150,40)

    return urect, prect, srect



#main
while running:
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not logged_in:
            if urect.collidepoint(event.pos):
                typinguser = True
                typingpass = False
                usertext = ""
            if prect.collidepoint(event.pos):
                typingpass = True
                typinguser = False
                passtext = ""
            if srect.collidepoint(event.pos) and usertext != "" and passtext != "":
                exists = False
                cursor.execute("select * from users")
                result = cursor.fetchall()
                for row in result:
                    if row[0] == usertext and row[1] == passtext:
                        logged_in = True
                        exists = True
                
                if not exists:
                    cursor.execute("insert into users(username, password) values(%s, %s)", (usertext, passtext))
                    logged_in = True
            
        if event.type == pygame.KEYDOWN and not logged_in:
            if typinguser:
                print(usertext)
                if event.key == pygame.K_RETURN:
                    typinguser = False
                if event.key == pygame.K_BACKSPACE:
                    usertext = usertext[:-1]
                elif len(usertext) < 15:
                    usertext += event.unicode
            if typingpass:
                if event.key == pygame.K_RETURN:
                    typingpass = False
                if event.key == pygame.K_BACKSPACE:
                    passtext = passtext[:-1]
                elif len(passtext) < 15:
                    passtext += event.unicode

    if logged_in == False:
        urect, prect, srect = loginscreen()
        print(typinguser, usertext, typingpass)
    
    if logged_in == True:
        ball = pygame.draw.circle(screen, "white")
        

    dt = clock.tick(60)/1000
    space.step(dt)
    pygame.display.update()


pygame.quit()
sys.exit()
cursor.close()