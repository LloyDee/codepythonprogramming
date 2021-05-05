# x = 0
# while x < 5:
#     print("the current value of x is {}.".format(x))
#     x += 2


# pass
# x = [1, 2, 3]
# for item in x:
#     pass

# continue
my_string = 'Sammy'
print('For Continue')
for letter in my_string:
    if letter == 'm':
        continue
    print(letter)

# break
x = 10
print('For Break')
while x >= 0:
    if x == 5:
        break
    print(x)
    x-=1