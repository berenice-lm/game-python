from dataclasses import dataclass
import pygame, pytmx, pyscroll
from player import NPC, MovingSprite, Panneau, Enemy

@dataclass
class Portal:
    from_world: str
    origin_point: str
    target_world: str
    teleport_point: str

@dataclass #decorateur absorbé par la classe dessous (init aussi)
class Map :
    name: str
    walls: list[pygame.Rect]
    group: pyscroll.PyscrollGroup
    tmx_data: pytmx.TiledMap
    portals: list[Portal]
    npcs: list[NPC]
    movingsprites: list[MovingSprite]
    enemies: list[Enemy]
    panneaux: list[Panneau]

class MapManager:

    def __init__(self, screen, player):
        self.maps = dict() #pour stocker plusieurs cartes : "house" -> Map("house", walls, group)
        self.screen = screen
        self.player = player
        self.current_map = "world"
        self.dialog_box_triggered = False
        # self.map_zoom_out = pygame.image.load('map/carte_dezoom.png').convert_alpha()
        self.zoom_level = 4  # Initial zoom level

        self.register_map("world", portals=[
            Portal(from_world="world", origin_point="enter_house", target_world="house", teleport_point="spawn_house"),
            Portal(from_world="world", origin_point="enter_house2", target_world="house2", teleport_point="spawn_house"),
            Portal(from_world="world", origin_point="enter_dungeon", target_world="map_nord", teleport_point="spawn_dungeon"),
            Portal(from_world="world", origin_point="enter_map2", target_world="labyrinthe", teleport_point="spawn_map2")
        ], npcs=[
            NPC("papy", nb_points=4, dialog=["Salut, quelque chose ne va pas ?", "Ah mince, je ne suis pas d'ici. Je ne peux pas t'aider", "Mais j'ai perdu une boucle d'oreille ici...", "Je galère un peu :("]),
            NPC("red", nb_points=1, dialog=["Que voulez-vous ?", "Vous êtes perdu ? Etonnant", "On se trouve à Ville machin, ici", "Si vous ne savez pas ou c'est, suivre la rivière truc", "Elle prend sa source à Grande Ville", "Elle passe pas très loin d'ici, en traversant un PNR", "Mince...je ne sais plus comment il s'appelle", "Je crois qu'il a des chemins en forme d'étoile", "Bon courage !"]),
            # NPC("boss", nb_points=2, dialog=["test"]),
        ], movingsprites=[
            MovingSprite("smoke", 270, 367),
            # MovingSprite("bubble", 200, 290),
        ], enemies=[
            Enemy("boss", nb_points=1, dialog=[])
        ], panneaux=[
            Panneau("panneau", nb_points=1, dialog=["Nord : Ville machin", "Est : Ville truc"])
        ])
        self.register_map("house", portals=[
            Portal(from_world="house", origin_point="exit_house", target_world="world", teleport_point="enter_house_exit")
        ], npcs=[
            NPC("red", nb_points=1, dialog=["Vous êtes réveillé ?", "Bla bla bla sur comment on est là", "Vous avez une note : la voici"])
        ])
        self.register_map("house2", portals=[
            Portal(from_world="house2", origin_point="exit_house", target_world="world", teleport_point="exit_house2")
         ])
        self.register_map("map_nord", portals=[
            Portal(from_world="map_nord", origin_point="exit_dungeon", target_world="world", teleport_point="dungeon_exit_spawn")
        ], npcs=[
            NPC("boss", nb_points=2, dialog=["N'ALLEZ PAS PAR LA !!!"])
        ])
        self.register_map("labyrinthe", portals=[
            Portal(from_world="labyrinthe", origin_point="exit_map2", target_world="world", teleport_point="exit_map2_spawn"),
            Portal(from_world="labyrinthe", origin_point="exit_map22", target_world="world", teleport_point="exit_map2_spawn")
        ])
        self.teleport_player("player")
        self.teleport_npcs()
        # self.load_bubble(True)
        # self.teleport_panneaux()

    def is_npc_colliding(self):
        enlarged_player_rect = self.player.rect.inflate(10, 10)
        for sprite in self.get_group().sprites():
            if sprite.feet.colliderect(enlarged_player_rect) and isinstance(sprite, NPC):
                return True
        return False

    def check_collisions(self):
    # portails
        for portal in self.get_map().portals:
            if portal.from_world == self.current_map:
                point = self.get_object(portal.origin_point)
                rect = pygame.Rect(point.x, point.y, point.width, point.height)

                if self.player.feet.colliderect(rect):
                    copy_portal = portal
                    self.current_map = portal.target_world
                    self.teleport_player(copy_portal.teleport_point)

        # collisions
        for sprite in self.get_group().sprites():
            if sprite.feet.collidelist(self.get_walls()) > -1:
                sprite.move_back()

            if isinstance(sprite, NPC):
                enlarged_player_rect = self.player.rect.inflate(10, 10)

                if sprite.feet.colliderect(self.player.rect):
                    self.player.move_back()

                if sprite.feet.colliderect(enlarged_player_rect):
                    sprite.speed = 0

                else:
                    sprite.speed = 1 

    def teleport_player(self, name):
        point = self.get_object(name)
        self.player.position[0] = point.x
        self.player.position[1] = point.y
        self.player.save_location()
    
    def register_map(self, name, portals=[], npcs=[], movingsprites=[], enemies=[], panneaux=[]):
        # charger la carte (tmx)
        tmx_data = pytmx.util_pygame.load_pygame(f"map/{name}.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 4

        # definir liste qui stocke les rectangles de collision
        walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                walls.append(pygame.Rect(obj.x, obj.y - 15, obj.width, obj.height))

        # dessiner le groupe de calques
        group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=7)
        group.add(self.player)

        # recuperer tous les npcs pour les ajouter au groupe
        for npc in npcs:
            group.add(npc)

        for movingsprite in movingsprites:
            group.add(movingsprite)
        
        for enemy in enemies:
            group.add(enemy)

        for panneau in panneaux:
            group.add(panneau)
        
        # for moving_sprite in moving_sprites: #sprite charge sur la carte mais sans animation
        #     group.add(moving_sprite)

        # creer un objet Map
        self.maps[name] = Map(name, walls, group, tmx_data, portals, npcs, movingsprites, enemies, panneaux)

    def get_map(self): return self.maps[self.current_map]

    def get_group(self): return self.get_map().group

    def get_walls(self): return self.get_map().walls

    def get_object(self, name): return self.get_map().tmx_data.get_object_by_name(name)

    def teleport_npcs(self):
        for map in self.maps:
            map_data = self.maps[map]
            npcs = map_data.npcs
            panneaux = map_data.panneaux
            enemies = map_data.enemies

            for npc in npcs:
                npc.load_points(map_data.tmx_data)
                npc.teleport_spawn()
            
            for enemy in enemies:
                enemy.load_points(map_data.tmx_data)
                enemy.teleport_spawn()
            
            for panneau in panneaux:
                panneau.load_points_P(map_data.tmx_data)
                panneau.teleport_spawn_P()

    def draw(self):
        self.get_group().draw(self.screen)
        self.get_group().center(self.player.rect.center)
    
    def check_npc_collisions(self, dialog_box):
        enlarged_player_rect = self.player.rect.inflate(10, 10)
        if not self.dialog_box_triggered:
            for sprite in self.get_group().sprites():
                if sprite.feet.colliderect(enlarged_player_rect) and isinstance(sprite, (NPC, Panneau, Enemy)):
                    if not dialog_box.is_reading():
                        dialog_box.execute(sprite.dialog)
                        self.player.speed = 0
                    else:
                        if dialog_box.is_reading():
                            dialog_box.next_text()
                        if not dialog_box.is_reading():
                            self.player.speed = 2

    def update(self):
        self.get_group().update()
        self.check_collisions()

        for npc in self.get_map().npcs:
            npc.move()
        
        for enemy in self.get_map().enemies:
            enemy.move()
        
        for movingsprite in self.get_map().movingsprites:
            movingsprite.move_idle()

        # for moving_sprite in self.get_map().moving_sprites:
        #     moving_sprite.move_idle()

        # for moving_sprite in self.get_map().moving_sprites:
        #     moving_sprite.move_S()
        