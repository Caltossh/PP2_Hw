# import pygame
# pygame.init()
# screen = pygame.display.set_mode((600, 300)) #flags = pygame.NOFRAME
# screen.fill('White')
# pygame.display.set_caption('CIRCLE')
# icon = pygame.image.load('images/circle.png')
# pygame.display.set_icon(icon)

# running = True
# while running:

#     pygame.draw.circle(screen, 'Red', (100, 150), 25)

#     pygame.display.update()
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running == False
#             pygame.quit()

import pygame

pygame.init()
screen = pygame.display.set_mode((800,800))
screen.fill('White')
icon = pygame.image.load('images/circle.png')
pygame.display.set_icon(icon)

clock = pygame.time.Clock()


done = False
x=0
y=0

is_blue = True

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_DOWN] and 400 >= y+77:
        y+=7
    if pressed[pygame.K_UP] and 400 >= -y+77:
        y-=7
    if pressed[pygame.K_LEFT] and 400 >= -x+77:
        x-=7
    if pressed[pygame.K_RIGHT] and 400 >= x+77:
        x+=7

    screen.fill(('White'))
    if is_blue:
        color = ('Red')
    else:
        color = (255, 100, 0)
    pygame.draw.circle(screen, color, (400+x, 400+y), 70)
    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)