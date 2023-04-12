import pygame
import os
pygame.init()
os.chdir('/Users/saltanateszan/Desktop/pygame9lab')

screen = pygame.display.set_mode((1080, 1000))

clock = pygame.time.Clock()

RED = ('Red')
GREEN = ('Green')
BLUE = ("Blue")
WHITE = ('White')
BLACK = ('Black')
colors = [RED, GREEN, BLUE]
color = WHITE

eraser = pygame.image.load('materials/lastik.png')
eraser = pygame.transform.scale(eraser, (70, 70))

def draw_rect(index):
    pygame.draw.rect(screen, colors[index], (index*40, 0, 40, 40))

def pick_color():
    click = pygame.mouse.get_pressed()
    x, y = pygame.mouse.get_pos()
    if click[0]:
        if 0<=x<=40 and 0<=y<=40:
            return RED
        elif 40<x<=80 and 0<=y<=40:
            return GREEN
        elif 80<x<=120 and 0<=y<=40:
            return BLUE
        elif 1010<=x<=1080 and 0<=y<=40:
            return BLACK
        elif 130<=x<=170 and 0 <= y <= 40:
            return "rect"
    return color

def painting(color):
    click = pygame.mouse.get_pressed()
    x, y = pygame.mouse.get_pos()
    if click[0] and not (0<=x<=400 and 0<=y<=90):
        if mode == 'circle':
            pygame.draw.circle(screen, color, (x, y), 27)
        if mode == 'rect':
            pygame.draw.rect(screen, color, (x, y, 40, 40), 4)
        if mode == 'right_triangle':
            pygame.draw.polygon(screen, color, ((x, y), (x, y+40), (x+40, y+40)), 3)
        if mode == 'equal_triangle':
            pygame.draw.polygon(screen, color, ((x,y), (x+20, y-40), (x+40, y)))
        if mode == 'rhomb':
            pygame.draw.polygon(screen, color, ((x, y), (x+20, y-20), (x+40, y), (x+20, y+20)))

mode = 'circle'

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    
    for i in range(len(colors)):
        draw_rect(i)
    screen.blit(eraser, (1010, 0))
    rect = pygame.draw.rect(screen, WHITE, (130, 0, 40, 40), 3)
    circle = pygame.draw.circle(screen, WHITE, (197, 20), 23, 3)
    right = pygame.draw.polygon(screen, WHITE, ((230, 0), (230, 40), (270, 40)), 3)
    equal = pygame.draw.polygon(screen, WHITE, ((280, 40), (300, 0), (320, 40)), 3)
    rhomb = pygame.draw.polygon(screen, WHITE, ((330, 20), (350,0), (370, 20), (350, 40)), 3)

    pos = pygame.mouse.get_pos()
    print(mode)
    if rect.collidepoint(pos):
        mode = "rect"
    if circle.collidepoint(pos):
        mode = "circle"
    if right.collidepoint(pos):
        mode = 'right_triangle'
    if equal.collidepoint(pos):
        mode = 'equal_triangle'
    if rhomb.collidepoint(pos):
        mode = 'rhomb'

    # pygame.draw.rect(screen, WHITE, (130, 0, 40, 40), 4)

    color = pick_color()
    painting(color)


    clock.tick(370)
    pygame.display.update()