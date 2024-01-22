# import pygame

# from dialog import DialogBox
# from player import Player
# from map import MapManager

# class Game:

#     def __init__(self):

#         # demarrage
#         self.running = True
#         self.map = "world"
        
#         # creer la fenetre du jeu
#         self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
#         pygame.display.set_caption("My own adventure")

#         # generer un joueur
#         self.player = Player()
#         # self.player = Player(x=0, y=0)
#         self.map_manager = MapManager(self.screen, self.player)
#         self.dialog_box = DialogBox()
        
#         # definir le logo du jeu
#         # pygame.display.set_icon(self.player.get())
        
#     def handle_input(self):
#         pressed = pygame.key.get_pressed()

#         if pressed[pygame.K_ESCAPE]:
#             self.running = False
#         if pressed[pygame.K_z]:
#             self.player.move_up()
#         elif pressed[pygame.K_s]:
#             self.player.move_down()
#         elif pressed[pygame.K_q]:
#             self.player.move_left()
#         elif pressed[pygame.K_d]:
#             self.player.move_right()

#     def update(self):
#         self.map_manager.check_npc_collision(self.dialog_box)
#         self.map_manager.update()
        
#     def run(self):
#         clock = pygame.time.Clock()

#         while self.running:
            
#             self.player.save_location()
#             self.handle_input()
#             self.map_manager.draw()
#             self.dialog_box.render(self.screen)

#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     self.running = False
#                 elif event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_f:
                        
#                         # self.dialog_box.close()
#                         # self.map_manager.check_npc_collision(self.dialog_box)
#                         # self.dialog_box.execute(self.dialog_box)
#                         # self.dialog_box.next_text()

#                         if not self.map_manager.check_npc_collision(self.dialog_box):
#                             self.dialog_box.next_text()     
            
#             self.update()
#             clock.tick(60)
#             pygame.display.flip() #actualiser en temps reel
            
#         pygame.quit()

import pygame

from dialog import DialogBox
from player import Player
from map import MapManager

class Game:

    def __init__(self):
        # definir si le jeu à commencé ou non
        # self.is_playing = False

        # demarrage
        self.running = True
        self.map = "world"
        
        # creer la fenetre du jeu
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("My own adventure")

        # generer un joueur
        self.player = Player()
        self.map_manager = MapManager(self.screen, self.player)
        self.dialog_box = DialogBox()
        
        # definir le logo du jeu
        # pygame.display.set_icon(self.player.get())
        
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
    
    def run(self):
        clock = pygame.time.Clock()
        
        # clock

        while self.running:

            # verifier si notre jeu a commencé ou non
            # if Game.is_playing:
                # declencher instructions de la partie
                # Game.update(screen)
            
            self.player.save_location()
            self.handle_input()
            self.update()
            self.map_manager.draw()
            self.dialog_box.render(self.screen)
            # self.map_manager.check_npc_collision(self.dialog_box)
            pygame.display.flip() #actualiser en temps reel

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        self.map_manager.check_npc_collision(self.dialog_box)
                        # self.dialog_box.next_text()

            clock.tick(60)

        pygame.quit()