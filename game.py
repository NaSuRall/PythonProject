import pygame
import sys
from constants import BLACK, WHITE, GRAY, FONT
from grid import Grid

class Game:
    def __init__(self):
        pygame.display.set_caption("Démineur")
        self.screen = pygame.display.set_mode((1080, 720))
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            difficulty = self.show_menu()
            self.play_game(difficulty)

    def show_menu(self):
        while True:
            self.screen.fill(BLACK)
            text = FONT.render("Choisissez une difficulté:", True, WHITE)
            self.screen.blit(text, (20, 20))

            easy_button = pygame.Rect(20, 80, 200, 50)
            medium_button = pygame.Rect(20, 150, 200, 50)
            hard_button = pygame.Rect(20, 220, 200, 50)

            pygame.draw.rect(self.screen, GRAY, easy_button)
            pygame.draw.rect(self.screen, GRAY, medium_button)
            pygame.draw.rect(self.screen, GRAY, hard_button)

            easy_text = FONT.render("Facile (9x9)", True, BLACK)
            medium_text = FONT.render("Moyen (16x16)", True, BLACK)
            hard_text = FONT.render("Difficile (30x16)", True, BLACK)

            self.screen.blit(easy_text, (30, 90))
            self.screen.blit(medium_text, (30, 160))
            self.screen.blit(hard_text, (30, 230))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if easy_button.collidepoint(event.pos):
                        return (9, 9, 10)
                    elif medium_button.collidepoint(event.pos):
                        return (16, 16, 40)
                    elif hard_button.collidepoint(event.pos):
                        return (16, 30, 99)

    def play_game(self, difficulty):
        rows, cols, bombs = difficulty
        grid = Grid(rows, cols, bombs)
        running = True

        while running:
            self.screen.fill(BLACK)
            grid.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    col = x // (30 + 2)
                    row = y // (30 + 2)

                    if event.button == 1:  # Left click
                        grid.reveal_tile(row, col)
                        if grid.is_bomb(row, col):
                            running = False
                    elif event.button == 3:  # Right click
                        grid.toggle_flag(row, col)

            if grid.check_win():
                running = False
