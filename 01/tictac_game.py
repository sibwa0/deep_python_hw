def input_data():
    return [int(a) for a in list(input())]


def validate_input(playground):
    unique_positions = set(playground)
    size_playground = len(playground)

    if size_playground < 5 or size_playground > 9:
        print(
            f"Not Valid\nOut of range commited steps (>=5 and <=9)\n"
            f"Your amount of steps = {size_playground}")
        return False

    if size_playground != len(unique_positions):
        print(
            f"Not Valid\nSeveral steps has the same position\n"
            f"playground = {size_playground},"
            f"unique_positions = {len(unique_positions)}")
        return False

    sorted_playground = sorted(playground)

    if sorted_playground[0] < 0 or sorted_playground[size_playground - 1] > 8:
        print(
            f"Not Valid\nIncorrect input data (index >= 0 and <=8)\n"
            f"min index = {sorted_playground[0]},"
            f"max index = {sorted_playground[8]}")
        return False

    print(f"Valid input data = {playground}")
    return True


def show_board(playground):
    if (validate_input(playground)):
        print("Result board state:")
        x_pos = [
            playground[i] for i in range(0, len(playground), 2) if i % 2 == 0
        ]
        o_pos = [
            playground[i] for i in range(1, len(playground), 2) if i % 2 != 0
        ]
        for i in range(9):
            if i in x_pos:
                print("x", end="")
            elif i in o_pos:
                print("o", end="")
            else:
                print("-", end="")

            if (i - 2) % 3 == 0:  # to form standart tictac board
                print()

        return True
    return False


def got_victory(tmp_set):
    if {0, 1, 2}.issubset(tmp_set) or \
            {3, 4, 5}.issubset(tmp_set) or \
            {6, 7, 8}.issubset(tmp_set):
        return True

    if {0, 3, 6}.issubset(tmp_set) or \
            {1, 4, 7}.issubset(tmp_set) or \
            {2, 5, 8}.issubset(tmp_set):
        return True

    if {0, 4, 8}.issubset(tmp_set) or \
            {2, 4, 6}.issubset(tmp_set):
        return True

    return False


def check_winner(x_pos, o_pos):
    if (got_victory(set(x_pos))):
        print("x wins")
        return True

    if (got_victory(set(o_pos))):
        print("o wins")
        return True

    print("draw")
    return False
