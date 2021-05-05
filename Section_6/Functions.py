# from random import shuffle
#
#
# def shuffler(my_list):
#     shuffle(my_list)
#     return my_list
#
#
# print(shuffler([1, 2, 3, 4, 5, 6, 7]))
#
#
# def get_the_total_number_from_this_list(my_list):
#     total = 0
#     for number in my_list:
#         total = total + number
#     return total
#
#
# print(get_the_total_number_from_this_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
#
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# add = [x for x in my_list if not x % 2]
# total = 0
# for c in add:
#     total = total + c
#     print(c)
# print("Total is {}" .format(total))
#
# print(add)
# x = 0;
# for number in my_list:
#     if number % 2 == 0:
#         print(number)
#         x = x + number
#     print(x)
#

def highest_stock(stock_prices):
    highest_prices = 0
    stock_name = ''
    for a, b in stock_prices:
        if b > highest_prices:
            highest_prices = b
            stock_name = a
        else:
            pass
    return (stock_name, highest_prices)


print(highest_stock([('APPL', 560), ('GOOD', 50056), ('MSFT', 10)]))
