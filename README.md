
# Factorial Calculation

This project provides two Python implementations for calculating the factorial of a number. You can find both methods – using loops and recursion – in separate files to compare and understand their approaches.

## Table of Contents
- [Overview](#overview)
- [Methods](#methods)
  - [Loop Method](#loop-method)
  - [Recursive Method](#recursive-method)
- [Usage](#usage)
- [Requirements](#requirements)
- [License](#license)

## Overview
A factorial of a non-negative integer `n` is the product of all positive integers less than or equal to `n`. Factorials are often represented with the symbol `n!`. This project demonstrates two approaches to calculate factorials:
1. Using a `for` loop
2. Using recursion

## Methods

### Loop Method
The loop-based factorial calculation is located in the file `factorial_loop.py`. This method calculates the factorial by iteratively multiplying numbers from `1` to `n`.

Example:
```python
def factorial_loop(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```

### Recursive Method

The recursive factorial calculation is implemented in factorial_recursive.py. This method calls itself with decreasing values of n until reaching the base case (n = 1).

Example:

```
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
```

## Usage

1. Clone the repository:

```
git clone https://github.com/CheryMinkyy/factorial-calculation.git
```

2. Navigate to the project folder:

```
cd factorial-calculation
```
3. Run the Python files:

```
python factorial_loop.py
python factorial_recursive.py
```
