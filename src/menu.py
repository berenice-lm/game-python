import pygame, sys
from game import Game

SCREENWIDTH, SCREENHEIGHT = 800, 500
FPS = 60

class Start:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
        self.clock = pygame.time.Clock()

        self.gameStateManager = GameStateManager('menu')
        self.menu = Menu(self.screen, self.gameStateManager)
        self.game = Game_start(self.screen, self.gameStateManager)
        self.option = Option(self.screen, self.gameStateManager)

        # dictionnaire des états
        self.states = {'menu':self.menu, 'game':self.game, 'option':self.option}

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # if event.type == pygame.KEYDOWN:
                #     self.gameStateManager.set_state('level')

            self.states[self.gameStateManager.get_state()].run()

            pygame.display.update()
            self.clock.tick(FPS)

class Game_start:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        
    def run(self):
        # keys = pygame.key.get_pressed()
        pygame.init()
        game = Game()
        game.run()

class Option:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.pressed = False
        self.gameStateManager = gameStateManager
        self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
        self.clock = pygame.time.Clock()
        
        self.button1 = ButtonO('Système', 200, 40, (20, 80), 1)
        self.button2 = ButtonO('Audio', 200, 40, (40, 130), 2)
        self.button3 = ButtonO('Vidéo', 200, 40, (60, 180), 3)
        self.button4 = ButtonO('Interface', 200, 40, (80, 230), 4)
        self.button5 = ButtonO('Paramètres', 200, 40, (100, 280), 5)
        self.button6 = ButtonO('Commandes', 200, 40, (120, 330), 6)
        self.button7 = ButtonO('Langue', 200, 40, (140, 380), 7)
        self.button8 = ButtonO('Gameplay', 200, 40, (160, 430), 8)
        self.button1_1 = ButtonO('Système1', 200, 40, (400, 80), 1_1)

        self.bg_rect = pygame.Rect(400, 70, 350, 400)
        self.bg_color = (176, 176, 176, 220)
        self.bg_surface = pygame.Surface((self.bg_rect.width, self.bg_rect.height), pygame.SRCALPHA)
        pygame.draw.rect(self.bg_surface, self.bg_color, self.bg_surface.get_rect(), border_radius=12)

        self.bg_images = []
        for i in range(1, 6):
            self.bg_image = pygame.image.load(f'map/forest_{i}.png').convert_alpha()
            self.bg_image_size = pygame.transform.scale(self.bg_image, (600, SCREENHEIGHT))
            self.bg_images.append(self.bg_image_size)

        self.bg_width = self.bg_images[0].get_width()

        self.chat_return = pygame.image.load('map/cat_return1.png').convert_alpha()
        self.chat_return2 = pygame.image.load('map/cat_return2.png').convert_alpha()
        self.chat = pygame.transform.scale(self.chat_return, (70, 80))
        self.chat_rect = self.chat.get_rect(topleft=(5, -8))
        self.chat_mask = pygame.mask.from_surface(self.chat)

        self.bullet = pygame.Surface((10, 10))
        self.bullet_mask = pygame.mask.from_surface(self.bullet)

        #define game variables
        self.scroll = 0
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()

    def reset_button_states(self):
        self.button1.pressed = False
        self.button2.pressed = False
        self.button3.pressed = False
        self.button4.pressed = False
        self.button5.pressed = False
        self.button6.pressed = False
        self.button7.pressed = False
        self.button8.pressed = False

        self.button1_1.pressed = False
        
    def run(self):
        fond_ecran = pygame.image.load('map/option.png')
        fond_ecran_size = pygame.transform.scale(fond_ecran, (800, 500))

        self.screen.fill('#DCDDD8')
        self.screen.blit(fond_ecran_size, (0, 0))
        self.screen.blit(self.chat, self.chat_rect.topleft)

        pos = pygame.mouse.get_pos() #mouse coordinates

        self.draw_bg()
        # self.draw_buttons()
        self.screen.blit(self.chat, self.chat_rect.topleft)
        self.button1.draw(self.screen)
        self.button2.draw(self.screen)
        self.button3.draw(self.screen)
        self.button4.draw(self.screen)
        self.button5.draw(self.screen)
        self.button6.draw(self.screen)
        self.button7.draw(self.screen)
        self.button8.draw(self.screen)

        new_mouse_x, new_mouse_y = pygame.mouse.get_pos() # get mouse position
        mouse_delta = new_mouse_x - self.mouse_x # calculate the difference in mouse position

        # update scroll based on the mouse movement
        self.scroll -= mouse_delta * 0.05  # Adjust this value for sensitivity
        self.scroll = max(0, min(self.scroll, 300)) # clamp scroll to prevent going out of bounds
        self.mouse_x, self.mouse_y = new_mouse_x, new_mouse_y # update mouse position for the next iteration
        
        # pygame.draw.rect(self.bg_surface, self.bg_color, self.bg_surface.get_rect(), border_radius=12)
        # self.screen.blit(self.bg_surface, self.bg_rect.topleft)

        # if self.button1.pressed:
        #     self.bg_color = (176, 176, 176, 200)
        #     self.screen.blit(self.bg_surface, self.bg_rect.topleft)
        #     if pygame.mouse.get_pressed()[0]:
        #         self.bg_color = (176, 176, 176, 0)
        #         self.pressed == False
        # else:
        #     self.bg_color = (176, 176, 176, 0)

        if self.button1.pressed:
            self.reset_button_states()
            if True:
        #     self.reset_button_states()
            # print("butt 1 pressed")
        #     self.pressed = True
        #     self.bg_color = (176, 176, 176, 200)
                self.button1_1.draw(self.screen)
        else:
            self.reset_button_states()
                
        # else:
        #     # self.pressed = False
        #     self.bg_color = (176, 176, 176, 0)
            # self.reset_button_states()
            # self.button1_1.draw(self.screen)
        # check if buttons are pressed

        if self.chat_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            else:
                if self.pressed == True:
                    self.pressed = False
                    self.gameStateManager.set_state('menu')
        # check mask overlap
        if self.chat_mask.overlap(self.bullet_mask, (pos[0] - self.chat_rect.x, pos[1] - self.chat_rect.y)):
            self.chat = pygame.transform.scale(self.chat_return2, (70, 80))
        else:
            self.chat = pygame.transform.scale(self.chat_return, (70, 80))
    
    def draw_bg(self):
        for x in range(5):
            speed = 0.2  # Decreased speed for slower movement
            for i in self.bg_images:
                self.screen.blit(i, ((x * self.bg_width) - self.scroll * speed, 0))
                speed += 0.2  # Adjust this value to control the parallax effect
    
    def draw_buttons(self):
        # Draw the chat image on top of the background
        self.screen.blit(self.chat, self.chat_rect.topleft)
        self.button1.draw(self.screen)
        self.button2.draw(self.screen)
        self.button3.draw(self.screen)
        self.button4.draw(self.screen)
        self.button5.draw(self.screen)
        self.button6.draw(self.screen)
        self.button7.draw(self.screen)
        self.button8.draw(self.screen)
    
    # def draw_bg_rects(self):
    #     for button in [self.button1, self.button1_1, self.button2, self.button3, self.button4,
    #                    self.button5, self.button6, self.button7, self.button8]:
    #         bg_surface = pygame.Surface((button.bg_rect.width, button.bg_rect.height), pygame.SRCALPHA)
    #         pygame.draw.rect(bg_surface, button.bg_color, bg_surface.get_rect(), border_radius=12)
    #         self.screen.blit(bg_surface, button.bg_rect.topleft)

