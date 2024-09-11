# Unit 2 Study Guide: JavaScript Fundamentals

## Table of Contents
- [Document Object Model](#document-object-model)
- [Variables](#variables)
  - [Variables: What are they?](#variables-what-are-they)
  - [Variables: Behind the Scenes](#variables-behind-the-scenes)
  - [Variables: Memory Lifecycle Explained](#variables-memory-explained)
  - [Variables: Mutable versus Immutable](#variables-mutable-versus-immutable)
  - [Variables: Naming Conventions](#variables-naming-conventions)
- [Strings](#strings)
- [Numbers](#- [Booleans](#booleans)

## Document Object Model
### What is it?
The **Document Object Model (DOM)** is an interface that allows JavaScript to interact with or manipulate HTML by retrieving elements and their metadata. Once retrieved, we can affect, change, hide, display, or create new elements using JavaScript. The DOM can be represented by a tree data structure.

#### Key Points
- **DOM Structure**: A bundle of nodes that together content of a web page.
- **Accessing DOM**: We can reference or access the DOM by using the `document` keyword in JavaScript.
- **Window Object**: The highest level object in the browser’s environment, accessible by using the `window` keyword in JavaScript.
- **Nodes and Metadata**: Elements and their metadata are bundled into nodes, including the element’s attributes and values.

## Variables
### Variables: What are they?
A **variable** is a reusable label a developer creates to store data. The stored values can be changed if declared using the keywords `let` or `var`. If declared using `const`, the variable’s value cannot be changed.

#### Example
```javascript
let userAge = 23;
```

I'd be happy to help you convert this content into a styled Markdown format. I'll structure it with headers, code blocks, and some emphasis to make it more readable. Here's the Markdown version:
markdownCopy# JavaScript Basics: Variables and Data Types

## Variables

### Components of a Variable Declaration

- **Variable Name**: Also called the identifier, defined by the developer.
- **Variable Value**: The data assigned to the variable (e.g., a number).
- **Statement Terminator**: The semicolon (;) at the end of the statement.
- **Assignment Operator**: The equals sign (=) assigns the value to the variable.
- **Variable Declaration**: Keywords in JavaScript (let, var, const).

### Behind the Scenes

When we declare a variable, JavaScript allocates memory to store that variable. You don't necessarily have to assign a value right away.

```javascript
let name;  // Memory is allocated, but the value is `undefined`
name = "Alice";  // Now the value is the string "Alice"
```

Variables: Memory Lifecycle Explained

Variables go through a memory lifecycle which includes three stages: 

Memory Allocation

Memory Usage

Memory Release

Declaring the variable allocates the memory.

Using the variable uses or accesses the memory.

Unlike other languages such as C or C++, JavaScript periodically releases unused memory blocks for you in a process known as Garbage Collection.

Variables: Mutable versus Immutable

By choosing which keyword we use to declare our variable, we signal to JavaScript whether or not the value of our variable is allowed to change. We refer to this as being mutable or immutable.

Mutable: Variables declared with `let` or `var` can be reassigned.
let name = "Alice";  
name = "Greg"; // Now the memory holds the string "Greg"

Immutable: Variables declared with `const` cannot be reassigned.
const name = "Alice";  
name = "Greg"; // Expected outcome: “Error: Assignment to constant variable”


Variables: Naming Conventions

JavaScript has certain rules we must abide when naming variables. When developers follow rules dictated either by the language or by best-practice expectations, we call those rules conventions.

JavaScript also follows the convention of    camel case capitalization. The first word is lowercase and all subsequent words are capitalized.

Variables: Naming Conventions Pt. 2

When naming a variable, always think about clear, understandable semantic naming and providing content to other developers.

Don’t: Avoid giving variables shorthand or vague names
let myVar = “4457”;  // Unclear. What is this string meant to be used for?

Do: Provide clear context without making the variable too lengthy.
let streetAddressNumber = "4457";  
// A developer will now understand the intent here.


Strings: Data Type for Text

A string is a data type used to represent text. Strings are sequences of characters and can include letters, numeric characters, symbols, spaces, and even empty characters. Strings are denoted by the use of single quotes, double quotes, or backticks (in a special format).

let name = “4457”;  // Double quotes.

let name = ‘4457’;  // Single quotes.

let name = `4457`;  // Backticks (Called a template literal).

// Strings can be declared by using `let`, `var`, or `const`. These are just examples.


Numbers: Data Type for Calculation

A number is a data type used to represent either an integer or a floating point (decimal) value. Unlike some other programming languages, JavaScript does not have separate data types for integers and floating-point numbers.

let age = 4457;  // Integer

let price = 19.99;  // Floating-point number

let negative = -10;  // Negative number

let largeNum = 1e6;  // Exponential notation (1 million)

let quantity = “4457”;  // Beware! This looks like a number but is a string.

Numbers: Special Values

JavaScript, and most other programming languages, also have special number values: positive infinity, negative infinity, and NaN.

console.log(1 / 0); // Output: Infinity (Positive infinity, increasing above zero)

console.log(-1 / 0); // Output: -Infinity (Negative infinity, decreasing below zero)

console.log(“hello” * 3); // Output: NaN (Evaluates to “Not a Number”)

Booleans: Data Type for True and False

All modern programming languages support a dedicated boolean data type, or the data type represented by the keywords true or false. Boolean algebra forms the basis of binary, the computation language executing at the hardware level of all machines. Binary is a language that consists of only the characters 0 and 1. Similarly, in some older programming languages, boolean outcomes are represented by 0 (false) and 1 (true). However, modern languages have transitioned into human-readable boolean values of true and false. 

let canVote = true;  // Explicit boolean value is directly assigned true/false.

let isLarger = (5 > 3);  // Implicit or Evaluated boolean values are the results derived from expressions.

// It is a common convention to name functions and variables that expect a boolean result with a “question-like” name to signal context to other developers

Link to drive presentation - Private copy - https://docs.google.com/presentation/d/19CqMSFuOUgs0z0rd_0D-XCGQ_NZp0KV4qdTyIMf1EjY/edit?usp=sharing

