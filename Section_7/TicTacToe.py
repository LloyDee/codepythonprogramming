from IPython.display import clear_output

board = [' '] * 10


def display_board():
    clear_output()
    print("*****************************\n*****\t| " + board[0] + ' | ' + board[1] + ' | ' + board[
        2] + ' |\t*****\n*****\t| ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ''
                                                                                       ' |\t*****\n*****\t| ' + board[
              6] + ' | ' + board[7] + ' | ' + board[8] + ' |\t*****\n*****************************')


def player_input():
    player_1 = input("Select your player 'X' or 'O':\t")
    return player_1


def select_board():
    num_board = int(input("Select number in board (1-9):\n"))
    return num_board


def play_the_game():
    q = True
    while q:
        board[select_board() - 1] = player_input()
        clear_output()
        display_board()


play_the_game()
