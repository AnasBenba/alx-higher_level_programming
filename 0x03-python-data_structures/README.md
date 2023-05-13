# Python - Data Structures: Lists, Tuples

Python provides several built-in data structures to hold and manipulate data. Two of the most commonly used data structures in Python are lists and tuples.

## Lists

A list is a collection of values that are ordered and changeable. Lists are created by enclosing a comma-separated sequence of values in square brackets `[]`. For example:

```
my_list = [1, 2, 3, 4, 5]
```

Lists can contain values of different data types:

```
my_list = [1, "two", 3.0, True]
```

To access an element in a list, you can use indexing. The index of the first element in the list is 0. For example, to access the first element of `my_list`, you would use:

```
my_list[0] # returns 1
```

You can also use negative indexing to access elements from the end of the list:

```
my_list[-1] # returns 5
```

Lists are mutable, which means you can change their contents by assigning new values to elements or by adding or removing elements:

```
my_list[2] = 4.0 # changes the third element to 4.0
my_list.append(6) # adds the value 6 to the end of the list
del my_list[0] # removes the first element from the list
```

## Tuples

A tuple is a collection of values that are ordered and immutable. Tuples are created by enclosing a comma-separated sequence of values in parentheses `()`. For example:

```
my_tuple = (1, 2, 3, 4, 5)
```

Like lists, tuples can contain values of different data types:

```
my_tuple = (1, "two", 3.0, True)
```

To access an element in a tuple, you can use indexing just like with lists:

```
my_tuple[0] # returns 1
```

However, because tuples are immutable, you cannot change their contents:

```
my_tuple[2] = 4.0 # raises TypeError
```

You can, however, create a new tuple by concatenating two existing tuples:

```
new_tuple = my_tuple + (6,) # creates a new tuple with the value 6 added to the end
```

## Conclusion

Lists and tuples are two of the most commonly used data structures in Python. They have different properties and are used for different purposes. Lists are mutable, which means you can change their contents, while tuples are immutable. Use lists when you need to modify the contents of a collection, and use tuples when you need to ensure that the contents of a collection cannot be changed
