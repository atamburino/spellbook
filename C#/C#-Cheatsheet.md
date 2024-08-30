# Getting Started

```csharp
class Hello {
  // main method
  static void Main(string[] args) {
    // Output: Hello, world!
    Console.WriteLine("Hello, world!");
  }
}
```
- Compiling and running (make sure you are in the project directory):
  ```bash
  $ dotnet run
  Hello, world!
  ```

# Variables

```csharp
int intNum = 9;
long longNum = 9999999;
float floatNum = 9.99F;
double doubleNum = 99.999;
decimal decimalNum = 99.9999M;
char letter = 'D';
bool @bool = true;
string site = "quickref.me";

var num = 999;
var str = "999";
var bo = false;
```

# Primitive Data Types

| Data Type | Size         | Range                  |
|-----------|--------------|------------------------|
| int       | 4 bytes      | -2^31 to 2^31-1        |
| long      | 8 bytes      | -2^63 to 2^63-1        |
| float     | 4 bytes      | 6 to 7 decimal digits  |
| double    | 8 bytes      | 15 decimal digits      |
| decimal   | 16 bytes     | 28 to 29 decimal digits|
| char      | 2 bytes      | 0 to 65535             |
| bool      | 1 bit        | true / false           |
| string    | 2 bytes per char | N/A              |

# Comments

```csharp
// Single-line comment

/* Multi-line 
   comment */

// TODO: Adds comment to a task list in Visual Studio

/// Single-line comment used for documentation

/** Multi-line comment 
    used for documentation **/
```

# Strings

```csharp
string first = "John";
string last = "Doe";

// string concatenation
string name = first + " " + last;
Console.WriteLine(name); // => John Doe
```

# User Input

```csharp
Console.WriteLine("Enter number:");
if(int.TryParse(Console.ReadLine(), out int input)) {
  // Input validated
  Console.WriteLine($"You entered {input}");
}
```

# Conditionals

```csharp
int j = 10;

if (j == 10) {
  Console.WriteLine("I get printed");
} else if (j > 10) {
  Console.WriteLine("I don't");
} else {
  Console.WriteLine("I also don't");
}
```

# Arrays

```csharp
char[] chars = new char[10];
chars[0] = 'a';
chars[1] = 'b';

string[] letters = {"A", "B", "C"};
int[] mylist = {100, 200};
bool[] answers = {true, false};
```

# Loops

```csharp
int[] numbers = {1, 2, 3, 4, 5};

for(int i = 0; i < numbers.Length; i++) {
  Console.WriteLine(numbers[i]);
}

foreach(int num in numbers) {
  Console.WriteLine(num);
}
```

# C# Strings

### String Concatenation

```csharp
string first = "John";
string last = "Doe";

string name = first + " " + last;
Console.WriteLine(name); // => John Doe
```

### String Interpolation

```csharp
string name = $"{first} {last}";
Console.WriteLine(name); // => John Doe
```

### Verbatim strings

```csharp
string longString = @"I can type any characters in here !#@$%^&*()__+ '' \n \t except double quotes and I will be taken literally. I even work with multiple lines.";
```

### String Members

```csharp
// Using property of System.String
string lengthOfString = "How long?";
Console.WriteLine(lengthOfString.Length);           // => 9

// Using methods of System.String
Console.WriteLine(lengthOfString.Contains("How")); // => true
```

### Member Example

| Member      | Description |
|-------------|-------------|
| Length      | A property that returns the length of the string. |
| Compare()   | A static method that compares two strings. |
| Contains()  | Determines if the string contains a specific substring. |
| Equals()    | Determines if the two strings have the same character data. |
| Format()    | Formats a string via the {0} notation and by using other primitives. |
| Trim()      | Removes all instances of specific characters from trailing and leading characters. Defaults to removing leading and trailing spaces. |
| Split()     | Removes the provided character and creates an array out of the remaining characters on either side. |

# Misc

## General .NET Terms

| Term                        | Definition |
|-----------------------------|------------|
| Runtime                     | A collection of services that are required to execute a given compiled unit of code. |
| Common Language Runtime (CLR)| Primarily locates, loads, and managed .NET objects. The CLR also handles memory management, application hosting, coordination of threads, performing security checks, and other low-level details. |
| Managed code                | Code that compiles and runs on .NET runtime. C#/F#/VB are examples. |
| Unmanaged code              | Code that compiles straight to machine code and cannot be directly hosted by the .NET runtime. Contains no free memory management, garbage collection, etc. DLLs created from C/C++ are examples. |