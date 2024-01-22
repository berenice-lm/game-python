import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Masks")
clock = pygame.time.Clock()

BG = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

pygame.mouse.set_visible(False)

# create chat
# chat_init = pygame.image.load('map/chat.png').convert_alpha()
# chat_init2 = pygame.image.load('map/chat2.png').convert_alpha()
# chat = pygame.transform.scale(chat_init, (800, 400))
# chat_rect = chat.get_rect()
# chat_mask = pygame.mask.from_surface(chat)

# create bullet and mask
bullet = pygame.Surface((10, 10))
bullet.fill(RED)
bullet_mask = pygame.mask.from_surface(bullet)

pressed = False
top_rect = pygame.Rect(290, 30, 200, 40)
top_color = '#65C244'

top_rect2 = pygame.Rect(290, 100, 200, 40)
top_color2 = '#65C244'
# position chat rectangle
# chat_rect.topleft = (30, 200)

run = True
show_chat_blanc = False

while run:
    pos = pygame.mouse.get_pos() #mouse coordinates
    screen.fill(BG)

    chat_init = pygame.image.load('map/chat.png').convert_alpha()
    chat_init2 = pygame.image.load('map/chat2.png').convert_alpha()
    chat = pygame.transform.scale(chat_init, (800, 400))
    chat_rect = chat.get_rect()
    chat_mask = pygame.mask.from_surface(chat)
    chat_rect.topleft = (30, 200)

    # chat_blanc = pygame.image.load('map/chat_blanc.png').convert_alpha()
    # chat_blanc_size = pygame.transform.scale(chat_blanc, (380, 400))

    
    #check is top rect pressed

    if top_rect.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
        top_color = (176, 176, 176, 220)
        show_chat_blanc = True
    else:
        top_color = '#65C244'

    # check if top_rect2 is clicked to hide chat_blanc_size
    if top_rect2.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
        show_chat_blanc = False
    
    if show_chat_blanc:
        chat_blanc = pygame.image.load('map/chat_blanc.png').convert_alpha()
        chat_blanc_size = pygame.transform.scale(chat_blanc, (380, 400))
        screen.blit(chat_blanc_size, (370, 70))
        chat_blanc_size.set_alpha(200)
    
    if chat_mask.overlap(bullet_mask, (pos[0] - chat_rect.x, pos[1] - chat_rect.y)):
            chat = pygame.transform.scale(chat_init2, (800, 400))
            col = RED
    else:
        col = GREEN
        chat = pygame.transform.scale(chat_init, (800, 400))

    # if pygame.mouse.get_pressed()[0]:
    #     pressed = True
    # else:
    #     if pressed == True:
    #         pressed = False
            
    # def pressed1 (screen):
    #     run = True 
    #     if run == True:
    #         screen.blit(chat_blanc_size, (370, 70))
    #         chat_blanc_size.set_alpha(200)

    #         return run

    # if top_rect.collidepoint(pos):
    #     top_color = (176,176,176,220)
    #     if pygame.mouse.get_pressed()[0]:
    #         screen.blit(chat_blanc_size, (370, 70))
    #         chat_blanc_size.set_alpha(200)
    #         # elif pygame.mouse.get_pressed()[0]:
    #         #     pressed = False
    # else:
    #     top_color = '#65C244'


    # screen.fill((30, 30, 30))
    # pygame.draw.rect(screen, (100, 200, 70), top_rect)


    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         run = False
    #     if event.type == pygame.MOUSEBUTTONDOWN:
    #         if event.button == 1:  # Left mouse button.
    #             # Check if the rect collides with the mouse pos.
    #             if top_rect.collidepoint(event.pos):
    #                 print('Area clicked.')
    #                 screen.blit(chat_blanc_size, (370, 70))
    #                 chat_blanc_size.set_alpha(200)

    # check mask overlap
    if chat_mask.overlap(bullet_mask, (pos[0] - chat_rect.x, pos[1] - chat_rect.y)):
        chat = pygame.transform.scale(chat_init2, (800, 400))
        col = RED
    else:
        col = GREEN
        chat = pygame.transform.scale(chat_init, (800, 400))

    # draw chat
    screen.blit(chat, chat_rect)

    pygame.draw.rect(screen, top_color, top_rect, border_radius=12)
    pygame.draw.rect(screen, top_color2, top_rect2, border_radius=12)

    #draw rectangle
    bullet.fill(col)
    screen.blit(bullet, pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.flip()

pygame.quit()