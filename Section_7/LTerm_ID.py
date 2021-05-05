lterm_no = 'L6016589'
eagle_id = 'PLA1027'
my_pass = 'Panther2'

my_file_location = 'C:\\Users\\loyd_\\Desktop\\myID.txt'


def get_lterm():
    return 'LTerm no.- {}'.format(lterm_no)


def get_eagle_id():
    return 'Eagle ID - {}'.format(eagle_id)


def get_pass():
    return 'Password - {}'.format(my_pass)


def get_info():
    display = "{}\n{}\n{}".format(get_lterm(), get_eagle_id(), get_pass())
    print(display)
    prompt = input('Want to export?\t Y or N:\t')
    if prompt.upper() == 'Y':
        with open(my_file_location, 'w') as my_file:
            my_file.write(display)
            print('Details are copied to {}'.format(my_file_location))
    else:
        print('Done')

def is_valid():
    name = input('Enter name: \t')
    return name == 'Lloyd'




def prompter():
    if is_valid():
        while True:
            options = input("Please select your options:\nLTerm No.\t'L'\nEagle ID\t'E'\nPassword\t'P'\nAll info\t'A'\nQuit\t\t'Q'\n")
            if options.upper() == 'L':
                print(get_lterm())
            elif options.upper() == 'E':
                print(get_eagle_id())
            elif options.upper() == 'P':
                print(get_pass())
            elif options.upper() == 'A':
                get_info()
            elif options.upper() == 'Q':
                break
            else:
                print('Wrong input! Please try again')
                prompter()
    else:
        print('Warning: Name cannot be found! Please try again\n')
        prompter()


prompter()
