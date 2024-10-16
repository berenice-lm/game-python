import pygame

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Affichage texte avec saut de ligne")

# Couleurs et police
white = (255, 255, 255)
black = (0, 0, 0)
font = pygame.font.Font(None, 36)

# Fonction pour dessiner du texte sur plusieurs lignes
def draw_text(screen, text_list, x, y, font, color):
    for i, text in enumerate(text_list):
        rendered_text = font.render(text, True, color)
        screen.blit(rendered_text, (x, y + i * 40))  # Espacement entre les lignes

# Boucle principale
running = True
while running:
    screen.fill(black)
    
    # Texte avec retour à la ligne
    dialog = ["<- Ville D", "Ville S ->"]
    draw_text(screen, dialog, 100, 200, font, white)
    
    # Affichage
    pygame.display.flip()
    
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()