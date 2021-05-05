# database = {'Edith': {'Age': 30, 'Gender': 'Female', 'Last Name': 'Serna', 'Favorite Cat': 'Ginger'},
#             'Lloyd': {'Age': 29, 'Gender': 'Male', 'Last Name': 'Pintac', 'Favorite Cat': 'Tiger'}}
#
# print(database['Edith']['Gender'])
#
# database['Edith']['Gender'] = "Babae"
#
# print(database['Edith']['Gender'])
# print(database.keys())
#
# print("Lloyd's age is {}".format(database['Lloyd']['Age']))
#
# for x in database:
#     print(x)
with open('C:\\Users\\loyd_\\Desktop\\foobar.txt', 'r') as file:
    x = file.read()
new_x = x.split()
for m in new_x:
    if m == 'bar':
        print(m)
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Odd numbers are:")
sum = 0
for x in my_list:
    if x % 2 != 0:
        print(x)
        sum = sum + x
print('Sum is {}'.format(sum))

print("Even numbers are;")
for y in my_list:
    if y % 2 == 0:
        print(y)
