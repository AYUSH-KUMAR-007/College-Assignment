def factorial_tail_recursive(n, accumulator=1):
    """Calculate factorial using tail recursion."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return accumulator
    return factorial_tail_recursive(n - 1, n * accumulator)

# Example usage
if __name__ == "__main__":
    num = int(input("Enter a number to find its factorial (tail recursive): "))
    print("Factorial (tail recursive):", factorial_tail_recursive(num))
