# Python Basics

# Conditionals Cheat Sheet

Conditionals in Python allow you to make decisions and execute different blocks of code based on certain conditions. Python provides several conditional statements and operators that enable you to control the flow of your program.

## Comparison Operators

Comparison operators are used to compare values and evaluate conditions. They return a Boolean value (`True` or `False`) based on the comparison result.

- `==`: Equal to
- `!=`: Not equal to
- `<`: Less than
- `>`: Greater than
- `<=`: Less than or equal to
- `>=`: Greater than or equal to

## Logical Operators

Logical operators are used to combine multiple conditions and perform logical operations. They return a Boolean value based on the combined conditions.

- `and`: Returns `True` if both conditions are `True`
- `or`: Returns `True` if at least one condition is `True`
- `not`: Returns the opposite Boolean value (negates the condition)

## If Statement

The `if` statement allows you to execute a block of code if a condition is `True`.

```python
if condition:
    # Code to execute if condition is True
```

## If-Else Statement

The `if-else` statement allows you to execute one block of code if a condition is `True`, and another block of code if the condition is `False`.

```python
if condition:
    # Code to execute if condition is True
else:
    # Code to execute if condition is False
```

## If-Elif-Else Statement

The `if-elif-else` statement allows you to test multiple conditions and execute different blocks of code based on those conditions.

```python
if condition1:
    # Code to execute if condition1 is True
elif condition2:
    # Code to execute if condition1 is False and condition2 is True
else:
    # Code to execute if both condition1 and condition2 are False
```

## Nested If Statements

You can nest if statements within other if statements to create more complex decision-making logic.

```python
if condition1:
    # Code to execute if condition1 is True
    if condition2:
        # Code to execute if both condition1 and condition2 are True
    else:
        # Code to execute if condition1 is True and condition2 is False
else:
    # Code to execute if condition1 is False
```

## Truth Value Testing

In Python, certain values are considered "falsey" when used in a boolean context. These values include `False`, `None`, `0`, empty sequences (e.g., empty strings, lists, tuples), and empty dictionaries. All other values are considered "truthy".

## Short-Circuit Evaluation

Logical operators (`and` and `or`) use short-circuit evaluation. In an `and` operation, if the first operand is `False`, the second operand is not evaluated. In an `or` operation, if the first operand is `True`, the second operand is not evaluated.

```python
if condition1 and condition2:
    # Code to execute if both condition1 and condition2 are True

if condition1 or condition2:
    # Code to execute if either condition1 or condition2 is True
```

## Conditional Expressions (Ternary Operator)

Conditional expressions, also known as the ternary operator, provide a concise way to write simple if-else statements in a single line.

```python
value_if_true if condition else value_if_false
```


# Python Lists Cheatsheet

## Initialization and Declaration

```python
my_list = []                    # Empty list
my_list = [1, 2, 3]              # List with initial values
my_list = list(range(1, 10))     # List generated using range
```

## Accessing Elements

```python
element = my_list[index]         # Access element at specific index
last_element = my_list[-1]       # Access last element
sliced_list = my_list[start:end] # Get a sublist using slicing
```

## Modifying Elements

```python
my_list[index] = new_value       # Modify element at specific index
my_list.append(element)          # Add element at the end of the list
my_list.extend(another_list)     # Extend the list with another list
```

## List Operations

```python
length = len(my_list)            # Get the length of the list
count = my_list.count(element)   # Count occurrences of an element
index = my_list.index(element)   # Get the index of the first occurrence
```

## List Manipulation

```python
my_list.reverse()                # Reverse the order of elements
my_list.sort()                   # Sort the list in ascending order
my_list.sort(reverse=True)       # Sort the list in descending order
my_list.remove(element)          # Remove the first occurrence of an element
my_list.pop(index)               # Remove and return element at specific index
my_list.clear()                  # Clear all elements in the list
```

## List Comprehension

```python
new_list = [expression for item in my_list if condition]  # Create a new list based on the existing list
```

## List Functions

```python
sum_of_elements = sum(my_list)                 # Calculate the sum of elements
maximum_element = max(my_list)                 # Find the maximum element
minimum_element = min(my_list)                 # Find the minimum element
sorted_list = sorted(my_list)                  # Return a new sorted list
reversed_list = reversed(my_list)              # Return a new reversed list
zipped_list = zip(my_list1, my_list2)          # Combine two lists into a list of tuples
```

## List Membership and Existence

```python
element in my_list               # Check if an element is in the list
element not in my_list           # Check if an element is not in the list
my_list == another_list          # Check if two lists are equal
my_list is another_list          # Check if two lists are the same object
```

## List Copying

```python
new_list = my_list.copy()        # Shallow copy of the list
new_list = my_list[:]            # Shallow copy of the list
import copy
new_list = copy.deepcopy(my_list) # Deep copy of the list
```


# Python Functions Cheatsheet

## Function Declaration

```python
def function_name(parameters):
    """Function docstring"""
    # Function body
    return result
```

## Function Calling

```python
function_name(arguments)          # Call a function
```

## Function Parameters

```python
def function_name(param1, param2=default_value, *args, **kwargs):
    # Function body
```

