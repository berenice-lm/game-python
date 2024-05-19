import pygame, sys
from game import Game

# SCREENWIDTH, SCREENHEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
FPS = 60

class Start:
    def __init__(self):
        pygame.init()
        SCREENWIDTH, SCREENHEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
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

            # self.gameStateManager.run_with_fade(self.screen, self.states[self.gameStateManager.get_state()])
            self.states[self.gameStateManager.get_state()].run()

            pygame.display.update()
            self.clock.tick(FPS)

class Game_start:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        
    def run(self):
        pygame.init()
        game = Game()
        game.run()

class Option:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.pressed = False
        self.gameStateManager = gameStateManager
        SCREENWIDTH, SCREENHEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
        self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
        self.clock = pygame.time.Clock()
        self.show_chat_blanc1 = False
        self.show_chat_blanc2 = False
        self.show_chat_blanc3 = False
        self.show_chat_blanc4 = False
        self.show_chat_blanc5 = False
        self.show_chat_blanc6 = False
        self.show_chat_blanc7 = False
        self.show_chat_blanc8 = False
        self.on_display = True
        self.off_display = False
        self.on1_display = True
        self.off1_display = False
        
        self.button1 = ButtonO('Système', 300, 50, (80, 140), 1)
        self.button2 = ButtonO('Audio', 300, 50, (120, 230), 2)
        self.button3 = ButtonO('Vidéo', 300, 50, (160, 320), 3)
        self.button4 = ButtonO('Interface', 300, 50, (200, 410), 4)
        self.button5 = ButtonO('Paramètres', 300, 50, (240, 500), 5)
        self.button6 = ButtonO('Commandes', 300, 50, (280, 590), 6)
        self.button7 = ButtonO('Langue', 300, 50, (320, 680), 7)
        self.button8 = ButtonO('Gameplay', 300, 50, (360, 770), 8)
        self.button1_1 = ButtonInside('Système', 130, 50, (1000, 250), 1_1)
        self.button1_2 = ButtonInside('Système2', 590, 65, (765, 410), 1_2)
        self.button1_3 = ButtonInside('Système3', 570, 65, (775, 510), 1_3)
        self.button1_4 = ButtonInside('Système4', 500, 65, (810, 610), 1_4)
        self.button2_1 = ButtonInside('Audio', 130, 50, (1000, 250), 2_1)
        self.button2_2 = ButtonInside('Audio1', 590, 65, (765, 410), 2_2)
        self.button2_3 = ButtonInside('Audio2', 570, 65, (775, 510), 2_3)
        self.button2_4 = ButtonInside('Audio3', 500, 65, (810, 610), 2_4)
        self.button3_1 = ButtonInside('Vidéo', 130, 50, (1000, 250), 3_1)
        self.button3_2 = ButtonInside('Vidéo1', 590, 65, (765, 410), 3_2)
        self.button3_3 = ButtonInside('Vidéo2', 570, 65, (775, 510), 3_3)
        self.button3_4 = ButtonInside('Vidéo3', 500, 65, (810, 610), 3_4)
        self.button4_1 = ButtonInside('Interface', 130, 50, (1000, 250), 4_1)
        self.button4_2 = ButtonInside('Interface1', 590, 65, (765, 410), 4_2)
        self.button4_3 = ButtonInside('Interface2', 570, 65, (775, 510), 4_3)
        self.button4_4 = ButtonInside('Interface3', 500, 65, (810, 610), 4_4)
        self.button5_1 = ButtonInside('Paramètres', 130, 50, (1000, 250), 5_1)
        self.button5_2 = ButtonInside('Paramètres1', 590, 65, (765, 410), 5_2)
        self.button5_3 = ButtonInside('Paramètres2', 570, 65, (775, 510), 5_3)
        self.button5_4 = ButtonInside('Paramètres3', 500, 65, (810, 610), 5_4)
        self.button6_1 = ButtonInside('Commandes', 130, 50, (1000, 250), 6_1)
        self.button6_2 = ButtonInside('Commandes1', 590, 65, (765, 410), 6_2)
        self.button6_3 = ButtonInside('Commandes2', 570, 65, (775, 510), 6_3)
        self.button6_4 = ButtonInside('Commandes3', 500, 65, (810, 610), 6_4)
        self.button7_1 = ButtonInside('Langue', 130, 50, (1000, 250), 7_1)
        self.button7_2 = ButtonInside('Langage', 590, 65, (765, 410), 7_2)
        self.button7_3 = ButtonInside('Sous-titres', 570, 65, (775, 510), 7_3)
        self.button7_4 = ButtonInside('Correcteur', 500, 65, (810, 610), 7_4)
        self.button8_1 = ButtonInside('Gameplay', 130, 50, (1000, 250), 8_1)
        self.button8_2 = ButtonInside('Gameplay1', 590, 65, (765, 410), 8_2)
        self.button8_3 = ButtonInside('Gameplay2', 570, 65, (775, 510), 8_3)
        self.button8_4 = ButtonInside('Gameplay3', 500, 65, (810, 610), 8_4)

        self.current_index = 0
        self.text_dictionary = {
            0: 'français',
            1: 'english',
            2: 'espanol',
            3: 'zzrfg',
            4: 'jnergjb'
        }

        self.bg_images = []
        for i in range(1, 6):
            self.bg_image = pygame.image.load(f'map/forest_{i}.png').convert_alpha()
            self.bg_image_size = pygame.transform.scale(self.bg_image, (SCREENWIDTH - 500, SCREENHEIGHT))
            self.bg_images.append(self.bg_image_size)
        self.bg_width = self.bg_images[0].get_width()

        self.chat_return = pygame.image.load('map/cat_return1.png').convert_alpha()
        self.chat_return2 = pygame.image.load('map/cat_return2.png').convert_alpha()
        self.chat = pygame.transform.scale(self.chat_return, (70, 80))
        self.chat_rect = self.chat.get_rect(topleft=(55, 20))
        self.chat_mask = pygame.mask.from_surface(self.chat)

        self.bullet = pygame.Surface((10, 10))
        self.bullet_mask = pygame.mask.from_surface(self.bullet)

        #define game variables
        self.scroll = 0
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        
    def run(self):
        pos = pygame.mouse.get_pos() #mouse coordinates

        self.draw_bg()
        self.draw_buttons()

        new_mouse_x, new_mouse_y = pygame.mouse.get_pos() # get mouse position
        mouse_delta = new_mouse_x - self.mouse_x # calculate the difference in mouse position

        # update scroll based on the mouse movement
        self.scroll -= mouse_delta * 0.05  # Adjust this value for sensitivity
        self.scroll = max(0, min(self.scroll, 300)) # clamp scroll to prevent going out of bounds
        self.mouse_x, self.mouse_y = new_mouse_x, new_mouse_y # update mouse position for the next iteration

        # check if buttons are pressed
        if self.chat_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            else:
                if self.pressed == True:
                    self.pressed = False
                    self.gameStateManager.set_state('menu')

        if self.button1.top_rect.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
            self.show_chat_blanc2 = False
            self.show_chat_blanc3 = False
            self.show_chat_blanc4 = False
            self.show_chat_blanc5 = False
            self.show_chat_blanc6 = False
            self.show_chat_blanc7 = False
            self.show_chat_blanc8 = False
            self.show_chat_blanc1 = True

        if self.button2.top_rect.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
            self.show_chat_blanc1 = False
            self.show_chat_blanc3 = False
            self.show_chat_blanc4 = False
            self.show_chat_blanc5 = False
            self.show_chat_blanc6 = False
            self.show_chat_blanc7 = False
            self.show_chat_blanc8 = False
            self.show_chat_blanc2 = True
        
        if self.button3.top_rect.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
            self.show_chat_blanc1 = False
            self.show_chat_blanc2 = False
            self.show_chat_blanc4 = False
            self.show_chat_blanc5 = False
            self.show_chat_blanc6 = False
            self.show_chat_blanc7 = False
            self.show_chat_blanc8 = False
            self.show_chat_blanc3 = True

        if self.button4.top_rect.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
            self.show_chat_blanc1 = False
            self.show_chat_blanc3 = False
            self.show_chat_blanc5 = False
            self.show_chat_blanc6 = False
            self.show_chat_blanc7 = False
            self.show_chat_blanc8 = False
            self.show_chat_blanc2 = False
            self.show_chat_blanc4 = True

        if self.button5.top_rect.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
            self.show_chat_blanc1 = False
            self.show_chat_blanc2 = False
            self.show_chat_blanc3 = False
            self.show_chat_blanc4 = False
            self.show_chat_blanc6 = False
            self.show_chat_blanc7 = False
            self.show_chat_blanc8 = False
            self.show_chat_blanc5 = True

        if self.button6.top_rect.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
            self.show_chat_blanc1 = False
            self.show_chat_blanc2 = False
            self.show_chat_blanc3 = False
            self.show_chat_blanc4 = False
            self.show_chat_blanc5 = False
            self.show_chat_blanc7 = False
            self.show_chat_blanc8 = False
            self.show_chat_blanc6 = True
        
        if self.button7.top_rect.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
            self.show_chat_blanc1 = False
            self.show_chat_blanc2 = False
            self.show_chat_blanc3 = False
            self.show_chat_blanc4 = False
            self.show_chat_blanc5 = False
            self.show_chat_blanc6 = False
            self.show_chat_blanc8 = False
            self.show_chat_blanc7 = True

        if self.button8.top_rect.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
            self.show_chat_blanc1 = False
            self.show_chat_blanc3 = False
            self.show_chat_blanc4 = False
            self.show_chat_blanc5 = False
            self.show_chat_blanc6 = False
            self.show_chat_blanc7 = False
            self.show_chat_blanc2 = False
            self.show_chat_blanc8 = True

        def button_on_off():
            font_path = "dialogs/Catalina.ttf"
            self.gui_font = pygame.font.Font(font_path, 20)
            button_on = pygame.Surface((50, 36), pygame.SRCALPHA)
            button_off = pygame.Surface((50, 39), pygame.SRCALPHA)
            button_on1 = pygame.Surface((50, 36), pygame.SRCALPHA)
            button_off1 = pygame.Surface((50, 39), pygame.SRCALPHA)
            pygame.draw.rect(button_on, 'white', button_on.get_rect(), border_radius=12)
            pygame.draw.rect(button_off, 'black', button_off.get_rect(), border_radius=12)
            pygame.draw.rect(button_on1, 'white', button_on1.get_rect(), border_radius=12)
            pygame.draw.rect(button_off1, 'black', button_off1.get_rect(), border_radius=12)
            self.text_surf1 = self.gui_font.render('on', True, "black")
            self.text_surf3 = self.gui_font.render('on', True, "white")
            self.text_surf2 = self.gui_font.render('off', True, "white")
            self.text_surf4 = self.gui_font.render('off', True, "black")
            self.text_rect1 = self.text_surf1.get_rect(topleft=(1253, 625)) #off B
            self.text_rect2 = self.text_surf2.get_rect(topleft=(1190, 625)) #on B
            self.text_rect3 = self.text_surf1.get_rect(topleft=(1291, 525)) #off H
            self.text_rect4 = self.text_surf2.get_rect(topleft=(1220, 525)) #on H
            
            if self.on_display:
                self.screen.blit(button_on, (1277, 525)) 
                self.screen.blit(button_off, (1205, 525))
                self.screen.blit(self.text_surf3, self.text_rect4) #on white avec texte on haut
                self.screen.blit(self.text_surf4, self.text_rect3) #off black avec rect off haut
            
            if self.off_display:
                self.screen.blit(button_off, (1277, 525))
                self.screen.blit(button_on, (1205, 525))
                self.screen.blit(self.text_surf1, self.text_rect4) #on black avec texte on haut
                self.screen.blit(self.text_surf2, self.text_rect3) #off white avec texte off haut

            if self.on1_display:
                self.screen.blit(button_on1, (1240, 625)) #c'est le off x)
                self.screen.blit(button_off1, (1175, 625)) #c'est le on ??
                self.screen.blit(self.text_surf3, self.text_rect2) #on white avec texte on bas
                self.screen.blit(self.text_surf4, self.text_rect1) #off black avec texte off bas
            
            if self.off1_display:
                self.screen.blit(button_off1, (1240, 625))
                self.screen.blit(button_on1, (1175, 625))
                self.screen.blit(self.text_surf1, self.text_rect2) #on black avec texte on bas
                self.screen.blit(self.text_surf2, self.text_rect1) #off white avec texte off bas

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    button_on_rect = pygame.Rect(1220, 525, 50, 36)
                    button_off_rect = pygame.Rect(1291, 525, 50, 39)
                    button_on1_rect = pygame.Rect(1175, 625, 50, 36)
                    button_off1_rect = pygame.Rect(1240, 625, 50, 39)

                    if button_on_rect.collidepoint(x, y):
                        self.on_display = not self.on_display
                        self.off_display = not self.off_display
                        
                    elif button_off_rect.collidepoint(x, y):
                        self.on_display = not self.on_display
                        self.off_display = not self.off_display
                    
                    elif button_on1_rect.collidepoint(x, y):
                        self.on1_display = not self.on1_display
                        self.off1_display = not self.off1_display
                        
                    elif button_off1_rect.collidepoint(x, y):
                        self.on1_display = not self.on1_display
                        self.off1_display = not self.off1_display
                    
                    elif 1320 <= event.pos[0] <= 1340 and 432 <= event.pos[1] <= 462:
                        self.current_index = (self.current_index + 1) % len(self.text_dictionary)
                    
                    elif 1180 <= event.pos[0] <= 1200 and 432 <= event.pos[1] <= 462:
                        self.current_index = (self.current_index - 1) % len(self.text_dictionary)

        
        def button_dictionary():
            font_path = "dialogs/Catalina.ttf"
            gui_font = pygame.font.Font(font_path, 20)

            text_dict = self.text_dictionary[self.current_index]
            text_dict_surf = gui_font.render(text_dict, True, "white")
            text_rect = text_dict_surf.get_rect(topleft=(1230, 425))
            self.screen.blit(text_dict_surf, text_rect)

            fleche1 = pygame.image.load('map/fleche1.png').convert_alpha()
            fleche1_size = pygame.transform.scale(fleche1, (20, 20))
            self.screen.blit(fleche1_size, (1320, 432))

            fleche2 = pygame.image.load('map/fleche2.png').convert_alpha()
            fleche2_size = pygame.transform.scale(fleche2, (20, 20))
            self.screen.blit(fleche2_size, (1180, 432))
        
        if self.show_chat_blanc1:
            chat_blanc = pygame.image.load('map/chat_noir.png').convert_alpha()
            chat_blanc_size = pygame.transform.scale(chat_blanc, (680, 700))
            chat_blanc_size.set_alpha(150)
            self.screen.blit(chat_blanc_size, (720, 120))
            self.button1_1.draw(self.screen)
            self.button1_2.draw(self.screen)
            self.button1_3.draw(self.screen)
            self.button1_4.draw(self.screen)
        
        if self.show_chat_blanc2:
            chat_blanc = pygame.image.load('map/chat_noir.png').convert_alpha()
            chat_blanc_size = pygame.transform.scale(chat_blanc, (680, 700))
            chat_blanc_size.set_alpha(150)
            self.screen.blit(chat_blanc_size, (720, 120))
            self.button2_1.draw(self.screen)
            self.button2_2.draw(self.screen)
            self.button2_3.draw(self.screen)
            self.button2_4.draw(self.screen)

        if self.show_chat_blanc3:
            chat_blanc = pygame.image.load('map/chat_noir.png').convert_alpha()
            chat_blanc_size = pygame.transform.scale(chat_blanc, (680, 700))
            chat_blanc_size.set_alpha(150)
            self.screen.blit(chat_blanc_size, (720, 120))
            self.button3_1.draw(self.screen)
            self.button3_2.draw(self.screen)
            self.button3_3.draw(self.screen)
            self.button3_4.draw(self.screen)
        
        if self.show_chat_blanc4:
            chat_blanc = pygame.image.load('map/chat_noir.png').convert_alpha()
            chat_blanc_size = pygame.transform.scale(chat_blanc, (680, 700))
            chat_blanc_size.set_alpha(150)
            self.screen.blit(chat_blanc_size, (720, 120))
            self.button4_1.draw(self.screen)
            self.button4_2.draw(self.screen)
            self.button4_3.draw(self.screen)
            self.button4_4.draw(self.screen)

        if self.show_chat_blanc5:
            chat_blanc = pygame.image.load('map/chat_noir.png').convert_alpha()
            chat_blanc_size = pygame.transform.scale(chat_blanc, (680, 700))
            chat_blanc_size.set_alpha(150)
            self.screen.blit(chat_blanc_size, (720, 120))
            self.button5_1.draw(self.screen)
            self.button5_2.draw(self.screen)
            self.button5_3.draw(self.screen)
            self.button5_4.draw(self.screen)
        
        if self.show_chat_blanc6:
            chat_blanc = pygame.image.load('map/chat_noir.png').convert_alpha()
            chat_blanc_size = pygame.transform.scale(chat_blanc, (680, 700))
            chat_blanc_size.set_alpha(150)
            self.screen.blit(chat_blanc_size, (720, 120))
            self.button6_1.draw(self.screen)
            self.button6_2.draw(self.screen)
            self.button6_3.draw(self.screen)
            self.button6_4.draw(self.screen)

        if self.show_chat_blanc7:
            chat_blanc = pygame.image.load('map/chat_noir.png').convert_alpha()
            chat_blanc_size = pygame.transform.scale(chat_blanc, (680, 700))
            chat_blanc_size.set_alpha(150)

            self.screen.blit(chat_blanc_size, (720, 120))

            self.button7_1.draw(self.screen)
            self.button7_2.draw(self.screen)
            self.button7_3.draw(self.screen)
            self.button7_4.draw(self.screen)

            button_on_off()
            button_dictionary()
        
        if self.show_chat_blanc8:
            chat_blanc = pygame.image.load('map/chat_noir.png').convert_alpha()
            chat_blanc_size = pygame.transform.scale(chat_blanc, (680, 700))
            chat_blanc_size.set_alpha(150)
            self.screen.blit(chat_blanc_size, (720, 120))
            self.button8_1.draw(self.screen)
            self.button8_2.draw(self.screen)
            self.button8_3.draw(self.screen)
            self.button8_4.draw(self.screen)

        # check mask overlap
        if self.chat_mask.overlap(self.bullet_mask, (pos[0] - self.chat_rect.x, pos[1] - self.chat_rect.y)):
            self.chat = pygame.transform.scale(self.chat_return2, (70, 80))
            self.show_chat_blanc1 = False
            self.show_chat_blanc2 = False
            self.show_chat_blanc3 = False
            self.show_chat_blanc4 = False
            self.show_chat_blanc5 = False
            self.show_chat_blanc6 = False
            self.show_chat_blanc7 = False
            self.show_chat_blanc8 = False
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

