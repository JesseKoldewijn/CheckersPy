## Match - Component

# Imports external
import pygame

# Imports local
from .board import Board
from .constants import VALID_MOVE, BROWN_DARK_ALT, OFF_WHITE, SQUARE_SIZE

class Match:
    # Init functionality that's called on initial class call
    def __init__(self, win):
        self._init()
        self.win = win
    
    # Method for updating match state
    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    # Method thats called by class init
    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = BROWN_DARK_ALT
        self.valid_moves = {}

    # Method that sets match winner
    def winner(self):
        return self.board.winner()

    # Method that resets match
    def reset(self):
        self._init()

    # Method that defines selected piece and places logic into the functionality
    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
            
        return False

    # Method to move piece to new location
    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False

        return True

    # Method that shows circle on spot for valid moves
    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, VALID_MOVE, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

    # Method that changes the turn to the other player when this needs to happen
    def change_turn(self):
        self.valid_moves = {}
        if self.turn == BROWN_DARK_ALT:
            self.turn = OFF_WHITE
        else:
            self.turn = BROWN_DARK_ALT