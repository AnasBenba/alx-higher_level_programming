# Python Import and Modules

In Python, modules are separate files that contain definitions and statements that can be used in other programs. You can import a module in your program and use the functions and classes defined in it.

## Importing modules

You can import a module in your program using the `import` keyword followed by the name of the module. For example, to import the `math` module, you would use the following code:

```
import math
```

Once the module is imported, you can use its functions and classes by prefixing them with the module name. For example, to use the `sqrt()` function from the `math` module, you would write:

```
import math

x = math.sqrt(4)
```

You can also import specific functions or classes from a module using the `from` keyword. For example, to import only the `sqrt()` function from the `math` module, you would write:

```
from math import sqrt

x = sqrt(4)
```

## Creating modules

You can also create your own modules in Python. To create a module, simply write the definitions and statements that you want to include in the module in a separate file with a `.py` extension.

For example, suppose you want to create a module that contains a function called `add()` that adds two numbers. You could create a file called `my_module.py` with the following contents:

```
def add(a, b):
    return a + b
```

You can then import this module in another program using the `import` keyword:

```
import my_module

x = my_module.add(2, 3)
```

## Preventing code from being executed when imported

When you import a module in Python, any code that is not inside a function or a class definition is executed immediately. To prevent this code from being executed when the module is imported, you can use the `if __name__ == "__main__":` block.

For example, suppose you have a module called `my_module` with the following contents:

```
def add(a, b):
    return a + b

print("This code will be executed when the module is imported.")

if __name__ == "__main__":
    print("This code will be executed only if the module is run as the main program.")
```

In this example, the `print()` function outside the `if` block will be executed immediately when the module is imported. The `if __name__ == "__main__":` block ensures that the code inside it is executed only if the module is run as the main program, and not when it is imported.

## Conclusion

Importing and using modules is a key feature of Python that allows you to reuse code and organize your programs into separate files. By understanding how to import and create modules in Python, you can write more efficient and modular programs.
