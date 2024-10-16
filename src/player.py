import pygame
from animation import AnimateSprite
from chat_sprite import SpriteSheet

class Entity(AnimateSprite):

    def __init__(self, name, x, y):
        super().__init__(name)
        self.image = self.get_image(0, 0, 32, 32)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.position = [x, y]

        self.feet = pygame.Rect(10, 0, self.rect.width * 0.5, 1)
        self.old_position = self.position.copy()

    def save_location(self): self.old_position = self.position.copy()
    
    def move_right(self): 
        self.change_animation("right")
        self.position[0] += self.speed

    def move_left(self): 
        self.change_animation("left")
        self.position[0] -= self.speed

    def move_down(self): 
        self.change_animation("down")
        self.position[1] += self.speed

    def move_up(self): 
        self.change_animation("up")
        self.position[1] -= self.speed
    
    def move_idle(self): 
        self.change_animation("idle")

    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.center

    def move_back(self):
        self.position = self.old_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.center

    def slow_down(self):
        # Calculate the distance to move back
        distance_x = self.position[0] - self.old_position[0]
        distance_y = self.position[1] - self.old_position[1]

        # Move the player back by twice the distance
        self.position[0] -= 0.5 * distance_x
        self.position[1] -= 0.5 * distance_y

        # Update the player's rectangle
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.center

    def move_back_more(self):
        # Calculate the distance to move back
        distance_x = self.position[0] - self.old_position[0]
        distance_y = self.position[1] - self.old_position[1]

        # Move the player back by twice the distance
        self.position[0] -= 10 * distance_x
        self.position[1] -= 10 * distance_y

        # Update the player's rectangle
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.center

    def play_death_animation(self, animation_name):
        if not self.is_dead:  # Check if the player is already dead
            self.is_dead = True
            self.change_animation(animation_name)

            # Schedule a return to idle animation after the death animation completes
            pygame.time.set_timer(pygame.USEREVENT + 1, 500)  # Delay of 500ms (adjust as needed)

    def handle_event(self, event):
        if event.type == pygame.USEREVENT + 1:  # Custom event triggered after animation
            self.is_dead = False  # Reset death state
            self.change_animation("idle")  # Return to idle animation
            pygame.time.set_timer(pygame.USEREVENT + 1, 0)  # Stop the timer
        
class Player(Entity):
    def __init__(self):
        super().__init__('chattest5', 0, 0)
        self.is_dead = False
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 120
        self.action = 0
        self.frame = 0
        # self.animation_list = load_animations()
        sprite_sheet_image = pygame.image.load('sprites/cat/chat_principal.png').convert_alpha()
        sprite_sheet = SpriteSheet(sprite_sheet_image)
        self.animation_list = sprite_sheet.load_animations()

class NPC(Entity):

    def __init__(self, name, nb_points, dialog):
        super().__init__(name, 0, 0)
        # self.player = Player()
        self.nb_points = nb_points
        self.dialog = dialog
        self.points = []
        self.name = name
        self.speed = 1
        self.current_point = 0
        self.type = type
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    def move(self):
        current_point = self.current_point
        target_point = self.current_point + 1

        if target_point >= self.nb_points:
            target_point = 0

        current_rect = self.points[current_point]
        target_rect = self.points[target_point]

        if current_rect.y < target_rect.y and abs(current_rect.x - target_rect.x) < 3:
            self.move_down()
        elif current_rect.y > target_rect.y and abs(current_rect.x - target_rect.x) < 3:
            self.move_up()
        elif current_rect.x > target_rect.x and abs(current_rect.y - target_rect.y) < 3:
            self.move_left()
        elif current_rect.x < target_rect.x and abs(current_rect.y - target_rect.y) < 3:
            self.move_right()
        else:
            self.move_idle()

        if self.rect.colliderect(target_rect):
            self.current_point = target_point

    def teleport_spawn(self):
        location = self.points[self.current_point]
        self.position[0] = location.x
        self.position[1] = location.y
        self.save_location()
    
    def load_points(self, tmx_data):
        for num in range(1, self.nb_points+1):
            point = tmx_data.get_object_by_name(f"{self.name}_path{num}")
            rect = pygame.Rect(point.x, point.y, point.width, point.height)
            self.points.append(rect)
    
    def load_bubble(self, display_dialog):
        if display_dialog:
            self.dialog_test_ini = pygame.image.load('dialogs/dialog_box.png').convert_alpha()
            self.dialog_test = pygame.transform.scale(self.dialog_test_ini, (40, 30))
            self.dialog_test_rect = self.dialog_test.get_rect(topleft=(self.position[0], self.position[1]))
            # self.dialog_test_rect = self.dialog_test.get_rect(topleft=(290, 200))
            # bulle = MovingSprite("bubble", 200, 290)

            # bulle.move()
            # self.screen.draw(self.dialog_test, self.dialog_test_rect)

