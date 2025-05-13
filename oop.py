class Dog:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def bark(self):
        print(self.name + ": " + "Woofs!")


# dog_1 = Dog(name="Jessie", age=4, color="Black")
# dog_1.bark()


class GermanDog(Dog):

    def search(self):
        print(self.name + ": " + "I'm searching for humans")

    def eat(self, food):
        print(self.name + ": " + "I'm eating " + food)
        self.bark()

    def bark(self):
        print(self.name + ": " + "Woof woof!")


gdog = GermanDog(name="Joe", age=4, color="Black")
# gdog.bark()
# gdog.search()
gdog.eat("Meat")
