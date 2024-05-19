import pygame

# class SpriteSheet():
#     def __init__(self, image):
#         self.sheet = image

#     def get_image(self, frame, width, height, scale):
#         image = pygame.Surface((width, height), pygame.SRCALPHA)
#         image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
#         image = pygame.transform.scale(image, (width * scale, height * scale))
#         image.set_colorkey(None)

#         return image
    
class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, name):
        super().__init__()
        self.sprite_sheet = pygame.image.load(f'sprites/{name}.png').convert_alpha()
        self.animation_index = 0
        self.clock = 0
        self.images = {
            'idle': self.get_images(0, 0, 4, 32, 32),
            'down': self.get_images(0, 32, 3, 32, 32),
            'left': self.get_images(0, 64, 4, 32, 32),
            'right': self.get_images(0, 96, 4, 32, 32),
            'up': self.get_images(0, 128, 3, 32, 32),
            'smoke': self.get_images(0, 0, 19, 32, 32),
            'bubble': self.get_images(3, 160, 3, 16, 16),
        }
        self.speed = 2

    def change_animation(self, name): 
        self.clock += self.speed * 8

        if self.clock >= 100:
            self.animation_index += 1

            if self.animation_index >= len(self.images[name]):
                self.animation_index = 0

            self.image = self.images[name][self.animation_index]
            self.image.set_colorkey((0, 0, 0))

            self.clock = 0
    
    def get_images(self, start_x, y, num_frames, pixel_x, pixel_y):
        images = []

        for i in range(num_frames):
            x = (start_x + i) * pixel_x  
            image = self.get_image(x, y, pixel_x, pixel_y)
            images.append(image)

        return images

    def get_image(self, x, y, pixel_x, pixel_y):
        image = pygame.Surface([32, 32])
        image.blit(self.sprite_sheet, (0, 0), (x, y, pixel_x, pixel_y))
        return image