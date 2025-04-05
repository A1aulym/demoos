import pygame
import datetime
import sys

pygame.init()
W, H = 800, 600
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Часы Микки Мауса")

# Загрузка изображений из папки images
background = pygame.image.load("images/clock.png")
minute_hand = pygame.image.load("images/min_hand.png")
second_hand = pygame.image.load("images/sec_hand.png")

# Центр вращения стрелок
center = (400, 300)

clock = pygame.time.Clock()

# Функция поворота и отображения стрелки
def blitrot(surf, image, pos, angle):
    rotated = pygame.transform.rotate(image, angle)
    new_rect = rotated.get_rect(center=pos)
    surf.blit(rotated, new_rect)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Получаем текущее время
    now = datetime.datetime.now()
    
    # Углы поворота стрелок (по часовой стрелке → отрицательные)
    second_angle = -now.second * 6
    minute_angle = -(now.minute * 6 + now.second * 0.1)

    # Отрисовка
    sc.fill((255, 255, 255))
    sc.blit(background, (0, 0))

    blitrot(sc, minute_hand, center, minute_angle)
    blitrot(sc, second_hand, center, second_angle)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
