# Fundamentos de Programacion 2023-1
Ejercicios Ticademia

Here's a cheat sheet for conditionals in Python:

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

Example:
```python
x = 5
result = "positive" if x > 0 else "negative or zero"
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


 Sure! Here's a cheat sheet for the `datetime` library in Python:

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
