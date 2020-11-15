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
