import pygame

# class DialogBox:

#     X_POSITION = 400
#     Y_POSITION = 700

#     def __init__(self):
#         self.box = pygame.image.load('dialogs/dialog_box.png')
#         self.box = pygame.transform.scale(self.box, (800, 100))
#         self.texts = []
#         self.text_index = 0
#         self.letter_index = 0
#         self.font = pygame.font.Font('dialogs/dialog_font.ttf', 18)
#         self.reading = False

#     def execute(self, dialog=[]):
#         if self.reading:
#             self.next_text()
#         else:
#             self.reading = True
#             self.text_index = 0
#             self.texts = dialog

#     def is_reading(self):
#         return self.reading
    
#     def render(self, screen):

#         if self.reading:
#             self.letter_index += 1

#             if self.letter_index >= len(self.texts[self.text_index]):
#                 self.letter_index = self.letter_index

#             screen.blit(self.box, (self.X_POSITION, self.Y_POSITION))
#             text = self.font.render(self.texts[self.text_index][0:self.letter_index], False, (0, 0, 0))
#             screen.blit(text, (self.X_POSITION + 60, self.Y_POSITION + 30))

#     def close(self):
#         self.reading = False

#     def next_text(self):
#         self.text_index += 1
#         self.letter_index = 0

#         if self.text_index >= len(self.texts):
#             self.close()

class DialogBox:

    X_POSITION = 400
    Y_POSITION = 700
    MAX_WIDTH = 700  # Largeur maximale de la boîte de dialogue

    def __init__(self):
        self.box = pygame.image.load('dialogs/dialog_box.png')
        self.box = pygame.transform.scale(self.box, (800, 100))
        self.texts = []
        self.text_index = 0
        self.letter_index = 0
        self.font = pygame.font.Font('dialogs/dialog_font.ttf', 18)
        self.reading = False

    def execute(self, dialog=[]):
        if self.reading:
            self.next_text()
        else:
            self.reading = True
            self.text_index = 0
            self.texts = dialog
    
    def is_reading(self):
        return self.reading

    def render(self, screen):
        if self.reading:
            self.letter_index += 1

            if self.letter_index >= len(self.texts[self.text_index]):
                self.letter_index = self.letter_index

            screen.blit(self.box, (self.X_POSITION, self.Y_POSITION))
            text = self.font.render(self.texts[self.text_index][0:self.letter_index], False, (0, 0, 0))
            screen.blit(text, (self.X_POSITION + 60, self.Y_POSITION + 30))
    
    def next_text(self):
        self.text_index += 1
        self.letter_index = 0

        if self.text_index >= len(self.texts):
            self.reading = False