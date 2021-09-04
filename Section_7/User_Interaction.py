row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]


def display():
    print(row1)
    print(row2)
    print(row3)


def is_within_range(user_input):
    if int(user_input) in range(1, 4):
        return True
    else:
        return False


def is_valid(user_input):
    if user_input.isdigit():
        new_int_user_input = int(user_input)
        if is_within_range(new_int_user_input):
            return True
    else:
        return False


def validator(input_number):
    while not is_valid(input_number):
        input_number = input("Wrong input! Enter a valid number (1-3)\n")
    return input_number


def play1():
    quit_game = False
    while not quit_game:
        num_row = input("Enter row\n")
        row = int(validator(num_row))

        num_col = input("Enter column\n")
        col = int(validator(num_col))

        quit_game = tic_tac(col, quit_game, row)


def tic_tac(col, quit_game, row):
    if row == 1:
        print("column: {}\nRow: {}".format(col, row))
        row1[int(col) - 1] = "X"
        quit_game = score_(quit_game)
    elif row == 2:
        print("column: {}\nRow: {}".format(col, row))
        row2[int(col) - 1] = "X"
        quit_game = score_(quit_game)

    elif row == 3:
        print("column: {}\nRow: {}".format(col, row))
        row3[int(col) - 1] = "X"
        quit_game = score_(quit_game)
    return quit_game


def score_(quit_game):
    display()
    if quit_the_game():
        quit_game = True
    return quit_game


def quit_the_game():
    quit_ = input('Would you like to keep Quit?\nY or N\n')
    if quit_ == 'Y':
        return True
    else:
        False


play1()
