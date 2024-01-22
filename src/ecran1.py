import pygame, sys
from game import Game

class Button:
    def __init__(self, text, width, height, pos, elevation, number):
        # core attributes
        self.running = True
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = pos[1]
        self.number = number

        # top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = '#65C244'

        # bottom rectangle
        self.bottom_rect = pygame.Rect(pos, (width, elevation))
        self.bottom_color = '#114905'

        # text
        self.text_surf = gui_font.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

    def draw(self):
        # elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(screen, self.bottom_color, self.bottom_rect, border_radius=12)
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius=12)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#610505'
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True
            else:
                self.dynamic_elevation = self.elevation
                if self.pressed == True:
                    self.pressed = False
                    self.quit()
                    self.play()
                    print(f"Button {self.number} pressed")
                    
                        
        else:
            self.dynamic_elevation = self.elevation
            self.top_color = '#65C244'

    def quit(self):
        if self.number == 3:
            pygame.quit()
            sys.exit()
    
    def play(self):
        if self.number == 1:
            if __name__ == '__main__':
                pygame.init()
                game = Game()
                game.run()

class Screen1:
    def __init__(self):
        pygame.init()

pygame.init()
screen = pygame.display.set_mode((800, 500))
fond_ecran = pygame.image.load('map/ecran1.png')
fond_ecran_size = pygame.transform.scale(fond_ecran, (800, 500))

# create chats
chat_init = pygame.image.load('map/chat.png').convert_alpha()
chat_init2 = pygame.image.load('map/chat2.png').convert_alpha()
chat = pygame.transform.scale(chat_init, (800, 400))
chat_rect = chat.get_rect()
chat_mask = pygame.mask.from_surface(chat)

pygame.display.set_caption('Gui Menu')
clock = pygame.time.Clock()
gui_font = pygame.font.Font(None, 30)

button1 = Button('PLAY', 200, 40, (290, 30),6, 1)
button2 = Button('OPTIONS', 200, 40, (290, 90),6, 2)
button3 = Button('QUIT', 200, 40, (290, 150),6, 3) 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill('#DCDDD8')
    screen.blit(fond_ecran_size, (0, 0))
    button1.draw()
    button2.draw()
    button3.draw()

    chat_init = pygame.image.load('map/chat.png').convert_alpha()
    chat_init2 = pygame.image.load('map/chat2.png').convert_alpha()
    chat_rect = chat.get_rect()
    chat_mask = pygame.mask.from_surface(chat)

    bullet = pygame.Surface((10, 10))
    bullet_mask = pygame.mask.from_surface(bullet) 

    pos = pygame.mouse.get_pos() #mouse coordinates

    # check mask overlap
    if chat_mask.overlap(bullet_mask, (pos[0] - chat_rect.x, pos[1] - chat_rect.y)):
        chat = pygame.transform.scale(chat_init2, (800, 500))
    else:
        chat = pygame.transform.scale(chat_init, (800, 500))

    # draw chat
    screen.blit(chat, chat_rect)

    pygame.display.update()
    clock.tick(60)