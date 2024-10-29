def evaluate_postfix(expression):
    """Evaluate a postfix expression."""
    stack = []
    
    for char in expression:
        if char.isdigit():  # Check if the character is a digit
            stack.append(int(char))  # Push the operand onto the stack
        else:  # The character is an operator
            b = stack.pop()  # Pop the top two operands
            a = stack.pop()
            if char == '+':
                stack.append(a + b)
            elif char == '-':
                stack.append(a - b)
            elif char == '*':
                stack.append(a * b)
            elif char == '/':
                stack.append(a / b)
            else:
                raise ValueError(f"Unknown operator: {char}")
    
    return stack.pop()  # The final result is the last item on the stack

# Example usage
if __name__ == "__main__":
    expression = input("Enter a postfix expression (e.g., '23 34 +'): ")
    result = evaluate_postfix(expression.split())
    print("Result of the postfix expression:", result)