class Menu:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager

        # Create the display surface using the screen size and FULLSCREEN flag
        SCREENWIDTH, SCREENHEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
        self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
        self.clock = pygame.time.Clock()

        # Load the image
        self.chat_init1 = pygame.image.load('map/background_vert.png').convert_alpha()
        self.chat_init = pygame.transform.scale(self.chat_init1, (SCREENWIDTH, SCREENHEIGHT))

        # Use the image without scaling
        self.chat = self.chat_init
        self.chat_rect = self.chat.get_rect()

        self.button1 = ButtonM('Play', 200, 40, (590, 300), 6, 1)
        self.button2 = ButtonM('Options', 200, 40, (590, 400), 6, 2)
        self.button3 = ButtonM('Quit', 200, 40, (590, 500), 6, 3)

        # self.chat_rect.topleft = (0, 0)

        # self.chat_mask = pygame.mask.from_surface(self.chat)
        # self.bullet = pygame.Surface((10, 10))
        # self.bullet_mask = pygame.mask.from_surface(self.bullet)

    def reset_button_states(self):
        self.button1.pressed = False
        self.button2.pressed = False
        self.button3.pressed = False 

    def run(self):

        self.screen.fill('black')
        self.screen.blit(self.chat_init, (0, 0))

        self.button1.draw(self.screen)
        self.button2.draw(self.screen)
        self.button3.draw(self.screen)

        # check if buttons are pressed
        if self.button1.pressed:
            self.reset_button_states()
            # if self.button1.pressed == False:
            self.gameStateManager.set_state('game')
        if self.button2.pressed:
            self.reset_button_states()
            # if self.button2.pressed == True:
                # self.button2.pressed = False
            self.gameStateManager.set_state('option')
        if self.button3.pressed:
            self.reset_button_states()  # Reset button states before transitioning
            pygame.quit()
            sys.exit()

        # pos = pygame.mouse.get_pos() #mouse coordinates

        # check mask overlap
        # if self.chat_mask.overlap(self.bullet_mask, (pos[0] - self.chat_rect.x, pos[1] - self.chat_rect.y)):
        #     self.chat = pygame.transform.scale(self.chat_init2, (800, 500))
        # else:
        #     self.chat = pygame.transform.scale(self.chat_init, (800, 500))

