def factorial_recursive(n):
    """Calculate factorial using standard recursion."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

# Example usage
if __name__ == "__main__":
    num = int(input("Enter a number to find its factorial: "))
    print("Factorial (recursive):", factorial_recursive(num))
