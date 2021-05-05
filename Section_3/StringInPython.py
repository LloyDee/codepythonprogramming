# String is Immutability
#############################################
# Concatenation
first_name = "Lloyd "
last_name = "Lintac"

print(first_name + "P" + last_name[1:])

print("My first name is {1} and my last name is {0}".format(last_name,first_name))
print(f'My first name is {first_name} and my last name is {last_name}')

print(first_name * 5)

# String methods
x = 'Hello World'
print(x.upper())
print(x.lower())
d = x[::-1]
print(x.split('o'))
print(d.split())

# String formatting for Printing
# .format() method
insert = "Kumusta"
print('This is a string {}'.format(insert))
print("The {0} {1} {1}".format('quick', 'brown', "fox"))
print('The {0} {q} {b}'.format(insert, b='brown', q='quick'))

# Float formatting

result = 100 / 777
print("The result was {b:1.3f} and {c:1.2f}".format(b= result,c= 100 / 777))

