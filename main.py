#   Checkers game using python

# Imports external
import pygame

# Import local
from checkers_game.constants import WIDTH, HEIGHT
from checkers_game.board import Board

# Runtime constants
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
MAX_FPS = 60

# Runtime display
pygame.display.set_caption('Checkers - Game made in Python')

def main():
    # Local variables - Main
    run = True
    fps_handler = pygame.time.Clock()
    board = Board()

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
               pass

        # Draws the tiles and updates display after event loop
        board.draw_defined(WIN)
        pygame.display.update()

    # Will run if user closed the app
    pygame.quit()

main()