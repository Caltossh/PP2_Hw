import pygame
import sys
import random
import pygame_menu


pygame.init()

background = pygame.image.load('materials3/snake2.png')

SIZE_BLOCK = 20
WHITE = (255, 255, 255)
FRAME_COLOR = (0, 255, 204)
HEADER_COLOR = (0, 204, 153)
SNAKE_COLOR = (0, 102, 0)
COUNT_BLOCKS = 20
BLUE = (204,255,255)
RED = (224, 0, 0)
MARGIN = 1
HEADER_MARGIN = 70

size = [SIZE_BLOCK*COUNT_BLOCKS+2*SIZE_BLOCK+MARGIN*COUNT_BLOCKS, 
        SIZE_BLOCK*COUNT_BLOCKS+2*SIZE_BLOCK+MARGIN*COUNT_BLOCKS+HEADER_MARGIN]
screen = pygame.display.set_mode(size)
timer = pygame.time.Clock()
courier = pygame.font.SysFont('courier', 36, 1)


class SnakeBlock:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def is_inside(self):
        return 0<=self.x<COUNT_BLOCKS and 0<=self.y<COUNT_BLOCKS
    
    def __eq__(self, other):
        return isinstance(other, SnakeBlock) and self.x == other.x and self.y == other.y





def draw_block(color, row, column):
    pygame.draw.rect(screen, color, [SIZE_BLOCK+column*SIZE_BLOCK + MARGIN*(column),
                                              HEADER_MARGIN+SIZE_BLOCK+row*SIZE_BLOCK + MARGIN*(row), 
                                              SIZE_BLOCK, SIZE_BLOCK])


def start_the_game():

    def get_random_empty_block():
        x = random.randint(0, COUNT_BLOCKS-1)
        y = random.randint(0, COUNT_BLOCKS-1)
        empty_block = SnakeBlock(x, y)
        while empty_block in snake_blocks:
            empty_block.x = random.randint(0, COUNT_BLOCKS-1)
            empty_block.y = random.randint(0, COUNT_BLOCKS-1)
        return empty_block


    snake_blocks = [SnakeBlock(9,9), SnakeBlock(9, 10), SnakeBlock(9, 11)]
    apple = get_random_empty_block()

    d_row = 0
    d_col = 1
    total = 0
    speed = 1

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('exit')
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and d_col!=0:
                    d_row = -1
                    d_col = 0
                elif event.key == pygame.K_DOWN and d_col!=0:
                    d_row = 1
                    d_col = 0
                elif event.key == pygame.K_RIGHT and d_row!=0:
                    d_row = 0
                    d_col = 1
                elif event.key == pygame.K_LEFT and d_row!=0:
                    d_row = 0
                    d_col = -1

        screen.fill(FRAME_COLOR)
        pygame.draw.rect(screen, HEADER_COLOR, [0, 0, size[0], HEADER_MARGIN])

        text_total = courier.render(f"Total: {total}", 1, WHITE)
        text_speed = courier.render(f"Speed: {speed}", 1, WHITE)
        screen.blit(text_total, (SIZE_BLOCK, SIZE_BLOCK))
        screen.blit(text_speed, (SIZE_BLOCK+230, SIZE_BLOCK))

        for row in range(COUNT_BLOCKS):
            for column in range(COUNT_BLOCKS):

                if (row+column)%2==0:
                    color = BLUE
                else:
                    color = WHITE 

                draw_block(color, row, column)

        head = snake_blocks[-1]
        if not head.is_inside():
            print('crash')
            break
            # pygame.quit()
            # sys.exit()

        draw_block(RED, apple.x, apple.y)
        for block in snake_blocks:
            # x, y = block
            draw_block(SNAKE_COLOR, block.x, block.y)

        if apple == head: 
            total+=1
            speed = total//3 + 1
            snake_blocks.append(apple)
            apple = get_random_empty_block()
        
        new_head = SnakeBlock(head.x + d_row, head.y + d_col)


        if new_head in snake_blocks:
            print('crash yourself')
            break

        snake_blocks.append(new_head)
        snake_blocks.pop(0)

        pygame.display.flip()
        timer.tick(3+speed)





menu = pygame_menu.Menu('Snake', 400, 300, theme=pygame_menu.themes.THEME_GREEN.set_background_color_opacity(1))

menu.add.text_input('Name :', default='Player')
menu.add.button('Play', start_the_game)
menu.add.button('END', pygame_menu.events.EXIT)

while True:

    screen.blit(background, (0, 0))

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    if menu.is_enabled():
        menu.update(events)
        menu.draw(screen)

    pygame.display.update()