my_list = "Lloyd Jayson Pintac is my name"
print(my_list.split())
in_list = my_list.split()
a = in_list[::-1]
print(len(in_list))

my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(len(my_numbers))
print(my_numbers[::-1])
print('{b} is reverse of {0}'.format(a, b=in_list))

in_list[4] = 'great'
in_list.append('very')
x = in_list.pop(1)

print(in_list)
print(x)
a_list = ['Vina', 'Kyla', 'Jake', 'Adele', 'Sai', 'Naruto',32]
a_list.pop()
print(a_list)
a_list.sort()
print(a_list)
