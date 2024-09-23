class Board:

    '''
    General game info:

    The grid will be 6 rows x 7 columns, so it will look like this:

    0000000
    0000000
    0000000
    0000000
    0000000
    0000000

    The below methods are the ones that we need to implement to make the game work. The __init__ method is complete,
    and the __repr__ method is just helpful for debugging, but the other 3 methods need to be implemented.

    Details about what they need to do are included in each method.
    '''
    
    def __init__(self):
        self.board = [[0 for _ in range(7)] for _ in range(6)] # this is a fancy thing called list comprehension
        self.player = 1

    def switch_player(self):
        '''
        this method doesn't need to return anything, it just needs to set self.player to 1 if it's 2, and 2 if it's 1
        '''
        pass

    def drop_piece(self, col:int) -> bool:
        '''
        This method needs to update self.board with the new piece, changing 0 to either 1 or 2 depending on the player. 
        The piece should be dropped in the lowest available row in the given column. Also, we can't allow a piece to be 
        dropped in a full column, so if the column is full, do nothing. Finally, main.py needs to know if the piece was
        successfully dropped to know whether to switch the player or not, so this should return true if the piece was
        dropped and false if the column was full.
        '''
        return True

    def check_win(self) -> bool:
        '''
        This needs to return a true if the game is won, and false if it's not. The game is won if there are 4 piece in a row.
        This will be the trickist one; start by just checking along the row and columns, and then try to approach the diagonals.
        '''
        pass

    # this method tells our class how to print itself when we call print() on it
    def __repr__(self):
        print_str = ''
        for row in self.board:
            print_str += ''.join(str(cell) for cell in row) + '\n'
        return print_str




'''
This is a way to run the code in this file only if you run it directly. We import this file in main.py,
but the below block of code will not be executed when we do that. This is useful for testing, you can
add any test code you want inside the if statement below.
'''
if __name__ == '__main__':
    board = Board()
    print(board)