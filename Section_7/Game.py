game_list = [0, 1, 2]


def display_game(game_list):
    print("Here is the current list:")
    print(game_list)


def position_choice():
    choice = 'wrong'

    while choice not in ['0', '1', '2']:
        choice = input("Pick a position (0,1,2):")
        if choice not in ['0', '1', '2']:
            print("Sorry, invalid choice! ")
    return int(choice)


def replacement_choice(game_list, position):
    user_placement = input("Type a string to place at position: ")

    game_list[position] = user_placement

    return game_list


def game_on():
    input_ = input("Want to keep playing? Y or N")
    if input_ == 'Y':
        return True
    else:
        False


def play():
    replacement_choice(game_list, position_choice())
    display_game(game_list)
    while game_on():
        replacement_choice(game_list, position_choice())
        display_game(game_list)


play()