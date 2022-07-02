#   Checkers game using python

# Imports external
import pygame

# Import local
from checkers_game.constants import SQUARE_SIZE, WIDTH, HEIGHT
from checkers_game.match import Match

# Runtime constants
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
MAX_FPS = 60

# Runtime display
pygame.display.set_caption('Checkers - Game made in Python')

# Method that gets row and col from mouse input
def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

# Main function
def main():
    # Local variables and function calls - Main
    run = True
    fps_handler = pygame.time.Clock()
    match = Match(WIN)

    # When game is running
    while run:
        fps_handler.tick(MAX_FPS) # Limiting max-fps for stability reasons
        
        # Check events during run and store them
        for event in pygame.event.get():

            # If user closes application
            if event.type == pygame.QUIT:
                run = False
            
            # If user clicks on window content
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                match.select(row, col)

        # Draws the tiles and updates display after event loop
        match.update()

    # Will run if user closed the app
    pygame.quit()

main()