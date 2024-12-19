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
            player_name = self.ask_for_name()
            self.play_game(difficulty, player_name)

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
                        return (9, 9, 30)
                    elif medium_button.collidepoint(event.pos):
                        return (16, 16, 40)
                    elif hard_button.collidepoint(event.pos):
                        return (16, 30, 99)

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
                            return text  # Return player's name when Enter is pressed
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

            # Display player's name and score (above the grid)
            score_text = FONT.render(f"{player_name}'s Score: {score}", True, WHITE)
            self.screen.blit(score_text, (20, 20))

            # Draw the grid below the score display
            grid.draw(self.screen)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    col = x // (30 + 2)
                    row = (y - 60) // (30 + 2)  # Adjust row calculation by subtracting 60 for the space above

                    if event.button == 1:  # Left click
                        grid.reveal_tile(row, col)
                        if grid.is_bomb(row, col):
                            running = False
                    elif event.button == 3:  # Right click
                        grid.toggle_flag(row, col)

            if grid.check_win():
                score += 10  # Increment score when the player wins
                running = False

        # Game over, show final score
        self.screen.fill(BLACK)
        game_over_text = FONT.render(f"Game Over! {player_name}, your score: {score}", True, WHITE)
        self.screen.blit(game_over_text, (20, 100))
        pygame.display.flip()
        pygame.time.wait(3000)  # Wait for 3 seconds before quitting