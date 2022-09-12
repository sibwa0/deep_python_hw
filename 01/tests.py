import unittest
import unittest.mock

from tictac_game import check_winner, got_victory, show_board, validate_input


class TestTicTac(unittest.TestCase):

    # validate_input
    def test_validate_input_correct_size_first(self):
        self.assertTrue(validate_input([0, 1, 2, 3, 4, 5, 6, 7, 8]))

    def test_validate_input_correct_size_second(self):
        self.assertTrue(validate_input([0, 1, 2, 3, 4]))

    def test_validate_input_wrong_size(self):
        self.assertFalse(validate_input([0, 1, 2, 3]))

    def test_validate_input_repeated_pos(self):
        self.assertFalse(validate_input([0, 1, 2, 3, 4, 4, 6, 7, 8]))

    def test_validate_input_out_of_range(self):
        self.assertFalse(validate_input([1, 2, 3, 4, 5, 6, 7, 8, 9]))

    # show_board
    def test_show_board_correct_input(self):
        print("test_show_board_correct_input")
        self.assertTrue(show_board([0, 1, 2, 3, 4, 5, 6, 7, 8]))

    def test_show_board_wrong_input(self):
        self.assertFalse(show_board([]))

    # got_victory
    # x cases
    def test_got_victory_x_wins_row(self):
        playground = [5, 4, 3]
        print("test_got_victory_x_wins_row")
        self.assertTrue(got_victory(playground))

    def test_got_victory_x_wins_column(self):
        playground = [6, 0, 3]
        print("test_got_victory_x_wins_column")
        self.assertTrue(got_victory(playground))

    def test_got_victory_x_wins_diag(self):
        playground = [2, 8, 4, 6]
        print("test_got_victory_x_wins_diag")
        self.assertTrue(got_victory(playground))

    def test_got_victory_x_doesnt_win(self):
        playground = [1, 5, 7, 2]
        print("test_got_victory_x_wins_diag")
        self.assertFalse(got_victory(playground))

    # o cases
    def test_got_victory_o_wins_raw(self):
        playground = [3, 5, 4]
        print("test_got_victory_o_wins_raw")
        self.assertTrue(got_victory(playground))

    def test_got_victory_o_wins_column(self):
        playground = [8, 5, 2]
        print("test_got_victory_o_wins_column")
        self.assertTrue(got_victory(playground))

    def test_got_victory_o_wins_diag(self):
        playground = [0, 2, 4, 8]
        print("test_got_victory_o_wins_diag")
        self.assertTrue(got_victory(playground))

    def test_got_victory_o_doesnt_win(self):
        playground = [0, 1, 3, 8]
        print("test_got_victory_o_doesnt_win")
        self.assertFalse(got_victory(playground))

    # check_winner
    def test_check_winner_draw(self):
        playground = [0, 1, 2, 5, 3, 6, 4, 8, 7]
        print("test_check_winner_draw")
        show_board(playground)
        self.assertFalse(check_winner(playground))

    def test_check_winner_x_wins(self):
        playground = [1, 0, 4, 2, 5, 3, 6, 8, 7]
        print("test_check_winner_x_wins")
        show_board(playground)
        self.assertTrue(check_winner(playground))

    def test_check_winner_o_wins(self):
        playground = [1, 0, 6, 4, 2, 7, 5, 8]
        print("test_check_winner_o_wins")
        show_board(playground)
        self.assertTrue(check_winner(playground))


if __name__ == '__main__':
    unittest.main()
