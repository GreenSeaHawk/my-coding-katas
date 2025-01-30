
'''
CHALLENGE

Practise your object-oriented skills to create a Connect Four class. Create a class called 
ConnectFourGame. A game should keep track of its state and should have a play method to allow a user to play.

Connect Four is a connection game in which the players first choose a color and then take turns dropping 
coloured discs from the top into a seven-column, six-row vertically suspended grid. The pieces fall straight down, 
occupying the next available space within the column. A player wins when they are the first to form a horizontal, 
vertical, or diagonal line of four of their own discs.

Methods Required
The get_board method should return the state of the board at any given time. It should be initialized as a 7 * 6 
matrix filled with None.

The get_player method should return a string indicating who the current player is. Use "x" and "o" to keep track 
of the players. "x" should go first.

The play method should take a column index number and should drop a counter into the correct column. If the column 
is full, it should raise an exception with the message "This column is full". The function does not return anything, 
but the state of the board can be checked by calling get_board and the next player can be checked by calling get_player.

The check_winner method should check for a winner in the instance of the Connect Four game. It should return False 
for no winner, or the winner if there are 4 connected counters in either horizontal, vertical or diagonal directions.

You may find it useful to write additional methods as helpers or bring in functions from other katas. Make sure you 
have sufficient test coverage on all of your methods.

Example Functionality
game = ConnectFourGame()

game.get_board()
#[
#     [None, None, None, None, None, None, None],
#     [None, None, None, None, None, None, None],
#     [None, None, None, None, None, None, None],
#     [None, None, None, None, None, None, None],
#     [None, None, None, None, None, None, None],
#     [None, None, None, None, None, None, None]
# ]
game = ConnectFourGame()

game.get_player() # "x"
game = ConnectFourGame()

game.play(3)

game.get_board()
# [
#     [None, None, None, None, None, None, None],
#     [None, None, None, None, None, None, None],
#     [None, None, None, None, None, None, None],
#     [None, None, None, None, None, None, None],
#     [None, None, None, None, None, None, None],
#     [None, None, None, "x", None, None, None]
# ]


game.get_player() # "o"
game = ConnectFourGame()

game.play(3)
game.play(2)
game.play(3)
game.play(1)
game.play(3)
game.play(0)
game.play(3)

game.get_board()
#[
    # [None, None, None, None, None, None, None],
    # [None, None, None, None, None, None, None],
    # [None, None, None, "x", None, None, None],
    # [None, None, None, "x", None, None, None],
    # [None, None, None, "x", None, None, None],
    # ["o", "o", "o", "x", None, None, None]
# ]

game.check_winner() # "x"'''


class ConnectFourGame():
    def __init__(self):
        self.turn = 0
        self.board = [
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None]
]
        self.player = 'x'

    def change_player(self):
        self.turn += 1
        if self.turn % 2 == 0:
            self.player = 'x'
        if self.turn % 2 == 1:
            self.player = 'o'

    def play(self,col):
        play_success = False
        if 0 <= col <= 6 and type(col) == int:
            for row in range(5,-1,-1):
                if not self.board[row][col]:
                    self.board[row][col] = self.player
                    self.change_player()
                    play_success = True
                    break
        if not play_success:
            raise Exception('Invalid column choice, please go again')
    
    def get_board(self):
        return self.board
        
    def check_winner(self):
        winner = False
        #check for horizontal victory
        for row in self.board:
            count = 1
            for i in range(1, len(row)):
                if row[i] == row[i - 1] and row[i]:
                    count += 1
                    if count == 4:
                        winning_player = row[i]
                        winner = True
                else:
                    count = 1
        #check for vertical victory
        for i in range(7):
            count = 1
            for j in range(1,6):
                if self.board[j][i] == self.board[j-1][i] and self.board[j][i]:
                    count += 1
                    if count == 4:
                        winning_player = self.board[j][i]
                        winner = True
                else:
                    count = 1

        #check for diagonal victory
        for i in range(4):
            for j in range(5,2,-1):
                if self.board[j][i] == self.board[j-1][i+1] == self.board[j-2][i+2] == self.board[j-3][i+3] and self.board[j][i]:
                    winning_player = self.board[j][i]
                    winner = True

        for i in range(4):
            for j in range(2,-1,-1):
                if self.board[j][i] == self.board[j+1][i+1] == self.board[j+2][i+2] == self.board[j+3][i+3] and self.board[j][i]:
                    winning_player = self.board[j][i]
                    winner = True

        if winner:
            return winning_player
        else:
            return 'No winner yet'
                


        