class Menu:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
        self.clock = pygame.time.Clock()
        self.button1 = ButtonM('Play', 200, 40, (290, 30),6, 1)
        self.button2 = ButtonM('Options', 200, 40, (290, 90),6, 2)
        self.button3 = ButtonM('Quit', 200, 40, (290, 150),6, 3)

        self.chat_init = pygame.image.load('map/chat.png').convert_alpha()
        self.chat_init2 = pygame.image.load('map/chat2.png').convert_alpha()
        self.chat = pygame.transform.scale(self.chat_init, (800, 500))
        self.chat_rect = self.chat.get_rect()
        self.chat_mask = pygame.mask.from_surface(self.chat)

        self.bullet = pygame.Surface((10, 10))
        self.bullet_mask = pygame.mask.from_surface(self.bullet)

    def reset_button_states(self):
        self.button1.pressed = False
        self.button2.pressed = False
        self.button3.pressed = False 

    def run(self):
        fond_ecran = pygame.image.load('map/ecran1.png')
        fond_ecran_size = pygame.transform.scale(fond_ecran, (800, 500))

        self.screen.fill('#DCDDD8')
        self.screen.blit(fond_ecran_size, (0, 0))
        self.screen.blit(self.chat, self.chat_rect)

        self.button1.draw(self.screen)
        self.button2.draw(self.screen)
        self.button3.draw(self.screen)

        # check if buttons are pressed
        if self.button1.pressed:
            self.reset_button_states()
            self.gameStateManager.set_state('game')
        if self.button2.pressed:
            self.reset_button_states()
            print("butt 2")
            self.gameStateManager.set_state('option')
        if self.button3.pressed:
            self.reset_button_states()  # Reset button states before transitioning
            pygame.quit()
            sys.exit()

        pos = pygame.mouse.get_pos() #mouse coordinates

        # check mask overlap
        if self.chat_mask.overlap(self.bullet_mask, (pos[0] - self.chat_rect.x, pos[1] - self.chat_rect.y)):
            self.chat = pygame.transform.scale(self.chat_init2, (800, 500))
        else:
            self.chat = pygame.transform.scale(self.chat_init, (800, 500))
        
        # if keys[pygame.K_e]:
        #     self.gameStateManager.set_state('game')

