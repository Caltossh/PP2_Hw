
#Imports
import pygame, sys
from pygame.locals import *
import random, time
#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCOREenemy = 0
CoinCount = 0
CoinCollected = 0
NewCoin = 1
CoinCheck = 0
music = 0

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load('materials/AnimatedStreet.png')

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load('materials/Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)
        self.speed = 5

      def move(self):
        global SCOREenemy
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            SCOREenemy += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
      def set_speed(self, value):
          self.speed = value


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load('materials/Player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
                  
class Coin(pygame.sprite.Sprite):
    def __init__(self, value):
        super().__init__()
        self.image = pygame.image.load('materials/coins1.webp')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(30, SCREEN_WIDTH - 30), 0)
        self.value = value

    def move(self):
        global CoinCount
        global CoinCollected
        CoinCollected = 0
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
            global CoinCheck
            CoinCheck = 0
        if self.rect.bottom < 100:
            global NewCoin
            NewCoin = 1
    def setCoinValue(self, value):
        self.value = value

def play_music():
    pygame.mixer.music.load('materials/background.wav')
    pygame.mixer.music.play()


def stop_music():
    pygame.mixer.music.stop()


#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coin(random.randint(1,10))

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)


#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)


#Game Loop
while True:
    speed_level = 10
    # Play music at the beginning
    if not music:
        play_music()
        music = 1

    #Cycles through all events occuring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5      
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCOREenemy), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    scores_coin = font_small.render("Coins: " + str(CoinCount), True, BLACK)
    DISPLAYSURF.blit(scores_coin, (SCREEN_WIDTH - 100, 10))


    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
        


    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('materials/crash.wav').play()
          time.sleep(1)
                   
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
          
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        
    
    C1.move()
    
    # If collected coin
    if pygame.sprite.spritecollideany(P1, coins):
        pygame.mixer.Sound('materials/crash.wav').play()
        CoinCheck = 1
        CoinCollected = 1

    # Continue displaying coin if not
    if not CoinCollected:
        for entity in coins:
            DISPLAYSURF.blit(entity.image, entity.rect)
    # Plus score if collected
    else:
        if CoinCheck == 1 and NewCoin == 1:
            CoinCount += C1.value
            C1.setCoinValue(random.randint(1,10))
            NewCoin = 0
            speed_level +=10
    if(CoinCount >= speed_level):
        E1.set_speed(speed_level)

        

    pygame.display.update()
    FramePerSec.tick(FPS)