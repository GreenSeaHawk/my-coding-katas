import pytest
from src.connect_four_game import ConnectFourGame
import pprint

class TestInitialisers:
    def test_initial_conditions(self):
        game = ConnectFourGame()
        
        assert game.turn == 0
        assert game.board == [
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None]
]   
        assert game.player == 'x'

class TestChangePlayer:
    def test_change_player(self):
        game = ConnectFourGame()

        assert game.player == 'x'

        game.change_player()

        assert game.player == 'o'

class TestPlay:
    def test_places_x_in_correct_col(self):
        game = ConnectFourGame()

        game.play(0)

        assert game.board == [
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    ['x', None, None, None, None, None, None]
]

    def test_places_x_in_correct_col_2(self):
        game = ConnectFourGame()

        game.play(5)

        assert game.board == [
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, 'x', None]
]
    # @pytest.mark.skip
    def test_places_x_and_o_in_correct_col(self):
        game = ConnectFourGame()
        # print(game.turn, game.player)
        game.play(5)
        # print(game.turn, game.player)
        game.play(5)
        # print(game.turn, game.player)

        # print(game.board)
        assert game.board == [
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, 'o', None],
    [None, None, None, None, None, 'x', None]
]
        
    def test_error_printed_and_no_turn_made(self,capfd):
        game = ConnectFourGame()

        with pytest.raises(Exception):
            game.play(8)
        assert game.board == [
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None]
]          
        assert game.turn == 0
        assert game.player == 'x'


    def test_error_printed_if_column_choice_invalid(self,capfd):
        game = ConnectFourGame()

        with pytest.raises(Exception):
            game.play(7)

    
    
    def test_error_printed_if_column_full(self,capfd):
        game = ConnectFourGame()

        game.play(6)
        game.play(6)
        game.play(6)
        game.play(6)
        game.play(6)
        game.play(6)

        assert game.board == [
    [None, None, None, None, None, None, 'o'],
    [None, None, None, None, None, None, 'x'],
    [None, None, None, None, None, None, 'o'],
    [None, None, None, None, None, None, 'x'],
    [None, None, None, None, None, None, 'o'],
    [None, None, None, None, None, None, 'x']
]

        with pytest.raises(Exception):
            game.play(6)

class TestGetBoard:
    def test_get_board_works(self):

        game = ConnectFourGame()

        game.play(6)
        game.play(6)
        game.play(6)
        game.play(6)
        game.play(6)
        game.play(6)

        assert game.get_board() == [
    [None, None, None, None, None, None, 'o'],
    [None, None, None, None, None, None, 'x'],
    [None, None, None, None, None, None, 'o'],
    [None, None, None, None, None, None, 'x'],
    [None, None, None, None, None, None, 'o'],
    [None, None, None, None, None, None, 'x']
]
class TestCheckWinner:
    def test_winner_found_when_horizontal(self):
        game = ConnectFourGame()

        game.play(0)
        game.play(0)
        game.play(1)
        game.play(0)
        game.play(2)
        game.play(0)
        game.play(3)

        assert game.check_winner() == 'x'

    def test_winner_found_when_horizontal_2(self):
        game = ConnectFourGame()

        game.play(0)
        game.play(1)
        game.play(2)
        game.play(3)
        game.play(4)
        game.play(5)
        game.play(6)
        game.play(0)
        game.play(2)
        game.play(0)
        game.play(3)
        game.play(0)
        game.play(4)
        game.play(1)
        game.play(5)

        assert game.check_winner() == 'x'
    
    def test_no_winner(self):
        game = ConnectFourGame()

        game.play(0)
        game.play(1)
        game.play(2)
        game.play(3)
        game.play(4)
        game.play(5)

        assert game.check_winner() == 'No winner yet'

    def test_winner_found_when_vertical(self):
        game = ConnectFourGame()

        game.play(0)
        game.play(1)
        game.play(0)
        game.play(1)
        game.play(0)
        game.play(1)
        game.play(0)

        assert game.check_winner() == 'x'

    def test_winner_found_when_vertical(self):
        game = ConnectFourGame()

        game.play(0)
        game.play(1)
        game.play(0)
        game.play(1)
        game.play(0)
        game.play(1)
        game.play(4)
        game.play(1)

        assert game.check_winner() == 'o'

    def test_winner_on_diagonal(self):
        game = ConnectFourGame()

        game.play(0)
        game.play(1)
        game.play(1)
        game.play(2)
        game.play(2)
        game.play(3)
        game.play(2)
        game.play(3)
        game.play(3)
        game.play(5)
        game.play(3)

        # pprint.pprint(game.get_board())
        assert game.check_winner() == 'x'

    # @pytest.mark.skip
    def test_winner_on_diagonal_2(self):
        game = ConnectFourGame()

        game.play(0)
        game.play(0)
        game.play(0)
        game.play(1)
        game.play(0)
        game.play(1)
        game.play(1)
        game.play(2)
        game.play(2)
        game.play(4)
        game.play(3)

        pprint.pprint(game.get_board())
        assert game.check_winner() == 'x'
        
