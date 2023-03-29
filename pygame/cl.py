import pygame
import datetime
import math


pygame.init()
screen = pygame.display.set_mode((800, 800))


min = pygame.image.load('images/minute.png')
minrec = min.get_rect()
min = pygame.transform.scale(min, (400,400))
minrec.center=(392,388)

sec = pygame.image.load('images/second.png')
secrec = sec.get_rect()
sec = pygame.transform.scale(sec, (400,400))
secrec.center=(392,388)



currt=datetime.datetime.now()
seccnt=currt.second
mincnt=currt.minute


clock = pygame.time.Clock()
done = False



def convert_degrees(R, alpha):
    x=math.sin(math.pi*alpha/180)*R
    y=math.cos(math.pi*alpha/180)*R
    return x+400-10, 400-y-15



def print_text(text, position):
    font = pygame.font.SysFont('Castellar', 40, True, False)
    surface = font.render(text, True, (0, 0, 0))
    screen.blit(surface, position)


while not done:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True



    screen.fill((255, 255, 255))


    pygame.draw.circle(screen, (0, 0, 0), (400, 400), 400, 4)
    

    for number in range(1, 13):
        print_text(str(number), convert_degrees(380, number*30))
   


    sec1=pygame.transform.rotate(sec, -1*(6*seccnt+180))
    secrec1=sec1.get_rect()
    secrec1.center=secrec.center
    screen.blit(sec1, secrec1)


    min1=pygame.transform.rotate(min, -1*(6*mincnt))
    minrec1=min1.get_rect()
    minrec1.center=minrec.center
    screen.blit(min1, minrec1)



    currt=datetime.datetime.now()
    seccnt=currt.second
    seccnt-=30
    mincnt=currt.minute
    mincnt-=15

    # R=250
    # alpha = 90
    # pygame.draw.line(screen, (255, 255, 255), (400, 400), convert_degrees(R, alpha), 4)

    # R=350
    # alpha = 10
    # line = pygame.draw.line(screen, (255, 0, 0), (400, 400), convert_degrees(R, alpha), 4)
    # line = pygame.transform.rotate(line, 6)

    pygame.display.update()
    clock.tick(60)