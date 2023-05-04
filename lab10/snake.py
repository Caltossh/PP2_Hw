import psycopg2
import pygame
import sys
import random
import time
pygame.init()
name = input() # вводим имя перед началом
config = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    user = 'postgres',
    password = 'зщыепкуы'
)
current = config.cursor()
sql = '''
    SELECT * FROM snake WHERE username = %s; 
'''
current.execute(sql, [name])
config.commit()
data = current.fetchone()

if data == None: # создаем начальные данные если игрока нет в базе данных
    sql = '''
        INSERT INTO snake VALUES(%s, 0, 0);
    '''
    current.execute(sql, [name])
    config.commit()
else: # если он уже есть в базе данных, высвечиваем в консоль его последний уровень
    sql = '''
    SELECT score FROM snake WHERE username = %s;
    '''
    current.execute(sql, [name])
    final = current.fetchone()
    print(*final)
    config.commit()


Black = (0,0, 0)
width = 1080
height = 800
move = 40
screen = pygame.display.set_mode((width, height))  
pygame.display.set_caption("snake")
font = pygame.font.SysFont(None, 100)
fond = pygame.font.SysFont(None, 70)
out_font = pygame.font.SysFont(None, move-5)
fffond = pygame.font.SysFont("Verdana", 20)
surf = pygame.Surface((390, 390))

clock = pygame.time.Clock()

def draw_grid():
    for x in range (0, width, move):
        pygame.draw.line(screen, ('White'), (x,move), (x, height), width=1)
    for y in range (move, height, move):
        pygame.draw.line(screen, ('White'), (0, y), (width, y), width=1)

def draw_snake(snake_list):
    # head color is different from body color
    m = 0
    c = ('Yellow')
    for a in snake_list:
        if m == len(snake_list) - 1:
            c = ('Yellow')
        m += 1
        pygame.draw.rect(screen, (c), [a[0], a[1], move, move])
        if c == (40, 244, 100):
            pygame.draw.rect(screen, (('Green')), [a[0] + move/5, a[1] + move/5, move*3/5, move*3/5],width=4)

def generate_food():
# Generate random food with different weights
    food_x = random.randint(0, width/move - 1)
    food_y = random.randint(1, height/move - 1)
    massa = random.choice([1, 2])
    return food_x, food_y, massa

def draw_food(food_x, food_y, massa):
    # here I drew 3 rectangles so that the food is beautiful
    if massa == 1:
        pygame.draw.rect(
            screen,
            color=(255, 19, 60),
            rect=pygame.Rect(
            food_x * move,
            food_y * move, 
            move,
            move,
            ),
        )
    else:
        pygame.draw.rect(
            screen,
            color=(200, 19, 34),
            rect=pygame.Rect(
            food_x * move - massa * 4,
            food_y * move - massa * 4, 
            move + 2*(massa * 3),
            move + 2*(massa * 3),
            ),
        )
    pygame.draw.rect(
        screen,
        color=(255, 255, 255),
        rect=pygame.Rect(
        food_x * move|+ 9 + 6,
        food_y * move + 9 + 6, 
        move - 18 - 12,
        move - 18 - 12,
        ),
    )

def out_score(b, c):
    b = out_font.render(b, True, (189, 189, 189) )
    screen.blit(b, (10, 0+7))
    c = out_font.render(c, True, (189, 189, 189) )
    screen.blit(c, (width - c.get_width() - 10, 0+7))

def loser(a, b, c):
    # цвета
    a = font.render(a, True, (255, 0, 0) )
    b = fond.render(b, True, (0, 0, 255) )
    c = fond.render(c, True, (0, 49, 200) )
    # positions
    screen.blit(a, (width/2 - a.get_width()/2, height/2 - 200))
    screen.blit(b, (width/2 - b.get_width()/2, height/2 ))
    screen.blit(c, (width/2 - c.get_width()/2, height/2 + 60))

def main():
    running = True
    pos_x, pos_y = 400, 400  # start position of snake head
    dx, dy = 0, 0
    # here i give start position to food
    food_x = 5
    food_y = 3
    score = 0
    level = 0
    massa = 1
    snake_speed = 8  # this is start speed of snake
    snake_List = []
    Length_of_snake = 1  # start lenght of snake


    time_event = pygame.USEREVENT
    pygame.time.set_timer(time_event, 1000)
    sec = 0

    while running:
        global paused
        paused = False
        screen.fill((100, 149, 237))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type  == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    dx = 0
                    dy = -1
                elif event.key == pygame.K_DOWN:
                    dx = 0
                    dy = 1
                elif event.key ==pygame.K_LEFT:
                    dx = -1
                    dy = 0
                elif event.key ==pygame.K_RIGHT:
                    dx = 1
                    dy = 0
                elif event.type == pygame.K_SPACE:
                    paused = True
            if event.type == time_event:
                if massa == 2:
                    sec += 1

        # change position according to  dx, dy
        pos_x += dx * move
        pos_y += dy * move

        #  Checking for border collision
        if pos_x >= width or pos_x < 0 or pos_y >= height or pos_y < move:
            running = False
        
        if sec > 6:
            food_x, food_y, massa = generate_food()
            sec = 0

        # check food position and add lenght and level
        if pos_x/move == food_x and pos_y/move == food_y:
            score += massa
            sec = 0
            food_x, food_y, massa = generate_food()
            if Length_of_snake < 2:
                Length_of_snake += 1
        
        level = 1 * int(score/4)
        snake_speed = 8 + level * 2
        if Length_of_snake > 1:
            Length_of_snake = 2 + level

        while paused: 
            clock.tick(snake_speed)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                    paused = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        paused = False # возобнавляем игру
                    if event.key == pygame.K_c:
                        a = score # обновляем текущие данные в базе данных
                        sql = '''
                            UPDATE snake SET score = %s, level = %s WHERE username = %s;
                        '''
                        current.execute(sql, [a, level, name])
                        config.commit()  
            screen.blit(surf, (200, 200))
            cntr = fffond.render(f'Your score is {score}', True, 'white')
            screen.blit(cntr, (315, 350))
            l = fffond.render(f'Your level is {level}', True, 'white')
            screen.blit(l, (317, 385))
            txt = fffond.render(f'Press "C" to save your current state', True, 'white')
            screen.blit(txt, (212, 420))
            pygame.display.flip()


        # length and head
        snake_Head = []
        snake_Head.append(pos_x)
        snake_Head.append(pos_y)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        for x in snake_List[:-1]:
            if x == snake_Head:  # Checking for body collision
                running = False
        for x in snake_List:
            if x[0] == food_x and x[1] == food_y: # Checking  it does not fall on a snake
                check = True
                while check:
                    if x[0] == food_x and x[1] == food_y:
                        food_x = random.randint(1, width/move-1)
                        food_y = random.randint(1, height/move-1)
                    else:
                        check = False

        draw_snake(snake_List)
        draw_grid()
        draw_food(food_x, food_y, massa)
        

        score_mes = f"score: {score}"
        level_mes = f'level: {level}'
        out_score(score_mes, level_mes)  # out counters during the game

        clock.tick(snake_speed)  # speed
        pygame.display.flip()
    
    over_mes = "game over"
    score_mes = f"score: {score}"

    
    screen.fill((100, 149, 237))
    loser(over_mes, score_mes, level_mes)    # game results
    pygame.display.flip()
    time.sleep(3)
    
        

    sql = '''
    UPDATE snake SET score = %s, level = %s WHERE username = %s;
    '''
    current.execute(sql, [score, level, name])
    config.commit()
    current.close()
    config.close()
    quit()

if __name__ == "__main__":
    main()
