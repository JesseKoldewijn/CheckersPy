## Creates a checkers piece

# Imports external
import pygame

# Imports local
from checkers_game.constants import BROWN_LIGHT_ALT, BLACK, SQUARE_SIZE

class Piece: 
    # local variables - Class
    PIECE_PADDING = 12
    BORDER = 1.75

    def __init__(self, row, col, color):
        # Local variables - Init
        self.row = row
        self.col = col
        self.color = color
        self.king = False

        # Fixes possible direction to color team
        if self.color == BROWN_LIGHT_ALT:
            self.direction = -1
        else:
            self.direction = 1

        # Do postion calc on piece
        self.x = 0
        self.y = 0
        self.calc_position()
    
    # Method that calculates piece position
    def calc_position(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2
    
    # Method that handles piece becoming a king
    def make_king(self):
        self.king = True

    # Method that draws the piece visually
    def draw_piece(self, win):
        radius = SQUARE_SIZE//2 - self.PIECE_PADDING  
        pygame.draw.circle(win, BLACK, (self.x, self.y), radius + self.BORDER)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)

    # Debugger method that will show more detailed data on color prop that throws error
    def __represent__(self):
        return str(self.color)