# def square(num):
#     return num ** 2
#
#
# my_num = [1, 2, 3, 4, 5, ]
#
# for item in map(square, my_num):
#     print(item)
#
# print(list(map(square, my_num)))
#
#
# def splicer(mystring):
#     if len(mystring) % 2 == 0:
#         return 'EVEN'
#     else:
#         return mystring
#
#
# names = ['Lloyd', 'Martin', 'Edith']
#
#
# def get_even(a):
#     ad = []
#     for x in a:
#         if len(x) % 2 == 0:
#             ad.append('EVEN')
#         else:
#             ad.append(x)
#     return ad
#
#
# print(get_even(['Sasm', 'Vsic', 'Anness']))
# # Panther, Tiger, EVEN, EVEN
# print(list(map(splicer, names)))

print('## MAP FUNCTION ##')


def square(num):
    return num ** 2


my_number = [1, 2, 3, 4, 5, 6]

for x in map(square, my_number):
    print(x)

print(list(map(square, my_number)))


def even_string(string):
    if len(string) % 2 == 0:
        return 'EVEN'
    else:
        return string


my_string = ['Lloyd', 'Jayson', 'Pintac']
print(list(map(even_string, my_string)))

print('\n## FILTER FUNCTION ##\n')


def is_even(num):
    return num % 2 == 0


list_number = [1, 2, 3, 4, 5, 6]

for item in filter(is_even, list_number):
    print(item)

print(list(filter(is_even, list_number)))

print('\n## LAMBDA EXPRESSION ##\n')

sq = lambda x: x ** 8

print(sq(3))

list_numbers = [1, 2, 3, 4, 5, 6, 7, 8]

print(list(filter(lambda x: x % 2 == 0, list_numbers)))

names = ['Job', 'David', 'Abel', 'Jesus']

print(list(map(lambda x: x, names)))
for item in map(lambda x: x, names):
    print(item)
