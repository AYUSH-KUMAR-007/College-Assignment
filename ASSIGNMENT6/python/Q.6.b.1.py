def fibonacci_recursive(n):
    """Calculate Fibonacci number using standard recursion."""
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Example usage
if __name__ == "__main__":
    n = int(input("Enter a number to find its Fibonacci value (standard recursion): "))
    print(f"Fibonacci({n}) =", fibonacci_recursive(n))