## Return Statement

```python
return expression                 # Return a value from a function
```

## Variable Scope

```python
variable = "global"               # Global variable

def function_name():
    variable = "local"            # Local variable

global variable                   # Access global variable inside a function
```

## Lambda Functions

```python
lambda arguments: expression       # Anonymous function
result = lambda_function(arguments)  # Call a lambda function
```

## Built-in Functions

```python
len(iterable)                     # Get the length of an iterable
range(start, stop, step)          # Generate a sequence of numbers
print(*objects, sep=' ', end='\n') # Print objects to the console
input(prompt)                     # Accept user input from the console
```

## Recursion

```python
def recursive_function(parameters):
    if base_case_condition:
        return base_case_result
    else:
        return recursive_function(modified_parameters)
```

## Function Decorators

```python
@decorator_function
def function_name():
    # Function body
```

## Error Handling

```python
try:
    # Code that may raise an exception
except ExceptionType:
    # Code to handle the exception
finally:
    # Code that always runs, regardless of exceptions
```

## Generators

```python
def generator_function():
    yield expression                # Yield a value from the generator

result = next(generator)           # Get the next value from the generator
```

## Anonymous Functions

```python
filter(function, iterable)         # Filter elements from an iterable
map(function, iterable)            # Apply a function to each element of an iterable
```


# Python Strings Cheatsheet

## String Declaration

```python
my_string = "Hello, World!"        # Create a string
```

## Accessing Characters

```python
character = my_string[index]       # Access character at specific index
sliced_string = my_string[start:end]  # Get a substring using slicing
```

## String Concatenation

```python
new_string = string1 + string2     # Concatenate two strings
```

## String Operations

```python
length = len(my_string)            # Get the length of a string
count = my_string.count(substring)  # Count occurrences of a substring
index = my_string.index(substring)  # Get the index of the first occurrence
```

## Modifying Strings

```python
new_string = my_string.upper()     # Convert string to uppercase
new_string = my_string.lower()     # Convert string to lowercase
new_string = my_string.capitalize()  # Capitalize the first character
new_string = my_string.replace(old, new)  # Replace occurrences of a substring
```

## String Formatting

```python
formatted_string = f"My name is {name}"  # F-string formatting
formatted_string = "Hello, {}".format(name)  # Format string using placeholders
```

## String Splitting and Joining

```python
list_of_words = my_string.split()  # Split string into a list of words
new_string = " ".join(list_of_words)  # Join list of strings into a single string
```

## String Stripping

```python
stripped_string = my_string.strip()  # Remove leading and trailing whitespace
```

## String Checking

```python
is_alpha = my_string.isalpha()     # Check if string contains only alphabetic characters
is_digit = my_string.isdigit()     # Check if string contains only numeric characters
is_space = my_string.isspace()     # Check if string contains only whitespace characters
starts_with = my_string.startswith(substring)  # Check if string starts with a specific substring
ends_with = my_string.endswith(substring)      # Check if string ends with a specific substring
```

## String Searching

```python
found = substring in my_string     # Check if substring is present in string
not_found = substring not in my_string  # Check if substring is not present in string
```

## String Escaping

```python
escaped_string = "This is a \"quoted\" string."  # Use escape characters in strings
```


# Python Files Cheatsheet

## File Opening

```python
file_object = open(file_path, mode)   # Open a file in a specific mode
```

## File Modes

- `'r'` - Read mode (default)
- `'w'` - Write mode (overwrites existing file or creates a new file)
- `'a'` - Append mode (appends to existing file or creates a new file)
- `'x'` - Exclusive creation mode (creates a new file but raises an error if the file already exists)
- `'b'` - Binary mode
- `'t'` - Text mode (default)
- `'+'` - Update mode (for reading and writing)

## File Closing

```python
file_object.close()                  # Close the file
```

## File Reading

```python
content = file_object.read()         # Read the entire file content
line = file_object.readline()        # Read a single line from the file
lines = file_object.readlines()      # Read all lines and return a list
```

## File Writing

```python
file_object.write(content)           # Write content to the file
```

## File Appending

```python
file_object.write(content)           # Append content to the file
```

## File Iteration

```python
for line in file_object:             # Iterate over each line in the file
    # Perform actions on each line
```

## File Seek

```python
file_object.seek(offset)             # Move the file pointer to a specific position
```

## File Metadata

```python
file_object.name                     # Get the name of the file
file_object.mode                     # Get the mode in which the file was opened
file_object.closed                   # Check if the file is closed
```

## File Existence

```python
import os

exists = os.path.exists(file_path)    # Check if a file exists
```

## File Deletion

```python
import os

os.remove(file_path)                  # Delete a file
```

## File Renaming

```python
import os

os.rename(old_file_path, new_file_path)  # Rename a file
```


# Python Dictionaries Cheatsheet

## Dictionary Declaration

```python
my_dict = {}                              # Create an empty dictionary
my_dict = {"key1": value1, "key2": value2}  # Create a dictionary with initial key-value pairs
```

## Accessing Values

```python
value = my_dict[key]                      # Access value using key
```

## Modifying Values

