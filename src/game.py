import pygame
from dialog import DialogBox
from player import Player
from map import MapManager

class Game:

    def __init__(self):

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
        
        # generer les elements qui vont aller sur l'ecran
        self.chat_coeur_ini = pygame.image.load('map/cat_heart.png').convert_alpha()
        self.chat_coeur = pygame.transform.scale(self.chat_coeur_ini, (250, 80))
        self.chat_coeur_rect = self.chat_coeur.get_rect(topleft=(30, 20))
        
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
        pygame.init()
        clock = pygame.time.Clock()

        while self.running:

            self.player.save_location()
            self.handle_input()
            self.update()
            self.map_manager.draw()
            self.dialog_box.render(self.screen)

            # afficher les elements sur l'ecran
            self.screen.blit(self.chat_coeur, self.chat_coeur_rect.topleft)

            pygame.display.flip() #actualiser en temps reel

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        self.map_manager.check_npc_collisions(self.dialog_box)

            clock.tick(60)

        pygame.quit()