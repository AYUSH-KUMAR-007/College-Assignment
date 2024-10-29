class Stack:
    """A simple stack implementation."""
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

def decimal_to_binary(decimal):
    """Convert a decimal number to binary using a stack."""
    stack = Stack()
    
    if decimal == 0:
        return "0"

    while decimal > 0:
        remainder = decimal % 2
        stack.push(remainder)
        decimal //= 2

    binary_number = ""
    while not stack.is_empty():
        binary_number += str(stack.pop())

    return binary_number

# Example usage
if __name__ == "__main__":
    decimal_number = int(input("Enter a decimal number: "))
    binary_representation = decimal_to_binary(decimal_number)
    print(f"Binary representation: {binary_representation}")
