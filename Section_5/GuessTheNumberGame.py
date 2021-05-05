from random import randint, shuffle
from datetime import datetime

#
# random_number = randint(1, 5)
# print(random_number)
# prompt = input("Please select a number from 1 to 10\t")
# print(type(prompt))
#
# if int(prompt) == random_number:
#     print(type(random_number))
#     print("Correct")
# else:
#     print("Wrong! The random number is {}".format(random_number))

# my_string = 'Hello World'
# ds = [x == 'e'for x in my_string]
# print(ds)
# for x in my_string:
#     print(x)

st = 'Print only the words that start with s in this sentence'
s = [x for x in st.split() if x[0] == 's']
print(s)
number = [x for x in range(1, 61, 2)]
time_now = datetime.today().second
if time_now in number:
    print('{} is odd number'.format(time_now))
else:
    print('{} is even number'.format(time_now))