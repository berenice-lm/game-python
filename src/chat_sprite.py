import pygame

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Spritesheets')

BG = (50, 50, 50)
BLACK = (0, 0, 0)

class SpriteSheet():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale, colour):
        image = pygame.Surface((width, height), pygame.SRCALPHA)
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        # Set colorkey to None to keep the black background
        image.set_colorkey(None)

        return image

#create animation list
animation_list = []
animation_steps = [4, 4, 6, 4]
action = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 120
frame = 0
step_counter = 0

sprite_sheet_image = pygame.image.load('sprites/cat/chat_principal.png').convert_alpha()
sprite_sheet = SpriteSheet(sprite_sheet_image)

for animation in animation_steps:
    temp_img_list = []
    for _ in range(animation):
        frame_image = sprite_sheet.get_image(step_counter, 32, 24, 3, BLACK)
        temp_img_list.append(frame_image)
        step_counter += 1
    # Add normal frames to the animation list
    animation_list.append(temp_img_list)
    # Add flipped frames to the animation list
    flipped_animation = [pygame.transform.flip(frame, True, False) for frame in temp_img_list]
    # Set colorkey to None for flipped frames to keep the black background
    flipped_animation = [frame.convert_alpha() for frame in flipped_animation]
    animation_list.append(flipped_animation)

run = True
while run:
    # update background
    screen.fill(BG)

    # update animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(animation_list[action]):
            frame = 0

    # show frame image
    idle_left = 0
    idle_right = 1
    run_left = 2
    run_right = 3
    death_left = 4
    death_right = 5
    roll_left = 6
    roll_right = 7
    screen.blit(animation_list[action][frame], (0, 0))

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and action > 0:
                action -= 1
                frame = 0
            if event.key == pygame.K_UP and action < len(animation_list) - 1:
                action += 1
                frame = 0

    pygame.display.update()

pygame.quit()