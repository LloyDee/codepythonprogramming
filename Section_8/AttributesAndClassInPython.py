class Dog:
    age = 2

    def __init__(self, color, trick, name):
        self.color = color
        self.trick = trick
        self.name = name

    def bark(self, attitude):
        print("WOOF my name is {} and I {}. I am {}".format(self.name, self.trick, attitude))


my_dog = Dog(color="Orange", trick="can eat a lot", name="Panther")
my_dog.bark("Friendly")
print(my_dog.name)


class Circle():
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def get_circumference(self):
        return self.radius * self.pi * 2


my_circle = Circle(radius=5)
print(my_circle.get_circumference())


class Rectangle():

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


rectangle = Rectangle(length= 5, width=9)

print(rectangle.area())
