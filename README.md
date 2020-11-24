# The Complete Python Course: Beginner to Advanced
This document is a consolidation of Emily Pfeffer’s course notes from [The Complete Python Course: Beginner to Advanced](https://www.skillshare.com/classes/The-Complete-Python-Course-Beginner-to-Advanced/81017023?lessonsTab=on) offered on Skillshare.

## Introduction to Python
* Python is a widely used high-level, general-purpose, interpreted, dynamic programming language
* Built around two main focal points
  * Code readability
  * Simplicity
* Two current versions
  1. Python2 (currently at 2.7.11)
  2. Python3 (currently at 3.5.1)
* When you look at python, it’s all indentation-based, so you don’t need to wrap blocks of code in curly braces (i.e., { } )

## Installation
### Mac/Linux
1. Open Terminal
2. Install Homebrew
  * `$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"`
3. Install Python
  * `$ brew install python` or `$ sudo yum install python3`
### Windows Installation
1. Go to https://python.org/downloads/
2. Download for Windows (Python 3.x)
3. Launch the installer program
4. Select “Add Python 3.6 to PATH”
5. Open Control Panel
6. Go to System > Advanced System Settings > Environment Variables
7. Select the PATH variable
  * Every time that you enter a python script in a terminal window, your computer will check that the python executable file exists in one of the locations listed in the PATH
8. Open command prompt
  * `> python -m pip install requests`
    * Now you’ll have access to the requests class

## Interpreted vs Compiled Programming Languages
* With a compiled programming language (e.g., C++), you write your code and save it into a file. So, you write a function and script. Once you save your file, you need to compile it into a language that the computer can read (i.e., binary code).
* With python, which is an interpreted programming language, when you write a script, you can instantaneously run that script without having to compile it. When you run python scripts, you run the python program, which interprets the code and automatically converts it into binary code using just-in-time compilation.
* Hands-on Example in Terminal
  * `$ python3`
  * `>>> print(“Hello World”)`
    * Returns “Hello World”
  * `>>> 4 + 6`
    * Interprets it as a summation and returns “10”

## Creating and Running Our First Python Script
1. Open Terminal
2. Change directory to a place where you'd like your python to live (e.g., `$ cd learn-python`)
3. `% nano test.py` to create a python script
4. ctrl+O to save, ENTER, ctrl+X to exit
5. Run script with `% python3 test.py` in your terminal

## Setting Up Our Integrated Development Environment (IDE)
* PyCharm (Community) from JetBrains is free; alternatively, you can use other IDEs
  * Requires Java
* Create a new Pure Python project with version 3.5.1

## Data Types
### Numbers
* Integers and Floating Points
  * `>>> 5+6`
    * Returns '11'
  * `>>> "5" + "6"`
    * Returns '56'
  * `>>> 5.5 + 5.5`
    * Returns '11.0' as a float
  * `>>> int("5") + int("7")`
    * Will convert both strings to integers and then do the math
    * Returns '12'

### Strings
* Any text that you want to be treated as text in the program
* `>>> 'Hello String'` or `>>> "Hello String"`; both double and single quotes work
  * `>>> 'Don't do that` will result in an error, since it doesn't know when to start and end the string due to the apostrophe.
    * Wrap the string in double quotations, instead of single
    * `>>> "Don't do that"` would work
    * `>>> print('She said \"Don\'t do that\"')` will return...
      * She said "Don't do that"
* Concatenate Strings
  * Use a plus symbol between strings
  * `>>> "H" + "e" + "ll" + "o"` will print 'Hello'
  * `>>> "This costs " + 6 + " bucks"` will error out, since it doesn't know what to do with the integer in the middle and is trying to perform some mathematical equation. Instead...
    * `>>> "This costs " + str(6 + 5) + " bucks"` will...
      * perform 6+5 as integers and then convert it to a string
      * concatenate all the three strings
      * return 'This costs 11 bucks'
* Split strings apart
  * .split() procedure, based on parameter
  * `>>> "Hello:Nick".split(":")` returns "['Hello', 'Nick']"
  * You can also select which part of the split string to keep (remember, indexes start at 0)
    * `>>> "My name is " + "Hello:Emily:World".split(":")[1]` returns 'My name is Emily'

### Booleans
* True and False operators
* Type 'True' and 'False' __without__ quotations; otherwise they'll be considered string values
  * `>>> True` returns a boolean True value
  * `>>> 'True'` returns a string 'True' value
* When comparing two values, use double equal signs
  * `>>> 5 = 4` will return an error
  * `>>> 5 == 4` will return a False boolean value
  * `>>> 5 is 5` will return a True boolean value
  * `>>> 5 is not 5` will return a False boolean value
* When comparing two values, it's checking both:
  * data type (i.e., are both strings or number values)
  * data value (i.e., index values of strings or numbers)
* Literal equations
  * `>>> "True" is str(True)` will return an error
  * `>>> "True" == str(True)` will return a boolean True value

### Arrays
* To define an array, open and close square brackets []
* You can also specify which index of the array you want returned by including a number in square brackets after the array list
* Suppose you're making a list of things you like...
  * `>>> ["Movies", "Kayaking", "Python"]` will create an array/list and return ['Movies', 'Kayaking', 'Python']
  * `>>> ["Movies", "Kayaking", "Python"][0]` will return 'Movies'
  * `>>> print("I like " + ["Movies", "Kayaking", "Python"][1])` will return 'I like Kayaking'
* Suppose one of the index values is a number...
  * `>>> print("I like " + ["Movies", 16, "Python"][1])` will return an error
    * Surrounding the number with quotations will make the program consider it as a string and accept it
    * `>>> print("I like " + ["Movies", "16", "Python"][1])` will return 'I like 16'

### Dictionaries
* To create a dictionary, use opened/closed curly brackets { }
* Suppose you want to create a person...
  * `>>> {"name": "Emily", "age": 29, "hobby": "code"}` returns {'name': 'Emily', 'age': 29, 'hobby': 'code'}
  * `>>> {'name': 'Emily', 'age': 29, 'hobby': 'code'}[0]` will return an error
    * Unlike arrays, using square brackets to identify a numbered index will return an error, because it's not a list
  * `>>> {'name': 'Emily', 'age': 29, 'hobby': 'code'}['name']` will return the value for that defined field - 'Emily'
  * `>>> {'name': 'Emily', 'age': 29, 'hobby': 'code'}['age']` will return 29
  * `>>> {'name': 'Emily', 'age': 29, 'hobby': 'code'}['hobby']` will return 'code'

## Variables
* The value of variables are not constant, which means they're also not reusable
* Variables allow us to have dynamic logic
* Some programming languages are typed, which means that you need to define the type of variable. Python does not require you to explicitly define the value type.
* `>>> greeting = "Hello World"` sets greeting as a string variable; this does not print anything
* `>>> print(greeting)` returns Hello World
* `>>> greeting = greeting.split(" ")[0]` resets the variable as the first word of the previously set variable
* `>>> print(greeting)` now prints Hello
* Concatenation with Variables
  * `>>> print(greeting + " Emily")` prints Hello Emily
  * `>>> greeting = greeting + " Emily"` resets the variable
  * `>>> number = 1`
  * `>>> secondnumber = 2`
  * `>>> print(number * secondnumber + secondnumber * number)` prints 4

## Built-in Functions
* `print()` prints text
* `str()` converts to string
* `int()` converts to integers
* `float()` converts strings to floats
  * `>>> float("5.6")` prints 5.6 as a float value
* `bool()` converts a string to a boolean
  * `>>> bool("True")` prints True
* `len()` tells us the number of characters in a string or array (i.e., it's length)
  * `>>> len("Hello")` prints 5
  * `>>> len([1, 2, 6, 3, 41])` prints 5, because there are five items in the array
  * `>>> len(["Hello", "Emily"])` prints 2, because there are two items in the array
* `sorted()`
  * `>>> [16, 3, 8, 6, 9, 133, 435, 21, 823, 45]` creates an array
  * `>>> sorted([16, 3, 8, 6, 9, 133, 435, 21, 823, 45])` prints the array in numerically ascending order [3, 6, 8, 9, 16, 21, 45, 133, 435, 823]
  * `>>> sorted(["B", "R", "a", "N"])` sorts it alphabetically and returns ['B', 'N', 'R', 'a']
    * Notice that the lowercase 'a' is at the end; capitals are parsed first
  * `>>> sorted(["B", "R", "a", "N", "d", "f", "100", "99", "G"])` will return ['100', '99', 'B', 'G', 'N', 'R', 'a', 'd', 'f']
    * Parsing order: spaces, numbers, capitals, lowercase
    * Notice that since the numbers must be included as strings, they are ordered as strings. 100 comes before 99, even though they would be numerically descending
      * If I put a space in front of the ' 99', then... [' 99', '100', 'B', 'G', 'N', 'R', 'a', 'd', 'f']

## Functions
* Pep is Python's style guides
* Drop down two lines before starting your code
* Snake case for function names (e.g., my_function) - separate words with underscores
* Python recognizes the end of a function based on indentation, instead of a semicolon like other programming languages.

### Arguments
* Go inside brackets at the end of a function name
* Use variables
* You can set defaults in your parameters
  * `def print_something(name = "Someone", age = "Unknown")`
  * When calling a function with arguments, you can specify the values
    * `print_something("Emily")` sets name = "Emily" and uses the default age value
    * `print_something(29)` sets name = 29 and uses the default age
    * `print_something(age = 29, name = "Emily")` sets name = "Emily" and age = 29

### Infinite Number of Arguments
* `def print_people(*people)`
  * asterisks denotes that there will be an array

## Conditional Statements
* IF, ELIF, ELSE Statements
  ```python
  check = "Hamburger"

  if check == False:
      print("If is false")
  elif check == "Hamburger":
      print("Yummmm, hamburgers")
  elif check == "Yo":
      print("Hey")
  else:
      print("It is actually equal to True")
  ```
