import pygame
from dialog import DialogBox
from player import Enemy, MovingSprite, Player, NPC
from map import MapManager
import subprocess

class Game:

    def __init__(self):

        # demarrage
        self.running = True
        self.map = "world"
        
        # creer la fenetre du jeu
        SCREENWIDTH, SCREENHEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
        self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
        pygame.display.set_caption("My own adventure")

        # generer un joueur
        self.player = Player()
        self.map_manager = MapManager(self.screen, self.player)
        self.dialog_box = DialogBox()
        
        # generer les elements qui vont aller sur l'ecran
        self.chat_coeur_ini = pygame.image.load('map/cat_heart.png').convert_alpha()
        self.chat_coeur = pygame.transform.scale(self.chat_coeur_ini, (250, 80))
        self.chat_coeur_rect = self.chat_coeur.get_rect(topleft=(30, 20))

        self.maps_icon_ini = pygame.image.load('map/maps_icon.png').convert_alpha()
        self.maps_icon = pygame.transform.scale(self.maps_icon_ini, (120, 120))
        self.maps_icon_rect = self.maps_icon.get_rect(topright=(1460, 20))

        # self.dialog_test_ini = pygame.image.load('dialogs/dialog_box.png').convert_alpha()
        # self.dialog_test = pygame.transform.scale(self.dialog_test_ini, (40, 30))
        # self.dialog_test_rect = self.dialog_test.get_rect(topleft=(290, 200))
        
    def handle_input(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_ESCAPE]:
            self.running = False
        elif pressed[pygame.K_z]:
            self.player.move_up()
        elif pressed[pygame.K_s]:
            self.player.move_down()
        elif pressed[pygame.K_q]:
            self.player.move_left()
        elif pressed[pygame.K_d]:
            self.player.move_right()
        else:
            self.player.move_idle()

    def update(self):
        self.map_manager.update()
        # self.bubble.update()

        for sprite in self.map_manager.get_group().sprites():
            if isinstance(sprite, Enemy):
                if self.player.rect.colliderect(sprite.rect):
                    print("Touched Enemy!")
                    self.player.move_back_more()
    
    def run(self):
        clock = pygame.time.Clock()

        while self.running:

            self.player.save_location()
            self.handle_input()
            self.update()
            self.map_manager.draw()
            self.dialog_box.render(self.screen)

            # afficher les elements sur l'ecran
            self.screen.blit(self.chat_coeur, self.chat_coeur_rect.topleft)
            self.screen.blit(self.maps_icon, self.maps_icon_rect.topright)

            if self.dialog_box.is_reading() or self.map_manager.is_npc_colliding():
                for sprite in self.map_manager.get_group().sprites():
                    if isinstance(sprite, NPC):
                        sprite.load_bubble(True)

            pygame.display.flip() #actualiser en temps reel

            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         self.running = False
            #     elif event.type == pygame.KEYDOWN:
            #         if event.key == pygame.K_f:
            #             self.map_manager.check_npc_collisions(self.dialog_box)
            #     elif event.type == pygame.MOUSEWHEEL:
            #         if event.y > 0:  # Zoom in
            #             self.map_manager.zoom_level += 1
            #             self.map_manager.get_map().group.zoom += 0.1
            #         elif event.y < 0:  # Zoom out
            #             self.map_manager.zoom_level -= 1
            #             self.map_manager.get_map().group.zoom -= 0.1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        self.map_manager.check_npc_collisions(self.dialog_box)
                    elif event.key == pygame.K_COMMA:  # Vérifier si la touche "," est pressée
                        print(", pressed")
                        subprocess.Popen(['python', 'src\carte.py'])  # Lancer carte.py
                elif event.type == pygame.MOUSEWHEEL:
                    if event.y > 0:  # Zoom in
                        self.map_manager.zoom_level += 1
                        self.map_manager.get_map().group.zoom += 0.1
                    elif event.y < 0:  # Zoom out
                        self.map_manager.zoom_level -= 1
                        self.map_manager.get_map().group.zoom -= 0.1

            clock.tick(60)

        pygame.quit()

class DialogOpen:
    def __init__(self):
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.player = Player()
        self.map_manager = MapManager(self.screen, self.player)

        self.dialog_test_ini = pygame.image.load('dialogs/dialog_box.png').convert_alpha()
        self.dialog_test = pygame.transform.scale(self.dialog_test_ini, (250, 80))
        self.dialog_test_rect = self.dialog_test.get_rect(topleft=(30, 20))
    
    def run(self):
        if self.dialog_box.is_reading() or self.map_manager.is_npc_colliding():
            self.screen.blit(self.dialog_test, self.dialog_test_rect.topleft)