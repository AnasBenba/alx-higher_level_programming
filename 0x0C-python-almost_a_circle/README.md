# Python - Almost a circle

## Import

In Python, the import statement is used to bring modules or specific items from modules into your current script. It allows you to use functionality defined in other modules or packages. Here's an example of importing a module and using its functions:

```
import math

# Using the math module
print(math.sqrt(16))  # Output: 4.0
```

## Exceptions

Exceptions in Python are used to handle errors and exceptional situations that may occur during program execution. They allow you to gracefully handle errors and provide appropriate error messages or perform specific actions. Here's an example of catching an exception:

```
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

## Class

A class is a blueprint for creating objects that encapsulate data and behavior. It defines the attributes and methods that objects of the class will have. Here's an example of defining and using a class:

```
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}.")

# Creating an instance of the class
person = Person("John")
person.greet()  # Output: Hello, my name is John.
```

## Private Attribute

In Python, there is no strict concept of private attributes. However, a convention is followed by prefixing an attribute name with an underscore `(_)` to indicate that it should be treated as private. It is a way to indicate that the attribute is intended for internal use within the class. Here's an example:

```
class MyClass:
    def __init__(self):
        self._private_attribute = 42

    def _private_method(self):
        print("This is a private method.")

my_obj = MyClass()
print(my_obj._private_attribute)  # Output: 42
my_obj._private_method()  # Output: This is a private method.
```

## Getter/Setter

Getter and setter methods are used to access and modify the values of private attributes in a controlled manner. They provide an interface to interact with private attributes while enforcing certain rules or validations if needed. Here's an example of using getter and setter methods:

```
class Circle:
    def __init__(self, radius):
        self._radius = radius

    def get_radius(self):
        return self._radius

    def set_radius(self, radius):
        if radius > 0:
            self._radius = radius
        else:
            raise ValueError("Radius must be a positive number.")

circle = Circle(5)
print(circle.get_radius())  # Output: 5
circle.set_radius(10)
print(circle.get_radius())  # Output: 10
```

## Class Method

A class method is a method that is bound to the class and not the instance of the class. It is defined using the `@classmethod` decorator and takes the class as the first parameter. Class methods can be used to perform operations related to the class itself rather than individual instances. Here's an example:

```
class MyClass:
    @classmethod
    def class_method(cls):
        print("This is a class method.")

MyClass.class_method()  # Output: This is a class method.
```

## Static Method

A static method is a method that belongs to the class and does not operate on any specific instance. It is defined using the `@staticmethod` decorator and does not take the class or instance as a parameter. Static methods are often used for utility functions that don't require access to instance-specific data. Here's an example:

```
class MathUtils:
    @staticmethod
    def add_numbers(a, b):
        return a + b

result = MathUtils.add_numbers(2, 3)
print(result)  # Output: 5
```

## Inheritance

Inheritance is a fundamental concept in object-oriented programming that allows a class to inherit attributes and methods from another class. The inherited class is called the child class or subclass, and the class it inherits from is called the parent class or superclass. Here's an example of inheritance:

```
class Animal:
    def speak(self):
        print("Animal speaks.")

class Dog(Animal):
    def speak(self):
        print("Dog barks.")

animal = Animal()
animal.speak()  # Output: Animal speaks.

dog = Dog()
dog.speak()  # Output: Dog barks.
```

## Unittest

The unittest framework is a built-in testing framework in Python that allows you to write and execute unit tests. It provides a set of tools and assertions to verify that the code behaves as expected. Unit tests help ensure the correctness and robustness of your code. Here's an example of writing a simple unit test using unittest:

```
import unittest

def add_numbers(a, b):
    return a + b

class MyTest(unittest.TestCase):
    def test_add_numbers(self):
        result = add_numbers(2, 3)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
```

## Read/Write File in Python

Reading and writing files in Python is essential for working with data and performing file operations. Python provides built-in functions and methods to read and write files. Here's an example of reading and writing a file:

```
# Read from a file
with open('input.txt', 'r') as file:
    content = file.read()
    print(content)

# Write to a file
with open('output.txt', 'w') as file:
    file.write('Hello, World!')
```

Remember to handle exceptions and close the file properly when working with file operations.
