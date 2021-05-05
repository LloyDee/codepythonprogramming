def get_palindrome(word):
    my_pal = []
    for counter in range(0, len(word)):
        if word[counter].upper() == word[counter].upper()[::-1]:
            my_pal.append(word[counter].upper())
    print('Palindrome: {}'.format(my_pal))


with open('C:\\Users\\loyd_\\Desktop\\Observation.txt', 'r+') as my_file:
    x = my_file.read()
    my_list_of_words = x.split()

list_here = 'loyol', 'manam', 'casperepdsc', '12321'

get_palindrome(list_here)
