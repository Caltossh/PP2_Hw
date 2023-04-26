import pygame, sys, random
from pygame.math import Vector2
from pygame import Rect
import numpy as np
import time
from functions import create_tables, add_new_user, add_new_user_score, get_user_id, update_user_score, check_user_exists
from util_functions import get_body_list, get_level, get_map



fps = 60
cell_size = 30
row_number = 20
col_number = 30
screen_size = (cell_size * col_number, cell_size * row_number)
speed = 150
level = 1

# initializing pygame module
pygame.init()
# initialzing screen object
screen = pygame.display.set_mode(screen_size)
# initializing clock object
clock = pygame.time.Clock()
game_font = pygame.font.Font('./assets/Blessed.ttf', 20)
is_paused = False




# Class inherited from Sprite for Fruit object
class Fruit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.time = 60
        self.value = random.randint(1, 5)
        self.randomize()

    # drawing fruit
    def draw(self, surf): 
        surf.blit(self.image, self.rect)

    # update remaining fruit's time to live 
    def update(self):
        self.time -= 1

    # randomly placing fruit
    def randomize(self):
        self.time = 60
        self.value = random.randint(1, 5)
        self.pos = Vector2(random.randint(1, col_number - 1), random.randint(1, row_number - 1))
        self.image = pygame.transform.scale(pygame.image.load(f'./assets/fruit_{self.value}.png'), (cell_size, cell_size))
        # create rectangle
        self.rect = Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)



