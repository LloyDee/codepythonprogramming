class Animal():
    def __init__(self):
        print("ANIMAL CREATED")

    def who_a_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")
myanimal = Animal()

myanimal.eat()
myanimal.who_a_i()


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    def who_a_i(self):
        print("I am a Dog")


    def bark(self):
        print('WOOF!')

mydog = Dog()
mydog.who_a_i()
mydog.bark()