import pygame
import sys
from constants import BLACK, WHITE, GRAY, FONT, DARK_GRAY
from grid import Grid

class Game:
    def __init__(self):
        pygame.display.set_caption("Démineur")
        self.screen = pygame.display.set_mode((1080, 720))
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            difficulty = self.show_menu()
            player_name = self.ask_for_name()
            self.play_game(difficulty, player_name)

    def show_menu(self):
        while True:
            self.screen.fill(BLACK)


            title_text = FONT.render("Démineur", True, WHITE)
            self.screen.blit(title_text, (20, 20))


            difficulty_text = FONT.render("Choisissez une difficulté:", True, WHITE)
            self.screen.blit(difficulty_text, (20, 80))


            easy_button = pygame.Rect(20, 140, 200, 50)
            medium_button = pygame.Rect(20, 210, 200, 50)
            hard_button = pygame.Rect(20, 280, 200, 50)

            pygame.draw.rect(self.screen, GRAY, easy_button)
            pygame.draw.rect(self.screen, GRAY, medium_button)
            pygame.draw.rect(self.screen, GRAY, hard_button)

            easy_text = FONT.render("Facile (9x9)", True, BLACK)
            medium_text = FONT.render("Moyen (16x16)", True, BLACK)
            hard_text = FONT.render("Difficile (30x16)", True, BLACK)

            self.screen.blit(easy_text, (30, 150))
            self.screen.blit(medium_text, (30, 220))
            self.screen.blit(hard_text, (30, 290))

            # Dessiner une grille vide
            self.draw_empty_grid()

            pygame.display.flip()

            # Gestion des événements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if easy_button.collidepoint(event.pos):
                        return (9, 9, 30)
                    elif medium_button.collidepoint(event.pos):
                        return (16, 16, 40)
                    elif hard_button.collidepoint(event.pos):
                        return (16, 30, 99)

    #creer une grille vide a utiliser dans le menue
    def draw_empty_grid(self):
        # Taille des cases
        TILE_SIZE = 30
        MARGIN = 2

        # Définir la taille d'une grille de démonstration (9x9 par exemple)
        rows, cols = 9, 9

        # Calculer le point de départ pour centrer la grille
        start_x = (self.screen.get_width() - (cols * (TILE_SIZE + MARGIN))) // 2
        start_y = 400  # Position verticale fixe

        for row in range(rows):
            for col in range(cols):
                x = start_x + col * (TILE_SIZE + MARGIN)
                y = start_y + row * (TILE_SIZE + MARGIN)
                rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(self.screen, GRAY, rect)  # Case grise
                pygame.draw.rect(self.screen, DARK_GRAY, rect, 1)

    def ask_for_name(self):
        # Ask for player's name
        input_box = pygame.Rect(200, 300, 400, 50)
        color_inactive = pygame.Color('lightskyblue3')
        color_active = pygame.Color('dodgerblue2')
        color = color_inactive
        text = ''
        active = False

        while True:
            self.screen.fill(BLACK)
            label_text = "Votre pseudo:"
            label_surface = FONT.render(label_text, True, WHITE)
            self.screen.blit(label_surface, (input_box.x, input_box.y - 40))
            pygame.draw.rect(self.screen, color, input_box, 2)
            text_surface = FONT.render(text, True, WHITE)
            self.screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        active = True
                        color = color_active
                    else:
                        active = False
                        color = color_inactive
                elif event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            #retourne le pseudo du joueur quand la touche entrer est pressé
                            return text
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode

    def play_game(self, difficulty, player_name):
        rows, cols, bombs = difficulty
        grid = Grid(rows, cols, bombs)
        running = True
        score = 0

        while running:
            self.screen.fill(BLACK)

            #afffiche le nom et le score du joueur
            score_text = FONT.render(f"{player_name}'s Score: {score}", True, WHITE)
            self.screen.blit(score_text, (20, 20))

            #dessine la grille
            grid.draw(self.screen)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    #permet de calculer la taille des case
                    col = x // (30 + 2)
                    row = (y - 60) // (30 + 2)

                    #clique gauche
                    if event.button == 1:
                        grid.reveal_tile(row, col)
                        if grid.is_bomb(row, col):
                            running = False
                    # clique droit
                    elif event.button == 3:
                        grid.toggle_flag(row, col)

            if grid.check_win():
                score += 10
                running = False

        # une fois la partie terminer
        self.screen.fill(BLACK)
        game_over_text = FONT.render(f"Game Over! {player_name}, your score: {score}", True, WHITE)
        self.screen.blit(game_over_text, (20, 100))
        pygame.display.flip()
        #quitte la partie au bout de 3 secondes
        pygame.time.wait(3000)
