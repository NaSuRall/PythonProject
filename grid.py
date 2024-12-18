import random
import pygame
from constants import TILE_SIZE, MARGIN, WHITE, GRAY, RED, DARK_GRAY, FONT, BLACK

class Grid:
    def __init__(self, rows, cols, bombs):
        self.rows = rows
        self.cols = cols
        self.bombs = bombs
        self.grid = self.create_grid()
        self.revealed = [[False for _ in range(cols)] for _ in range(rows)]
        self.flags = set()

    def create_grid(self):
        grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        bomb_positions = random.sample([(r, c) for r in range(self.rows) for c in range(self.cols)], self.bombs)
        for r, c in bomb_positions:
            grid[r][c] = -1
            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < self.rows and 0 <= nc < self.cols and grid[nr][nc] != -1:
                        grid[nr][nc] += 1
        return grid

    def draw(self, screen):
        for row in range(self.rows):
            for col in range(self.cols):
                x = col * (TILE_SIZE + MARGIN)
                y = row * (TILE_SIZE + MARGIN)
                rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)

                if self.revealed[row][col]:
                    pygame.draw.rect(screen, WHITE, rect)
                    if self.grid[row][col] > 0:
                        text = FONT.render(str(self.grid[row][col]), True, BLACK)
                        screen.blit(text, (x + TILE_SIZE // 3, y + TILE_SIZE // 4))
                else:
                    pygame.draw.rect(screen, GRAY, rect)
                    if (row, col) in self.flags:
                        pygame.draw.circle(screen, RED, rect.center, TILE_SIZE // 4)

                pygame.draw.rect(screen, DARK_GRAY, rect, 1)

    def reveal_tile(self, row, col):
        if self.revealed[row][col] or (row, col) in self.flags:
            return
        self.revealed[row][col] = True
        if self.grid[row][col] == 0:
            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < self.rows and 0 <= nc < self.cols:
                        self.reveal_tile(nr, nc)

    def toggle_flag(self, row, col):
        if (row, col) in self.flags:
            self.flags.remove((row, col))
        else:
            self.flags.add((row, col))

    def is_bomb(self, row, col):
        return self.grid[row][col] == -1

    def check_win(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] != -1 and not self.revealed[row][col]:
                    return False
        return True
