## Board - component

# Imports external
import pygame

# Imports local
from .constants import BLACK, BROWN_DARK, BROWN_LIGHT, OFF_WHITE, ROWS, BROWN_DARK_ALT, SQUARE_SIZE, COLS
from ._parts.piece import Piece

class Board:
    # Init functionality that's called on initial class call
    def __init__(self):
        self.board = []
        self.black_left = self.OFF_WHITE_left = 12
        self.black_kings = self.OFF_WHITE_kings = 0
        self.create_board()
    
    # Method for drawing the squares onto the board
    def draw_squares(self, win):
        win.fill(BROWN_DARK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, BROWN_LIGHT, (row*SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    # Method for moving the piece on the board
    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move_piece(row, col)

        if row == ROWS - 1 or row == 0:
            piece.make_king()
            if piece.color == OFF_WHITE:
                self.OFF_WHITE_kings += 1
            else:
                self.black_kings += 1 

    # Method to get the selected piece by column and row
    def get_piece(self, row, col):
        return self.board[row][col]

    # Method that places the pieces onto the board
    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row +  1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, OFF_WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, BROWN_DARK_ALT))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)
        
    # Method that draws the squares onto the board    
    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw_piece(win)

    # Method for removal of piece
    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == BROWN_DARK_ALT:
                    self.black_left -= 1
                else:
                    self.OFF_WHITE_left -= 1
    
    # Method that's called if there's a winner
    def winner(self):
        if self.black_left <= 0:
            return OFF_WHITE
        elif self.OFF_WHITE_left <= 0:
            return BROWN_DARK_ALT
        
        return None 
    
    # Method that defines valid moves
    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == BROWN_DARK_ALT or piece.king:
            moves.update(self._traverse_left(row -1, max(row-3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row -1, max(row-3, -1), -1, piece.color, right))
        if piece.color == OFF_WHITE or piece.king:
            moves.update(self._traverse_left(row +1, min(row+3, ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row +1, min(row+3, ROWS), 1, piece.color, right))
    
        return moves

    # Traversal to left side of piece
    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break
            
            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last
                
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)
                    moves.update(self._traverse_left(r+step, row, step, color, left-1,skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, left+1,skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            left -= 1
        
        return moves

    # Traversal to right side of piece
    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break
            
            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r,right)] = last + skipped
                else:
                    moves[(r, right)] = last
                
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)
                    moves.update(self._traverse_left(r+step, row, step, color, right-1,skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, right+1,skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1
        
        return moves