## Board - Component

# Imports external
import pygame

# Imports local
from .constants import BROWN_DARK, BROWN_LIGHT, ROWS, SQUARE_SIZE

class Board:
    # Initialize Class
    def __init__(self):
        # Local variables - Init
        self.board = []
        self.selected_piece = None
        self.black_left = self.white_left = 12
        self.black_kings = self.white_kings = 0

    # Draw the Board
    def draw_tiles(self, win):
        # Fill background
        win.fill(BROWN_DARK)

        # Fill in curtain spots on the background with alternate color
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, BROWN_LIGHT, (row*SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    
    # Defines board logic and draws the pieces
    def create_board(self):
        pass