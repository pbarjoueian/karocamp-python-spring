from abc import ABC, abstractmethod


class Person(ABC):
    @abstractmethod
    def signup(self, email, password):
        pass


class Student(Person):
    def __init__(self, first_name, last_name, age):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age

    def print_info(self):
        print(f"{self.__first_name} {self.__last_name} is {self.__age} years old.")

    def signup(self, email, password):
        print(
            f"Student {self.__first_name} {self.__last_name} signed up with email: {email} and password: {password}"
        )

    @property
    def first_name(self):
        print("getter of first_name called")
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        print("setter of x called")
        self.__first_name = value.strip()


stu = Student("Peyman", "Barjoueian", 34)
print(stu.first_name)
stu.first_name = "       Elham     "
print(stu.first_name)