class ButtonInside:
    def __init__(self, text, width, height, pos, number):
        # core attributes
        self.running = True
        self.pressed = False
        self.is_pressed = False
        self.original_y_pos = pos[1]
        self.number = number
        self.bg_color = (43,71,21,100)

        font_path = "dialogs/Catalina.ttf"
        self.gui_font = pygame.font.Font(font_path, 23)

        # top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = (0,0,0,210)

        # calculate the y coord of center position for the text
        text_center_y = self.top_rect.centery

        # text
        self.text_surf = self.gui_font.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center=(self.top_rect.x + 65, text_center_y))

    def draw(self, screen):
        
        screen.blit(self.text_surf, self.text_rect)

        button_surface = pygame.Surface((self.top_rect.width, self.top_rect.height), pygame.SRCALPHA)
        pygame.draw.rect(button_surface, self.top_color, button_surface.get_rect(), border_radius=12)

        # Blit the surface onto the screen
        screen.blit(button_surface, self.top_rect.topleft)
        screen.blit(self.text_surf, self.text_rect)

        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (255, 255, 0), self.top_rect, width=1, border_radius=12)
        
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                if self.is_pressed == False:
                    self.is_pressed = True
                        
        else:
            self.top_color =  (0,0,0, 150)

class ButtonO:
    def __init__(self, text, width, height, pos, number):
        # core attributes
        self.running = True
        self.pressed = False
        self.is_pressed = False
        self.original_y_pos = pos[1]
        self.number = number
        self.bg_color = (176, 176, 176, 0)

        font_path = "dialogs/Catalina.ttf"
        self.gui_font = pygame.font.Font(font_path, 23)

        # pygame.display.set_caption('Gui Menu')

        # top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = (0, 0, 0, 180)

        # text
        self.text_surf = self.gui_font.render(text, True, (255, 255, 255))
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

    def draw(self, screen):
        
        screen.blit(self.text_surf, self.text_rect)

        button_surface = pygame.Surface((self.top_rect.width, self.top_rect.height), pygame.SRCALPHA)
        pygame.draw.rect(button_surface, self.top_color, button_surface.get_rect(), border_radius=12)
        
        # Blit the surface onto the screen
        screen.blit(button_surface, self.top_rect.topleft)
        screen.blit(self.text_surf, self.text_rect)
        
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = (149,176,127, 180)
            if pygame.mouse.get_pressed()[0]:
                if self.is_pressed == False:
                    self.is_pressed = True  # Toggle the pressed state
                        
        else:
            self.top_color = (0, 0, 0, 180)

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

        # pygame.display.set_caption('Gui Menu')

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
            self.top_color = 'black'
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