import pygame
import os

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((900,300))
pygame.display.set_caption("Apple music")

path = os.listdir("/Users/saltanateszan/Desktop/docs/ppII/pygame")


# play_list = []
# for music in path:
#     if music.endswith(".mp3"):
#         play_list.append(music)
music_dir = "sounds"
play_list = [os.path.join(music_dir, f) for f in os.listdir(music_dir) if f.endswith(".mp3")]


id=0
os.chdir("/Users/saltanateszan/Desktop/docs/ppII/pygame")
pygame.mixer.music.load(play_list[id])
pygame.mixer.music.play()
pygame.mixer.music.pause()



clock = pygame.time.Clock()


done = False
play = False


bg = pygame.image.load('images/background.jpg')
bg = pygame.transform.scale(bg, (900, 300))


prev = pygame.image.load('sounds/prev.png')
playbt = pygame.image.load('sounds/play.png')
stop = pygame.image.load('sounds/stop.png')
next = pygame.image.load('sounds/next.png')


prev = pygame.transform.scale(prev, (130, 130))
playbt = pygame.transform.scale(playbt, (105, 105))
stop = pygame.transform.scale(stop, (100, 120))
next = pygame.transform.scale(next, (130, 130))

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        

        if event.type == pygame.KEYUP:


            if event.key == pygame.K_RIGHT:
                id+=1
                pygame.mixer.music.stop()
                pygame.mixer.music.load(play_list[id])
                print("Curently playing: ", play_list[id])
                pygame.mixer.music.play()
                play=True
            

            if not play and event.key == pygame.K_SPACE:
                play = True
                pygame.mixer.music.unpause()



            elif play and event.key == pygame.K_SPACE:
                play = False
                pygame.mixer.music.pause()


    font = pygame.font.SysFont(None, 24)     
    text = font.render('Currently playing:   ' + play_list[id][:-4], True, 'WHITE')

   

    screen.blit(bg, (0, 0))
    screen.blit(text, (300,100))
    screen.blit(prev, (150,160))
    screen.blit(playbt, (295,167))
    screen.blit(stop, (425,159))
    screen.blit(next, (560,160))
    pygame.display.update()
    clock.tick(60)



    