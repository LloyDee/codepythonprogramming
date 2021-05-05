from datetime import datetime
import time
import random


def lottery_pick():
    x_list = []
    for x in range(1, 7):
        y = random.randint(1, 100)
        x_list.append(y)
    print('Lottery pick is: \t{}'.format(x_list))
    return x_list


def your_entry():
    picks = []
    for x in range(1, 7):
        pick = input('Enter your lottery number {}: \t'.format(x))
        picks.append(int(pick))
    print('Your lot. pick is: {}'.format(picks))
    return picks


def get_result(x, y):
    winning_number = []
    for x_counter in range(0, len(x)):
        for counter in range(0, len(x)):
            if x[counter] == y[x_counter]:
                winning_number.append(x[counter])
    if len(winning_number) == 1:
        print('You match 1 winning number: {}'.format(winning_number))
    elif len(winning_number) == 2:
        print('You match 2 winning number: {}'.format(winning_number))
    elif len(winning_number) == 3:
        print('You match 3 winning number: {}'.format(winning_number))
    elif len(winning_number) == 4:
        print('You won a Quick Lottery:: {}'.format(winning_number))
    elif len(winning_number) == 5:
        print('You won a Super Lottery:: {}'.format(winning_number))
    elif len(winning_number) == 6:
        print('You won a Mega Lottery: {}'.format(winning_number))
    else:
        print('You LOST!!! The winning numbers {}'.format(y))


get_result(your_entry(), lottery_pick())
