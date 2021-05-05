import random

list_of_name = ['Lloyd', 'Edith', 'Lupita', 'Pintac']
list_of_pet = ['cats', 'dogs', 'goats', 'cows', 'foxes', 'horses']
list_of_fruit = ['apple', 'orange', 'avocado', 'mango', 'pineapple', 'coconut']


def get_random(list_here):
    return list_here[random.randint(0, len(list_here) - 1)]


print('{} has {} {} and likes {}'.format(get_random(list_of_name), random.randint(1, 5),
                                         get_random(list_of_pet),
                                         get_random(list_of_fruit)))


