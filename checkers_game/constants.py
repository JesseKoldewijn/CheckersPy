## Constants - Global

# Imports external
import pygame

# Dimensions
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

# Colors - RGB
BROWN_DARK = (75,60,40)
BROWN_DARK_ALT = (55,45,30)
BROWN_LIGHT = (190,155,105)
BROWN_LIGHT_ALT = (210,170,125)
ORANGE = (245,100,5)
RED = (255,0,0)
OFF_WHITE = (207,179,140)
BLACK = (0,0,0)
VALID_MOVE = (207,179,140)

# Assets
CROWN = pygame.transform.scale(pygame.image.load('checkers_game/assets/crown.png'), (50, 50))