class ButtonO:
    def __init__(self, text, width, height, pos, number):

        # core attributes
        self.running = True
        self.pressed = False
        self.original_y_pos = pos[1]
        self.number = number

        # font_path = "dialogs/ACCESSIBLE.ttf"
        # self.gui_font = pygame.font.Font(font_path, 20)

        font_path = "dialogs/Catalina.ttf"
        self.gui_font = pygame.font.Font(font_path, 25)

        pygame.display.set_caption('Gui Menu')
        # gui_font = pygame.font.Font(None, 30)

        # top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = (100, 194, 68, 210)

        # bg rectangle
        # self.bg_rect = pygame.Rect(pos, (width, height))
        # self.bg_color = (176,176,176, 220)
        # self.bg_rect = pygame.Rect(pos[0] - bg_padding, pos[1] - bg_padding, width + 2 * bg_padding, height + 2 * bg_padding)
        # self.bg_rect = pygame.Rect(400, 70, 350, 400)
        # self.bg_color = (176, 176, 176, 220)

        # text
        self.text_surf = self.gui_font.render(text, True, (0, 0, 0))
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
        self.is_pressed = False

    def draw(self, screen):
        self.top_rect.y = self.original_y_pos
        self.text_rect.center = self.top_rect.center
        screen.blit(self.text_surf, self.text_rect)

        # button_surface = pygame.Surface((self.top_rect.width, self.top_rect.height), pygame.SRCALPHA)
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius=12)

        # bg_surface = pygame.Surface((self.bg_rect.width, self.bg_rect.height), pygame.SRCALPHA)
        # pygame.draw.rect(bg_surface, self.bg_color, bg_surface.get_rect(), border_radius=12)

        # Blit the surface onto the screen
        # screen.blit(button_surface, self.top_rect.topleft)
        screen.blit(self.text_surf, self.text_rect)
        # screen.blit(bg_surface, self.bg_rect.topleft)
        
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = (176,176,176, 220)
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            else:
                if self.pressed == True:
                    self.pressed = False  # Toggle the pressed state
            #         self.is_pressed = not self.is_pressed  # Toggle the pressed state
                    print(f"Buttonnnn {self.number} pressed")
                        
        else:
            self.top_color = (100, 194, 68, 210)

        # if self.is_pressed:
        #     self.screen.blit(self.bg_surface, self.bg_rect.topleft)
        #     self.bg_color = (176, 176, 176, 200)
        #     if pygame.mouse.get_pressed()[0]:
        #         self.bg_color = (176, 176, 176, 0)
        #         self.is_pressed == False
        # else:
        #     self.bg_color = (176, 176, 176, 0)

class ButtonM:
    def __init__(self, text, width, height, pos, elevation, number):
        # core attributes
        self.running = True
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = pos[1]
        self.number = number

        font_path = "dialogs/Catalina.ttf"
        self.gui_font = pygame.font.Font(font_path, 27)

        pygame.display.set_caption('Gui Menu')
        # clock = pygame.time.Clock()
        # gui_font = pygame.font.Font(None, 30)

        # top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = '#65C244'

        # bottom rectangle
        self.bottom_rect = pygame.Rect(pos, (width, elevation))
        self.bottom_color = '#114905'

        # text
        self.text_surf = self.gui_font.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

    def draw(self, screen):

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
                    print(f"Button {self.number} pressed")
                        
        else:
            self.dynamic_elevation = self.elevation
            self.top_color = '#65C244'

class GameStateManager:
    def __init__(self, currentState):
        self.currentState = currentState
    def get_state(self):
        return self.currentState
    def set_state(self, state):
        self.currentState = state

if __name__ == '__main__':
    game = Start()
    game.run()