# Sprite class inherited from pygame Sprite for Snake 
class Snake(pygame.sprite.Sprite):
    # Initializing snaek
    def __init__(self, body_list = None):
        super().__init__()
        # list that holds all snake body parts
        if body_list is None:
            self.pos_list = [Vector2(8, 10), Vector2(7, 10), Vector2(6, 10)]
        else:
            self.pos_list = body_list
        # direction attribute for moving in a specific direction
        self.direction = Vector2(1,0)

        # many attributes for different parts of snake for smooth visualization
        self.head_up = pygame.transform.scale(pygame.image.load("./assets/head.png"), (cell_size, cell_size))
        self.head_down = pygame.transform.scale(pygame.image.load("./assets/head_down.png"), (cell_size, cell_size))
        self.head_right = pygame.transform.scale(pygame.image.load("./assets/head_right.png"), (cell_size, cell_size))
        self.head_left = pygame.transform.scale(pygame.image.load("./assets/head_left.png"), (cell_size, cell_size))

        self.tail_up = pygame.transform.scale(pygame.image.load("./assets/tail.png"), (cell_size, cell_size))
        self.tail_down = pygame.transform.scale(pygame.image.load("./assets/tail_down.png"), (cell_size, cell_size))

        self.tail_right = pygame.transform.scale(pygame.image.load("./assets/tail_right.png"), (cell_size, cell_size))
        self.tail_left = pygame.transform.scale(pygame.image.load("./assets/tail_left.png"), (cell_size, cell_size))

        self.body_vertical = pygame.transform.scale(pygame.image.load("./assets/body_vrt.png"), (cell_size, cell_size))
        self.body_horizontal = pygame.transform.scale(pygame.image.load("./assets/body_hr.png"), (cell_size, cell_size))


        self.body_tr = pygame.transform.scale(pygame.image.load("./assets/body_tr.png"), (cell_size, cell_size))
        self.body_tl = pygame.transform.scale(pygame.image.load("./assets/body_tl.png"), (cell_size, cell_size))
        self.body_br = pygame.transform.scale(pygame.image.load("./assets/body_br.png"), (cell_size, cell_size))
        self.body_bl = pygame.transform.scale(pygame.image.load("./assets/body_bl.png"), (cell_size, cell_size))

        self.head = self.head_right
        self.tail = self.tail_right
        
        # sound attributed for fruit eating sound
        self.sound = pygame.mixer.Sound('./assets/munch.mp3')
        # snake speed attribute
        self.speed = speed



       
    # drawing snake 
    def draw(self, surf):
        for i, pos in enumerate(self.pos_list):   
            # Rect for positioning
            rect = Rect(int(pos.x * cell_size), int(pos.y * cell_size), cell_size, cell_size)
            # comples drawing of snake based on many different conditions
            if i == 0:
                self.update_head_graphics()
                surf.blit(self.head, rect)
            elif i == len(self.pos_list) - 1:
                self.update_tail_graphics()
                surf.blit(self.tail, rect)
            else:
                prev_pos = self.pos_list[i+1] - pos
                next_pos = self.pos_list[i-1] - pos
                
                if prev_pos.y == next_pos.y:
                    surf.blit(self.body_vertical, rect)
                elif prev_pos.x == next_pos.x:
                    surf.blit(self.body_horizontal, rect)
                else:
                    if prev_pos.x == -1 and next_pos.y == -1 or prev_pos.y == -1 and next_pos.x == -1:
                        surf.blit(self.body_tl, rect)
                    if prev_pos.x == -1 and next_pos.y == 1 or prev_pos.y == 1 and next_pos.x == -1:
                        surf.blit(self.body_bl, rect)
                    if prev_pos.x == 1 and next_pos.y == -1 or prev_pos.y == -1 and next_pos.x == 1:
                        surf.blit(self.body_tr, rect)
                    if prev_pos.x == 1 and next_pos.y == 1 or prev_pos.y == 1 and next_pos.x == 1:
                        surf.blit(self.body_br, rect)


    # method for moving snake
    def move(self):
        # copy the list of snake body parts
        pos_list_copy = self.pos_list[:-1]
        # add additional element at the end of the snake
        pos_list_copy.insert(0, pos_list_copy[0] + self.direction)
        # assign the modified list to the attribute list
        self.pos_list = pos_list_copy

    # snake eating fruit and increasing its size by 1
    def eat(self, fruit_value):
        # settings speed for global speed variable
        self.speed = speed
        pos_list_copy = self.pos_list[:]
        for i in range(fruit_value):
            last_index = len(pos_list_copy) - 1
            pos_list_copy.insert(last_index, pos_list_copy[last_index] + self.direction)
        self.pos_list = pos_list_copy
        # setting a limit of the snake's speed
        #if(self.speed > 100):
            #self.speed = self.speed - 10 * level

        pygame.time.set_timer(screen_update, self.speed)

    # updating snake head graphics for correct visuals depending on the direction of snake
    def update_head_graphics(self):
        if self.direction == Vector2(0, -1):
            self.head = self.head_up
        elif self.direction == Vector2(0, 1):
            self.head = self.head_down   
        elif self.direction == Vector2(1, 0):
            self.head = self.head_right    
        elif self.direction == Vector2(-1, 0):
            self.head = self.head_left

    # updating tail graphics depending on the tail position and direction
    def update_tail_graphics(self):
        tail_direction = self.pos_list[-2] - self.pos_list[-1]
        
        if tail_direction == Vector2(0, -1):
            self.tail = self.tail_up
        if tail_direction == Vector2(0, 1):
            self.tail = self.tail_down
        if tail_direction == Vector2(1, 0):
            self.tail = self.tail_right
        if tail_direction == Vector2(-1, 0):
            self.tail = self.tail_left

    # playing eating sound
    def play_sound(self):
        self.sound.play()

    # reset method in the case of game over
    def reset(self):
        self.pos_list = [Vector2(8, 10), Vector2(7, 10), Vector2(6, 10)]
        self.speed = 150
        pygame.time.set_timer(screen_update, self.speed)




       


