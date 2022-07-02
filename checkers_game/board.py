## Board - Component

# Imports external
import pygame

# Imports local
from .constants import BROWN_DARK, BROWN_DARK_ALT, BROWN_LIGHT, COLS, OFF_WHITE, ROWS, SQUARE_SIZE
from checkers_game._parts.piece import Piece

class Board:
    # Initialize Class
    def __init__(self):
        # Local variables - Init
        self.board = []
        self.selected_piece = None
        self.black_left = self.white_left = 12
        self.black_kings = self.white_kings = 0
        self.create_board()

    # Draw the Board
    def draw_tiles(self, win):
        # Fill background
        win.fill(BROWN_DARK)

        # Fill in curtain spots on the background with alternate color
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, BROWN_LIGHT, (row*SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    
    # Defines board logic and defines the piece placements
    def create_board(self):
        for row in range(ROWS):
            # Create empty list to append into
            self.board.append([])
            for col in range(COLS):
                # Check rows
                # Like: row 0 mod 1 = empty & row 0 mod 2 = filled
                if col % 2 == ((row + 1) % 2):
                    # if row is 1 or 2 fill with white piece
                    if row < 3:
                        self.board[row].append(Piece(row, col, OFF_WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, BROWN_DARK_ALT))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    # Draws the actual pieces onto the board
    def draw_defined(self, win):
        self.draw_tiles(win)
        # Loops through the rows and cols
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                # Checks if col is not empty
                if piece != 0:
                    piece.draw_piece(win)
