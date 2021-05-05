# def get_name():
#     name = input("what is your name?\n")
#     return name
#
#
# def total(a, b):
#     return a + b
#
# print(total(12, 8))
#
#
# def say_hello():
#     print("Hello "+get_name())
#
# say_hello()

# def even_checker(number):
#     result = number % 2 == 0
#     print("{} is an even number?\nThat is {}".format(number,result))
#     return result
#
# even_checker(16)

def return_true_if_there_is_even_number_in_the_list(my_list):
    for number in my_list:
        if number % 2 == 0:
            return True
        else:
            pass
    return False


def return_all_even_number_in_a_list(my_list):
    even_number = []
    for number in my_list:
        if number % 2 == 0:
            even_number.append(number)
        else:
            pass
    return even_number


print(return_true_if_there_is_even_number_in_the_list([5, 9, 3, 7, 12]))
print(return_all_even_number_in_a_list([5, 9, 2, 18, 12]))


def employee_that_has_the_most_hours(work_hours):
    current_max = 0
    employee_of_the_month = ""

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_the_month = employee
        else:
            pass
    return employee_of_the_month, current_max


print(employee_that_has_the_most_hours([('Lloyd', 40), ('Edith', 922), ('Alex', 299)]))
