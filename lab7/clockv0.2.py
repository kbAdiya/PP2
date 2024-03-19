import pygame
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((829, 836))
pygame.display.set_caption("Micky_clock")
bg_image = pygame.image.load('C:\\Users\\Lenovo\\Desktop\\python\\lab7\\imgs\\pictureMicrosoftTeams-image (1).png')
sec_img = pygame.image.load('C:\\Users\\Lenovo\\Desktop\\python\\lab7\\imgs\\MicrosoftTeams-image.png')
min_img = pygame.image.load('C:\\Users\\Lenovo\\Desktop\\python\\lab7\\imgs\\hourMicrosoftTeams-image (2).png')
rect = bg_image.get_rect(center=(415, 418))

while True:
    screen.blit(bg_image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    time = datetime.now().time()

    sec_angle = 90-(time.second * 6)
    nsec_img = pygame.transform.rotate(sec_img, sec_angle)
    sec_rect = nsec_img.get_rect(center=rect.center)
    screen.blit(nsec_img, sec_rect.topleft)

    min_angle = 90 - (time.minute*6)
    nmin_img = pygame.transform.rotate(min_img, min_angle)
    min_rect = nmin_img.get_rect(center=rect.center)
    
    screen.blit(nmin_img, min_rect)

    pygame.display.flip()