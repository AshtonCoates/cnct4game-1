import pygame
import sys

'''
General game info:

The grid will be 6 rows x 7 columns, so it will look like this:

0000000
0000000
0000000
0000000
0000000
0000000
'''

# Initialize Pygame
pygame.init()

# Set the window size
width, height = 700, 600

# Create a window surface
screen = pygame.display.set_mode((width, height))

# Set the window title
pygame.display.set_caption("Connect 4")

# draw the board on the screen
screen.fill((51, 51, 255))
radius = 45
cir_color = (0, 0, 0)
col_intervals = [50.5 + i * 100 for i in range(7)] # this is a fancy thing called "list comprehension" that just quickly makes a list, no need to
row_intervals = [50.5 + i * 100 for i in range(6)] # worry about how it works but these are lists of where I want each black circle on the board to be
print(col_intervals, row_intervals)
for col in col_intervals:
    for row in row_intervals:
        pygame.draw.circle(screen, cir_color, (col, row), radius)

# this is some stuff to keep track of and display the pieces, we call them "sprites"
class Counter(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))  # Create a square surface for the sprite
        self.image.fill((255, 0, 0))  # Fill the surface with a red color
        self.rect = self.image.get_rect()  # Get the rectangle that encloses the sprite


# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the display
    pygame.display.flip()
    
