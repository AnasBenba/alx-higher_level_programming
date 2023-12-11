## JavaScript - Warm up
# Why JavaScript Programming is Amazing
JavaScript is an amazing programming language known for its versatility and widespread use. Its ability to run on both the client and server sides, along with its support for asynchronous programming, makes it a powerful language for building dynamic and interactive web applications.

# How to Run a JavaScript Script
To run a JavaScript script, you can use the following command in a terminal or command prompt:

```
node script.js
```

Replace `script.js` with the filename of your JavaScript script. Make sure you have Node.js installed on your machine.

# How to Create Variables and Constants
In JavaScript, you can create variables using `var`, `const`, or `let`. Constants are created using `const`. Here's an example:

```
// Variable
var myVar = 42;

// Constant
const myConst = "Hello, World!";
```

# Differences Between var, const, and let
- `var`: Function-scoped, can be redeclared and reassigned.
- `const`: Block-scoped, cannot be reassigned, must be initialized.
- `let`: Block-scoped, can be reassigned but not redeclared.

```
var x = 5;
const y = 10;
let z = 15;
```

# Data Types in JavaScript
JavaScript supports various data types, including:
- Primitive types: `string`, `number`, `boolean`, `null`, `undefined`, `symbol`.
- Complex types: `object`, `function`.

```
let text = "Hello";
let number = 42;
let isTrue = true;
let myObject = { key: "value" };
```

# Using if, if ... else Statements
Use `if` and `if ... else` statements for conditional logic:

```
let x = 10;

if (x > 5) {
    console.log("x is greater than 5");
} else {
    console.log("x is 5 or less");
}
```

# How to Use Comments
Comments in JavaScript are used to provide explanations within the code. Single-line comments start with `//`, and multi-line comments use `/* ... */`.

```
// This is a single-line comment

/*
  This is a
  multi-line comment
*/
```

# Assigning Values to Variables
Assign values to variables using the assignment operator `=`:

```
let myVariable;
myVariable = 42;
```

Variables can also be declared and assigned in a single line:

```
let myNumber = 7;
```

# Using While and For Loops
Use `while` and `for` loops for repetitive tasks:

```
// While Loop
let i = 0;
while (i < 5) {
    console.log(i);
    i++;
}

// For Loop
for (let j = 0; j < 5; j++) {
    console.log(j);
}
```

# Using Break and Continue Statements
`break` exits a loop, and `continue` skips the rest of the code for the current iteration:

```
for (let i = 0; i < 10; i++) {
    if (i === 5) {
        break; // Exit the loop
    }
    console.log(i);
}

for (let j = 0; j < 10; j++) {
    if (j === 5) {
        continue; // Skip the rest of the code for j equals 5
    }
    console.log(j);
}
```

# What is a Function and How to Use Functions
A function in JavaScript is a reusable block of code. Here's an example:

```
function greet(name) {
    console.log("Hello, " + name + "!");
}

greet("Alice"); // Output: Hello, Alice!
```

# Function without a Return Statement
A function without a `return` statement implicitly returns `undefined`:

```
function doSomething() {
    // Code without return statement
}

let result = doSomething();
console.log(result); // Output: undefined
```

# Scope of Variables
JavaScript has function-level scope for variables declared with `var` and block-level scope for variables declared with `const` and `let`:

```
var globalVar = "I am global";

function exampleFunction() {
    console.log(globalVar); // Accessible inside the function
}

exampleFunction();
console.log(globalVar); // Accessible outside the function
```

# Arithmetic Operators in JavaScript
JavaScript supports basic arithmetic operators:

```
let sum = 5 + 3; // Addition
let difference = 10 - 4; // Subtraction
let product = 3 * 7; // Multiplication
let quotient = 15 / 3; // Division
let remainder = 10 % 3; // Modulus
```

- Increment ('++')
- Decrement ('--')

# Manipulating Dictionaries
In JavaScript, you can use objects to create dictionary-like structures:

```
let myDictionary = {
    key1: 'value1',
    key2: 'value2',
    key3: 'value3'
};

// Adding a new key-value pair
myDictionary.newKey = 'new value';

// Removing a key-value pair
delete my
```
