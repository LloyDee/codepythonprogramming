def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)


def play():
    user_input_row = int(input("Select a row\n"))
    user_input_col = int(input("Select a col\n"))
    if user_input_row == 1:
        row1[user_input_col] = "X"
    elif user_input_row == 2:
        row2[user_input_col] = "X"
    elif user_input_row == 3:
        row3[user_input_col] = "X"


row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']


def start_game():
    play()
    display(row1, row2, row3)


start_game()
