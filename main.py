import pygame  # Импорт модуля пайгейм
import random
pygame.init()

ping = pygame.mixer.Sound('20725-otskok-puli-skorrektirovalos-napravlenie.mp3')
loose = pygame.mixer.Sound('20725-otskok-puli-skorrektirovalos-napravlenie.mp3')
pygame.mixer.music.load('muzyka-na-zadniy-fon-zadniy-fon.mp3')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)


width = 1366
height = 768
fps = 60
gameName = 'First Project'

screen = pygame.display.set_mode((width, height))  # Создание экрана с заданными размера

rounds = 3

def draw_text(screen, text, size, x, y, color):
    font_name = pygame.font.match_font('arial')
    font = pygame.font.Font(font_name,size)
    text_image = font.render(text, True, color)
    text_rect = text_image.get_rect()
    text_rect.center = (x,y)
    screen.blit(text_image, text_rect)

score = 0

BLACK = '#000000'
WHITE = '#FFFFFF'
RED = '#FF0000'
GREEN = '#008000'
BLUE = '#0000FF'
CYAN = '#00FFFF'

img = pygame.image.load('img.png')
img = pygame.transform.scale(img, (50, 50))
img_rect = img.get_rect()

platform = pygame.image.load('platform.png')
platform_rect = platform.get_rect()

platform_rect.x = width / 2 - platform.get_width() / 2
platform_rect.y = height - 60

speedX = 10
speedY = 10

clock = pygame.time.Clock()
run = True
while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    key = pygame.key.get_pressed()

    screen.fill(CYAN)
    screen.blit(img, img_rect)
    screen.blit(platform, platform_rect)

    img_rect.x += speedX
    img_rect.y += speedY

    if key[pygame.K_LEFT] and platform_rect.left > 0:
        platform_rect.x -= 10
    if key[pygame.K_RIGHT] and platform_rect.right < width:
        platform_rect.x += 10





    if img_rect.colliderect(platform_rect):
        speedY = -speedY

    if img_rect.top < 0:
        speedY = -speedY
    if img_rect.left < 0:
        speedX = -speedX
    if img_rect.right > width:
        speedX = -speedX
    if img_rect.bottom > height:
        img_rect.x = random.randint(100, width - 100)
        img_rect.y = 100
        #run = False

    pygame.display.update()
pygame.quit()