# Function to reverse a string using a stack
def reverse_string(input_string):
    # Create a stack (using a list in Python)
    stack = []

    # Push all characters of the input string onto the stack
    for char in input_string:
        stack.append(char)

    # Pop characters from the stack to get the reversed string
    reversed_string = ''
    while stack:
        reversed_string += stack.pop()

    return reversed_string

# Test the function
input_string = "Hello, World!"
reversed_string = reverse_string(input_string)
print(f"Original String: {input_string}")
print(f"Reversed String: {reversed_string}")
