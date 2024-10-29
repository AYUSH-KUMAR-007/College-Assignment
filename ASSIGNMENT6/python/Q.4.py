def precedence(op):
    """Return the precedence of the given operator."""
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0

def infix_to_postfix(expression):
    """Convert infix expression to postfix expression."""
    stack = []  # Stack to hold operators
    postfix = []  # List for output
    for char in expression:
        if char.isalnum():  # If the character is an operand (A-Z, a-z, 0-9)
            postfix.append(char)
        elif char == '(':  # If the character is '(', push it to stack
            stack.append(char)
        elif char == ')':  # If the character is ')'
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()  # Pop '(' from stack
        else:  # If an operator is encountered
            while (stack and precedence(stack[-1]) >= precedence(char)):
                postfix.append(stack.pop())
            stack.append(char)

    # Pop all the operators from the stack
    while stack:
        postfix.append(stack.pop())
    
    return ''.join(postfix)

# Example usage
if __name__ == "__main__":
    expression = input("Enter an infix expression: ")
    postfix_expression = infix_to_postfix(expression)
    print("Postfix expression:", postfix_expression)
