from random import randint


#
#
# def myfunc(a, b, c=0):
#     # returns 5% of the sum of a and b
#     return sum((a, b, c)) * 0.05
#
#
# print(myfunc(50, 50))
#
#
# def my_function(*args):
#     return sum(args)
#
#
# print(my_function(1, 2, 3, 4, 5))
#
#
# def myfunc(**kwargs):
#     if 'veggie' in kwargs:
#         print('My fruit of choice is {}'.format(kwargs['fruit']))
#     else:
#         print('I did not find any fruit here {}'.format(kwargs['veggie']))
#
#
# myfunc(fruit='Apple', veggie='Lettuce')
#
#
# def myfunc(*args, **kwargs):
#     print('I want {} {}'.format(args[randint(0, len(args) - 1)], kwargs['want']))
#
#
# myfunc(1, 2, 3, 4, 5, want='Bike', need='computer')
#
#
# def myfunc(*args):
#     list_of_even_args = []
#     for number in args:
#         if number % 2 ==0:
#             list_of_even_args.append(number)
#     return list_of_even_args
#
# print(myfunc(5,6,7,8))

def myfuncs(x):
    out = []
    for i in range(len(x)):
        if i % 2 == 0:
            out.append(x[i].upper())
        elif 1 % 2 != 0:
            out.append(x[i].lower())
    print(out)
    print("{} is change to {}".format(x, "".join(out)))


print(myfuncs("leave me alone, I'm busy pretending to work"))

my_name = 'Lloyd'
print(my_name.split())
l = []
for x in my_name:
    l.append(x)
print(''.join(l))
