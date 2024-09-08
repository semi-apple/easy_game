# Data Types

## Numeric  Types 
- int: Integer numbers.
- float: Floating-point numbers.
- complex: Complex numbers.

## Sequence Types
- str (string): Ordered collection of characters.
- list: Ordered, mutable collection of items.
- tuple: Ordered, immutable collection of items.

## Boolean Type
- bool: Represents truth values, True or False.

## Control Flow Statements
- if-else Statement: Conditional statements to execute code based on conditions.

## Loops
- for loop: Iterates over a sequence of items.
- while loop: Executes code repeatedly as long as a condition is true.

# Python Data Structures

## Lists (list)
- Ordered, mutable collection of items.
- Accessed by index.
- Example: my_list = [1, 2, 3, 'a', 'b', 'c']

## Tuples (tuple)
- Ordered, immutable collection of items.
- Accessed by index.
- Example: my_tuple = (1, 2, 3, 'a', 'b', 'c')

# How to Install Python On Mac
On terminal
- Install homebrew
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
Remember to change PATH, it will show on terminal once you finish installing brew, otherwise you cannot use brew. 
- Install python: For specific version, just change version number in the end, e.g. python3.9 for version 3.9.
```bash
brew install python3.11
```
- Install git: If you want to copy the repo using git, you also need to install git.
```bash
brew install git
```
- Copy the repo: Create or find a folder which you think is suitable to store code.
```bash
git clone https://github.com/semi-apple/easy_game.git
```