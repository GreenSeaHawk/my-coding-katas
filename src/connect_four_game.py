
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