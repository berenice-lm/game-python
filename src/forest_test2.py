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
mouse_x, mouse_y = pygame.mouse.get_pos()

bg_images = []
for i in range(1, 6):
    bg_image = pygame.image.load(f'map/forest_{i}.png').convert_alpha()
    bg_image_size = pygame.transform.scale(bg_image, (600, SCREEN_HEIGHT))
    bg_images.append(bg_image_size)

bg_width = bg_images[0].get_width()

def draw_bg():
    for x in range(5):
        speed = 0.2  # Decreased speed for slower movement
        for i in bg_images:
            screen.blit(i, ((x * bg_width) - scroll * speed, 0))
            speed += 0.2  # Adjust this value to control the parallax effect

run = True
while run:

    clock.tick(FPS)

    draw_bg()

    # get mouse position
    new_mouse_x, new_mouse_y = pygame.mouse.get_pos()

    # calculate the difference in mouse position
    mouse_delta = new_mouse_x - mouse_x

    # update scroll based on the mouse movement
    scroll -= mouse_delta * 0.05  # Adjust this value for sensitivity

    # clamp scroll to prevent going out of bounds
    scroll = max(0, min(scroll, 300))

    # update mouse position for the next iteration
    mouse_x, mouse_y = new_mouse_x, new_mouse_y

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()