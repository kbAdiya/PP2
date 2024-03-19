import pygame

pygame.mixer.init()
pygame.init()
screen = pygame.display.set_mode((600, 600))



songs = [
    {"title": "Snooze", "file_path": "C:\\Users\\Lenovo\\Desktop\\python\\lab7\\music\\AGUST_D_BTS_SUGA_Snooze.mp3", "image_path": "C:\\Users\\Lenovo\\Desktop\\python\\lab7\\imgformusic\\st,medium,507x507-pad,600x600,f8f8f8.webp"},
    {"title": "What do you think", "file_path": "C:\\Users\\Lenovo\\Desktop\\python\\lab7\\music\\03 - Agust D - What do you think (128).mp3", "image_path": "C:\\Users\\Lenovo\\Desktop\\python\\lab7\\imgformusic\\загрузка.png"},
    {"title": "Burn It", "file_path": "C:\\Users\\Lenovo\\Desktop\\python\\lab7\\music\\6. Burn It   Agust D feat. MAX.mp3", "image_path": "C:\\Users\\Lenovo\\Desktop\\python\\lab7\\imgformusic\\fposter,small,wall_texture,square_product,600x600.u6.jpg"},
    {"title": "Message Man", "file_path": "C:\\Users\\Lenovo\\Desktop\\python\\lab7\\music\\AMYGDALA.mp3", "image_path": "C:\\Users\\Lenovo\\Desktop\\python\\lab7\\imgformusic\\fposter,small,wall_texture,square_product,600x600.u5.jpg"}
]


current_song_index = 0
pygame.mixer.music.load(songs[current_song_index]["file_path"])
pygame.mixer.music.play()


current_image = pygame.image.load(songs[current_song_index]["image_path"])
current_image = pygame.transform.scale(current_image, (600, 600))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                current_song_index = (current_song_index + 1) % len(songs)
                pygame.mixer.music.load(songs[current_song_index]["file_path"])
                pygame.mixer.music.play()
               
                current_image = pygame.image.load(songs[current_song_index]["image_path"])
                current_image = pygame.transform.scale(current_image, (600, 600))
            elif event.key == pygame.K_LEFT:
                current_song_index = (current_song_index - 1) % len(songs)
                pygame.mixer.music.load(songs[current_song_index]["file_path"])
                pygame.mixer.music.play()
                
                current_image = pygame.image.load(songs[current_song_index]["image_path"])
                current_image = pygame.transform.scale(current_image, (600, 600))
            elif event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

    screen.blit(current_image, (0, 0))
    pygame.display.flip()

pygame.quit()
