# Python - Everything is an Object

## Introduction
Python is a high-level, interpreted programming language known for its simplicity, readability, and versatility. One of the fundamental concepts in Python is "Everything is an Object". This concept signifies that every entity in Python, including numbers, strings, functions, and modules, is represented and treated as an object.

## Objects in Python
In Python, an object is a runtime instance of a class. It consists of data (attributes) and behavior (methods) related to that particular object. Every object has a type, which is defined by its class. For instance, an integer object belongs to the `int` class, a string object belongs to the `str` class, and so on.

## Mutable and Immutable Objects
Objects in Python can be categorized as either mutable or immutable.

- **Mutable Objects**: Mutable objects can be modified after they are created. Changes made to a mutable object do not create a new object; rather, they modify the existing object in-place. Examples of mutable objects in Python include lists, dictionaries, and sets.

- **Immutable Objects**: Immutable objects, on the other hand, cannot be changed once they are created. If you want to modify an immutable object, such as a string or a tuple, you need to create a new object with the desired changes. Immutable objects ensure data integrity and can be safely shared among different parts of a program.

## Passing Variables to Functions
When passing variables to functions in Python, the "pass-by-object-reference" mechanism is used. It means that the reference to the object is passed to the function, not the actual variable itself. If the object is mutable, any modifications made within the function will be reflected outside the function. If the object is immutable, the function can't modify the object itself, but it can assign a new value to the parameter variable.

## Understanding Objects in Python
Understanding that "Everything is an Object" in Python helps in leveraging the language's features effectively. It allows you to manipulate and interact with different objects in a consistent manner, making it easier to write modular, reusable, and maintainable code.

This README provides a brief overview of the concept of "Everything is an Object" in Python. For more in-depth understanding and practical examples, refer to the official Python documentation or explore additional resources available online.