# Class with general logic of the game
class GameLogic(pygame.sprite.Sprite):
    # initializing snake and fruit instances
    def __init__(self, user_name, snake_body_list, map):
        super().__init__()
        self.user_name = user_name
        if snake_body_list == []:
            self.snake = Snake(body_list = [Vector2(8, 10), Vector2(7, 10), Vector2(6, 10)])
        else:
            self.snake = Snake(body_list = snake_body_list)
        self.fruit = Fruit()
        self.level = level
        if map == []:
            self.map = np.ones((col_number, row_number))
            self.map[1:-1, 1:-1] = np.random.choice([0, 1], size = (col_number-2, row_number-2), p=[(100 - 2 * self.level)/100, self.level * 2/100])
        else:
            self.map = map
        self.walls_list = []
        self.score = len(self.snake.pos_list) - 3
        self.death = False
        self.death_sound = pygame.mixer.Sound('./assets/death_sound.mp3')
        self.user_id = get_user_id(user_name)
        add_new_user_score(self.user_id, self.level, self.score)
        open(f'./progress_data/{self.user_name}_data.txt', 'w').close()


    # updating the state of the game
    def update(self):
        open(f'./progress_data/{self.user_name}_data.txt', 'w').close()
        self.score = len(self.snake.pos_list) - 3
        self.level = level
        self.check_collision()
        self.snake.move()
        self.fruit.update()
        update_user_score(self.user_id, self.level, self.score)
        if self.fruit.time <= 0:
            self.fruit.randomize()
        self.check_fail_states()



    # drawing game elements
    def draw_elements(self, surf, font, score_text):
        if not self.death:
            self.draw_dirt(surf)
            self.draw_walls(surf)
            self.snake.draw(surf)
            self.fruit.draw(surf)
            self.draw_score(surf, score_text, font)
        else:
            self.draw_death_screen()

    # checking for collision of snake with fruit
    def check_collision(self):
        # if snake eats the fruit
        if self.fruit.pos == self.snake.pos_list[0]:
            self.fruit.randomize()
            self.snake.eat(self.fruit.value)
            self.snake.play_sound()

        # if fruit spawns somewhere inside the snake
        for pos in self.snake.pos_list:
            if pos == self.fruit.pos:
                self.fruit.randomize()

        # is fruit spawns somewhere inside the walls
        for wall in self.walls_list:
            if wall == self.fruit.pos:
                self.fruit.randomize()

    # method running game over case
    def game_over(self):
        # global speed 
        # speed = 150
        # self.level = 1
        # self.snake.reset()
        # self.randomize_map()
        self.death = True
        if self.death:
            open(f'./progress_data/{self.user_name}_data.txt', 'w').close()
            update_user_score(self.user_id, self.level, self.score)



    def randomize_map(self):
        self.map[1:-1, 1:-1] = np.random.choice([0, 1], size = (col_number-2, row_number-2), p=[(100 - 2 * self.level)/100, self.level * 2/100])

    # method for checking all game over states
    def check_fail_states(self):
        # checking if snake goes outside of the screen
        if not 0 <= self.snake.pos_list[0].x < col_number or not 0 <=  self.snake.pos_list[0].y < row_number:
            self.game_over()
            self.level = 1

        # checking if snake head collides with itself
        for snake_part in self.snake.pos_list[1:]:
            if snake_part == self.snake.pos_list[0]:
                self.game_over()
                self.level = 1
        # if snake hits walls
        for wall in self.walls_list:
            if wall == self.snake.pos_list[0]:
                self.game_over()
                self.level = 1

    # method for drawing score on the screen
    def draw_score(self, surf, score_text, font):
        score_text = f"""{len(self.snake.pos_list) - 3} / {self.level} lvl"""
        score_surf = font.render(score_text, True, (255, 0 , 0))
        score_surf_pos = (int(cell_size * col_number - 40), int(cell_size * row_number - 20))
        score_rect = score_surf.get_rect(center = score_surf_pos)
        surf.blit(score_surf, score_rect)
        apple = self.fruit.image
        apple_rect = apple.get_rect(midright = (score_rect.left, score_rect.centery))
        surf.blit(apple, apple_rect)

    # method for drawing dirt on the ground
    def draw_dirt(self, surf):
        dirt_color = (150, 105, 65)
        for row in range(row_number):
            if row % 2 == 0:
                for col in range(0, col_number, 2):
                    dirt_rect = Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                    pygame.draw.rect(surf, dirt_color, dirt_rect)
            else:
                for col in range(1, col_number, 2):
                    dirt_rect = Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                    pygame.draw.rect(surf, dirt_color, dirt_rect)
    # method for drawing walls
    def draw_walls(self, surf):
        wall_img = pygame.image.load('./assets/wall.png')
        wall_img = pygame.transform.scale(wall_img, (cell_size, cell_size))
        wall_rect = wall_img.get_rect()
        for i, y in enumerate(self.map):
            for j, x in enumerate(y):
                if x == 1:
                    self.walls_list.insert(0, Vector2(i, j))
                    wall_rect.topleft = (i * cell_size, j * cell_size)
                    surf.blit(wall_img, wall_rect)

    def draw_death_screen(self):
        death_screen = pygame.transform.scale(pygame.image.load('./assets/death_screen.jpeg'), screen_size)
        death_text = f"Your level: {level}"
        death_surf = game_font.render(death_text, True, (255, 0, 0))
        death_surf_rect = death_surf.get_rect(center = (450, 400))
        screen.blit(death_screen, (0, 0))
        screen.blit(death_surf, death_surf_rect)
        self.death_sound.play()


    def save_progress(self):
        with open(f"./progress_data/{self.user_name}_data.txt", 'w') as file:
            file.write(f'user_name={self.user_name}\n')
            file.write(f'level={self.level}\n')
            file.write(f'score={self.score}\n')
            file.write(f'map=[')
            for c in self.map[0]:
                file.write(f'{c} ')
            file.write(f']\n')
            for i, row in enumerate(self.map):
                if i == 0:
                    continue
                file.write('[')
                for j, column in enumerate(row):
                    file.write(f'{column} ')
                file.write(']\n')
            file.write(f'body_list={self.snake.pos_list}\n')

    
    def pause(self):
        global is_paused
        font = pygame.font.SysFont('comicsansms', 100)
        text_surf = font.render("""Paused""", True, (0, 0, 0))
        text_rect = text_surf.get_rect()
        text_rect.center = (screen_size[0] // 2, screen_size[1] // 2)

        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.save_progress()
                    update_user_score(self.user_id, self.level, self.score)
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        is_paused = not is_paused
        screen.blit(text_surf, text_rect)
        

        pygame.display.flip()
        clock.tick(fps)  








            
# main method of the game
def main():
    global level, speed, is_paused
    # create tables
    create_tables()

    user_name = input("Enter the username: ")
    isPresent = check_user_exists(user_name)
    user = add_new_user(user_name)

    filename = f'./progress_data/{user_name}_data.txt'
    snake_game = None
    if isPresent > 0:
        level = int(get_level(filename))
        body_list = get_body_list(filename)
        body_list = [Vector2(pos[0], pos[1]) for pos in body_list]
        map = get_map(filename)
        snake_game = GameLogic(user_name, map = get_map(filename), snake_body_list=body_list)
    else:
        snake_game = GameLogic(user_name)


    
    # initialzing the general game logic 
    # adding font for score
    game_font = pygame.font.Font('./assets/Blessed.ttf', 20)

    # screen update for checking every user event to 
    global screen_update
    screen_update = pygame.USEREVENT
    # setting timer on user event for artificial laggy gameplay
    pygame.time.set_timer(screen_update, speed)
    while True:
        # running for every user input
        for event in pygame.event.get():
            # quit event type
            if event.type == pygame.QUIT:
                snake_game.save_progress()
                update_user_score(snake_game.user_id, snake_game.level, snake_game.score)
                pygame.quit()
                sys.exit()
            # updating the game on each user event
            if event.type == screen_update:
                snake_game.update()
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_UP:
                        if snake_game.snake.direction != Vector2(0, 1):
                            snake_game.snake.direction = Vector2(0, -1)
                    case pygame.K_DOWN:
                        if snake_game.snake.direction != Vector2(0, -1):
                            snake_game.snake.direction = Vector2(0, 1)
                    case pygame.K_RIGHT:
                        if snake_game.snake.direction != Vector2(-1, 0):
                            snake_game.snake.direction = Vector2(1, 0)
                    case pygame.K_LEFT:
                        if snake_game.snake.direction != Vector2(1, 0):
                            snake_game.snake.direction = Vector2(-1, 0)
                    case pygame.K_p:
                        is_paused = not is_paused
                        snake_game.pause()
        # calculating the score
        score = str(len(snake_game.snake.pos_list) - 3)
        # increasing level and resetting the game
        if int(score) >= 10:
            level += 1
            speed -= 25
            snake_game.kill()
            snake_game = GameLogic(user_name)
        screen.fill((173, 121, 75))
        snake_game.draw_elements(screen, game_font, score)
        pygame.display.update()
        clock.tick(fps)



if __name__ == "__main__":
    main()
