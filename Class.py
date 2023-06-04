# Python Classes/Objects
# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.
# Create a class named MyClass, with a property named x:

class MyClass:
    x = 5


p1 = MyClass()
print(p1.x)

# The __init__() Function
# Create a class named Person, use the __init__() function to assign values for name and age:


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)

print(p1.name)
print(p1.age)

# The __str__() Function
# The __str__() function controls what should be returned when the class object is represented as a string.
# If the __str__() function is not set, the string representation of the object is returned:


# The string representation of an object WITHOUT the __str__() function:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)

print(p1)

# The string representation of an object WITH the __str__() function:


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"


p1 = Person("John", 36)

print(p1)
