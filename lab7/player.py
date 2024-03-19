import pygame

pygame.mixer.init()
pygame.init()
screen = pygame.display.set_mode((600, 600))

songs = [
         "C:\\Users\\Lenovo\\Desktop\\python\\lab7\\music\\AGUST_D_BTS_SUGA_Snooze.mp3",
         "C:\\Users\\Lenovo\\Desktop\\python\\lab7\\music\\03 - Agust D - What do you think (128).mp3",
         "C:\\Users\\Lenovo\\Desktop\\python\\lab7\\music\\6. Burn It   Agust D feat. MAX.mp3",
         "C:\\Users\\Lenovo\\Desktop\\python\\lab7\\music\\AMYGDALA.mp3"]
pygame.mixer.music.load(songs[0])
pygame.mixer.music.play()
i = 0
a = True
background_image = pygame.image.load("C:\\Users\\Lenovo\\Desktop\\python\\lab7\\istockphoto-1175435360-612x612.jpg")
while True:
    screen.blit(background_image,[0,0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                i = (i + 1) % len(songs)
                pygame.mixer.music.load(songs[i])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                i = (i - 1) % len(songs)
                pygame.mixer.music.load(songs[i])
                pygame.mixer.music.play()
            elif event.key == pygame.K_SPACE:
                if a:
                    pygame.mixer.music.stop()
                    a = False
                else:
                    pygame.mixer.music.play()
                    a = True
    pygame.display.flip()