def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Example usage
if __name__ == "__main__":
    number = int(input("Enter a non-negative integer: "))  # User input
    print(factorial_recursive(number))  # Output: Factorial of the entered number