class Enemy(Entity):

    def __init__(self, name, nb_points, dialog):
        super().__init__(name, 0, 0)
        # self.player = Player()
        self.nb_points = nb_points
        self.dialog = dialog
        self.points = []
        self.name = name
        self.speed = 1
        self.current_point = 0
        self.type = type
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    def move(self):
        current_point = self.current_point
        target_point = self.current_point + 1

        if target_point >= self.nb_points:
            target_point = 0

        current_rect = self.points[current_point]
        target_rect = self.points[target_point]

        if current_rect.y < target_rect.y and abs(current_rect.x - target_rect.x) < 3:
            self.move_down()
        elif current_rect.y > target_rect.y and abs(current_rect.x - target_rect.x) < 3:
            self.move_up()
        elif current_rect.x > target_rect.x and abs(current_rect.y - target_rect.y) < 3:
            self.move_left()
        elif current_rect.x < target_rect.x and abs(current_rect.y - target_rect.y) < 3:
            self.move_right()
        else:
            self.move_idle()

        if self.rect.colliderect(target_rect):
        # if self.mask and self.mask.overlap(self.player.mask, (int(self.player.rect.x - self.rect.x), int(self.player.rect.y - self.rect.y))):
            self.current_point = target_point

    def teleport_spawn(self):
        location = self.points[self.current_point]
        self.position[0] = location.x
        self.position[1] = location.y
        self.save_location()
    
    def load_points(self, tmx_data):
        for num in range(1, self.nb_points+1):
            point = tmx_data.get_object_by_name(f"{self.name}_path{num}")
            rect = pygame.Rect(point.x, point.y, point.width, point.height)
            self.points.append(rect)

class MovingSprite(AnimateSprite):
    def __init__(self, name, x, y):
        super().__init__(name)
        self.name = name
        self.image = self.get_image(0, 0, 32, 32)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.feet = pygame.Rect(10, 0, self.rect.width * 0.5, 10)
        self.old_position = self.position.copy()
        self.points = []
        self.current_point = 0

    def move_idle(self):
        self.change_animation(self.name)
    
    def save_location(self): self.old_position = self.position.copy()

    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom
    
    def teleport_spawn(self):
        location = self.points[self.current_point]
        self.position[0] = location.x
        self.position[1] = location.y
        self.save_location()
    
    def load_points(self, tmx_data):
        for num in range(1, 2):
            point = tmx_data.get_object_by_name(f"{self.name}_path{num}")
            rect = pygame.Rect(point.x, point.y, point.width, point.height)
            self.points.append(rect)
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Panneau(Entity):
    def __init__(self, name, nb_points, dialog):
        super().__init__(name, 0, 0)
        self.nb_points = nb_points
        self.dialog = dialog
        self.points = []
        self.name = name
        self.speed = 1
        self.current_point = 0

    def teleport_spawn_P(self):
        location = self.points[self.current_point]
        self.position[0] = location.x
        self.position[1] = location.y
        self.save_location()
    
    def load_points_P(self, tmx_data):
        for num in range(1, self.nb_points+1):
            point = tmx_data.get_object_by_name(f"{self.name}_path{num}")
            rect = pygame.Rect(point.x, point.y, point.width, point.height)
            self.points.append(rect)