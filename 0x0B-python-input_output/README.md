# Python - Input/Output

## Opening a File

To open a file in Python, you can use the built-in `open()` function. Here's an example:

```
file = open("example.txt", "r")
```
In this example, we open the file "example.txt" in read mode (`"r"`). The file object is assigned to the variable `file`.

## Writing Text in a File

To write text to a file, you can use the `write()` method of a file object. Here's an example:

```
file = open("example.txt", "w")
file.write("Hello, world!")
```

In this example, we open the file "example.txt" in write mode (`"w"`), and then use the `write()` method to write the text "Hello, world!" to the file.

## Reading the Full Content of a File

To read the full content of a file, you can use the `read()` method of a file object. Here's an example:

```
file = open("example.txt", "r")
content = file.read()
print(content)
```

In this example, we open the file "example.txt" in read mode and then use the `read()` method to read the entire content of the file. The content is stored in the `content` variable and printed to the console.

## Reading a File Line by Line

To read a file line by line, you can use a loop and the `readline()` method of a file object. Here's an example:

```
file = open("example.txt", "r")
for line in file:
    print(line)
```

In this example, we open the file "example.txt" in read mode and use a `for` loop to iterate over each line in the file. Each line is printed to the console.

## Moving the Cursor in a File

To move the cursor in a file, you can use the `seek()` method of a file object. Here's an example:

```
file = open("example.txt", "r")
file.seek(10)
content = file.read()
print(content)
```

In this example, we open the file "example.txt" in read mode and use the `seek()` method to move the cursor to the 10th byte position in the file. The content from that position onwards is then read and printed to the console.

## Working with JSON

JSON (JavaScript Object Notation) is a popular data format for storing and exchanging structured data. Python provides the `json` module for encoding and decoding JSON data.

## Encoding (Serialization)

To convert a Python object into a JSON string, you can use the `json.dumps()` function. Here's an example:

```
import json

data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

json_data = json.dumps(data)
print(json_data)
```

## Decoding (Deserialization)

To convert a JSON string back into a Python object, you can use the `json.loads()` function. Here's an example:

```
import json

json_data = '{"name": "John Doe", "age": 30, "city": "New York"}'

data = json.loads(json_data)
print(data)
```

## Reading from a JSON file

To read JSON data from a file and parse it into a Python object, you can use the `json.load()` function. Here's an example:

```
import json

with open("data.json", "r") as file:
    data = json.load(file)
    print(data)
```

## Writing to a JSON file

To write a Python object as JSON to a file, you can use the `json.dump()` function. Here's an example:

```
import json

data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

with open("data.json", "w") as file:
    json.dump(data, file)
```

These examples provide a basic understanding of working with files and JSON in Python. You can further explore the Python documentation for more details and advanced usage of these concepts.
