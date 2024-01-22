import pygame

class SpriteSheet():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale, colour):
        image = pygame.Surface((width, height), pygame.SRCALPHA)
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(None)

        return image
    
class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, name):
        super().__init__()
        self.sprite_sheet = pygame.image.load(f'sprites/{name}.png').convert_alpha()
        self.animation_index = 0
        self.clock = 0
        self.images = {
            'idle': self.get_images(0),
            'down': self.get_images(32),
            'left': self.get_images(64),
            'right': self.get_images(96),
            'up': self.get_images(128)
        }
        self.speed = 2

    def change_animation(self, name): 
        self.image = self.images[name][self.animation_index]
        self.image.set_colorkey((0, 0, 0))
        self.clock += self.speed * 8

        if self.clock >= 100:

            self.animation_index += 1 #passer a l'image suivante
            if self.animation_index >= len(self.images[name]):
                self.animation_index = 0

            self.clock = 0

    # def get_images(self, y):
    #     images=[]

    #     for i in range(0, 3):
    #         x = i*32
    #         image = self.get_image(x, y)
    #         images.append(image)

        # return images
    
    def get_images(self, y):
        images = []

        num_frames = 8  # Adjust this based on the number of frames you have for each animation
        for i in range(num_frames):
            x = i * 32  # Assuming each frame is 32 pixels wide
            image = self.get_image(x, y)
            images.append(image)

        return images

    def get_image(self, x, y):
        image = pygame.Surface([32, 32])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32))
        return image

class SpriteSheet():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale):
        image = pygame.Surface((width, height), pygame.SRCALPHA)
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        # Set colorkey to None to keep the black background
        image.set_colorkey(None)

        return image