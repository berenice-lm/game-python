import pygame

pygame.init()

clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 432

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Parallax")

#define game variables
scroll = 0

bg_images = []
for i in range(1, 6):
    bg_image = pygame.image.load(f'map/forest_{i}.png').convert_alpha()
    bg_image_size = pygame.transform.scale(bg_image, (600,SCREEN_HEIGHT))
    bg_images.append(bg_image_size)
    
bg_width = bg_images[0].get_width()

def draw_bg():
    for x in range(5):
        speed = 1
        for i in bg_images:
            screen.blit(i, ((x * bg_width) - scroll * speed, 0))
            speed += 0.2

run = True
while run:

    clock.tick(FPS)

    draw_bg()

    #get key pressed
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and scroll > 0:
        scroll -= 5
    if key[pygame.K_RIGHT] and scroll < 300:
        scroll += 5

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()