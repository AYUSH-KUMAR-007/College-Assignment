def fibonacci_tail_recursive(n, a=0, b=1):
    """Calculate Fibonacci number using tail recursion."""
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers.")
    if n == 0:
        return a
    if n == 1:
        return b
    return fibonacci_tail_recursive(n - 1, b, a + b)

# Example usage
if __name__ == "__main__":
    n = int(input("Enter a number to find its Fibonacci value (tail recursion): "))
    print(f"Fibonacci({n}) =", fibonacci_tail_recursive(n))
