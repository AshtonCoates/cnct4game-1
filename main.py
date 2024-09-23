
import pygame
import sys
from board import Board

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
    def __init__(self, player):
        super().__init__()
        self.image = pygame.Surface((90, 90), pygame.SRCALPHA)  # Create a square surface for the sprite
        self.rect = self.image.get_rect()  # Get the rectangle that encloses the sprite
        if player == 1:
            pygame.draw.circle(self.image, (255, 0, 0), (45, 45), 45)
        elif player == 2:
            pygame.draw.circle(self.image, (255, 255, 0), (45, 45), 45)

pieces = pygame.sprite.Group()

def create_board(board):
    pieces.empty()
    for row_index, row in enumerate(board):
        for col_index, piece in enumerate(row):
            if piece != 0:
                counter = Counter(piece)
                counter.rect.x = col_intervals[col_index] - 45
                counter.rect.y = row_intervals[row_index] - 45
                pieces.add(counter)
    pieces.update()
    pieces.draw(screen)

def display_winner(winner):
    while True:
            font = pygame.font.Font(None, 72)
            text = font.render(f"Player {winner} wins!", True, (255, 255, 255))
            text_rect = text.get_rect(center=(width // 2, height // 2))
            screen.blit(text, text_rect)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

board = Board()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            col = (x) // 100
            successful_drop = board.drop_piece(col)
            if successful_drop:
                create_board(board.board)
                if board.check_win():
                    display_winner(board.player)
                board.switch_player()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)