```python
my_dict[key] = new_value                  # Modify value using key
```

## Adding Key-Value Pairs

```python
my_dict[new_key] = new_value              # Add new key-value pair
```

## Dictionary Operations

```python
len(my_dict)                              # Get the number of key-value pairs in the dictionary
del my_dict[key]                          # Delete a key-value pair by key
```

## Dictionary Methods

```python
keys = my_dict.keys()                     # Get all keys in the dictionary
values = my_dict.values()                 # Get all values in the dictionary
items = my_dict.items()                   # Get all key-value pairs as tuples
```

## Checking Key Existence

```python
key_exists = key in my_dict               # Check if a key exists in the dictionary
```

## Dictionary Copying

```python
new_dict = my_dict.copy()                 # Shallow copy of the dictionary
```

## Dictionary Comprehension

```python
new_dict = {key: value for key, value in iterable}   # Create a new dictionary using comprehension
```


# Random Library Cheat Sheet

The `random` library in Python provides functions for generating random numbers, shuffling sequences, and making random choices. It is commonly used in various applications, including simulations, games, and cryptography.

To use the `random` library, you need to import it first:

```python
import random
```

## Generating Random Numbers

### `random()`

Generates a random float number between 0 and 1 (exclusive).

Example:
```python
random_number = random.random()
print(random_number)
```

### `randrange(start, stop[, step])`

Generates a random integer from the specified range. If `step` is provided, it specifies the increment between the numbers.

Example:
```python
random_number = random.randrange(1, 10)
print(random_number)
```

### `randint(a, b)`

Generates a random integer between `a` and `b` (inclusive).

Example:
```python
random_number = random.randint(1, 100)
print(random_number)
```

## Shuffling Sequences

### `shuffle(sequence)`

Randomly shuffles the elements in a sequence in place.

Example:
```python
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)
```

### `sample(sequence, k)`

Returns a new list with `k` unique elements randomly chosen from the sequence.

Example:
```python
my_list = [1, 2, 3, 4, 5]
random_sample = random.sample(my_list, 3)
print(random_sample)
```

## Making Random Choices

### `choice(sequence)`

Returns a random element from a non-empty sequence.

Example:
```python
my_list = [1, 2, 3, 4, 5]
random_choice = random.choice(my_list)
print(random_choice)
```

### `choices(sequence, weights=None, k=1)`

Returns a list with `k` elements randomly chosen from the sequence. The `weights` parameter can be used to specify the probability of selecting each element.

Example:
```python
my_list = [1, 2, 3, 4, 5]
random_choices = random.choices(my_list, k=3)
print(random_choices)
```

## Setting the Random Seed

### `seed(a=None)`

Initializes the random number generator with the provided seed value. If no seed value is given, it uses the system time.

Example:
```python
random.seed(42)
random_number = random.random()
print(random_number)
```

Note: Setting the seed allows you to generate the same sequence of random numbers each time the code runs. This can be useful for reproducing results or debugging.


 
# Datetime Library Cheat Sheet

The `datetime` library in Python provides classes for manipulating dates, times, and intervals. It is commonly used for working with timestamps, performing date calculations, and formatting dates for display.

To use the `datetime` library, you need to import it first:

```python
import datetime
```

## Date and Time Components

### `date(year, month, day)`

Represents a date (year, month, day) without time.

Example:
```python
my_date = datetime.date(2023, 6, 9)
print(my_date)
```

### `time(hour, minute, second[, microsecond])`

Represents a time (hour, minute, second) with an optional microsecond component.

Example:
```python
my_time = datetime.time(12, 30, 45)
print(my_time)
```

### `datetime(year, month, day[, hour[, minute[, second[, microsecond]]]])`

Represents a specific date and time (year, month, day, hour, minute, second, microsecond).

Example:
```python
my_datetime = datetime.datetime(2023, 6, 9, 12, 30, 45)
print(my_datetime)
```

## Current Date and Time

### `datetime.now()`

Returns the current local date and time.

Example:
```python
current_datetime = datetime.datetime.now()
print(current_datetime)
```

## Formatting and Parsing

### `strftime(format)`

Formats a `datetime` object as a string using the specified format codes.

Example:
```python
my_datetime = datetime.datetime.now()
formatted_datetime = my_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_datetime)
```

### `strptime(date_string, format)`

Parses a string representing a date and time and returns a `datetime` object.

Example:
```python
date_string = "2023-06-09 12:30:45"
parsed_datetime = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(parsed_datetime)
```

## Date Arithmetic

### `timedelta(days[, seconds[, microseconds[, milliseconds[, minutes[, hours[, weeks]]]]]])`

Represents a duration or difference between two dates or times.

Example:
```python
start_date = datetime.date(2023, 6, 1)
end_date = datetime.date(2023, 6, 9)
duration = end_date - start_date
print(duration.days)
```

## Extracting Date and Time Components

### `year`, `month`, `day`, `hour`, `minute`, `second`, `microsecond`

Attributes of a `datetime` object that provide individual date and time components.

Example:
```python
my_datetime = datetime.datetime.now()
print(my_datetime.year)
print(my_datetime.month)
print(my_datetime.day)
```
