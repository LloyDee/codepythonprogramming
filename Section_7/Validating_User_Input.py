def user_choice():
    range_numbers = range(0, 11)
    valid_numbers = False
    choice = 'Not Digit'

    while (not choice.isdigit()) or valid_numbers == False:

        choice = input("Please enter a number (1-10)\n")

        # DIGIT CHECK
        if not choice.isdigit():
            print("Wrong Input! Enter a valid number")

        # RANGE CHECK
        if choice.isdigit():
            if int(choice) in range_numbers:
                valid_numbers = True
            else:
                print("Wrong Input! Out of range")
                pass

    return choice


print(user_choice())
