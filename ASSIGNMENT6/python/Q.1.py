class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []
    
    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0
    
    def is_full(self):
        """Check if the stack is full."""
        return len(self.stack) == self.capacity
    
    def push(self, item):
        """Add an item to the top of the stack."""
        if self.is_full():
            print("Stack Overflow! Cannot push", item)
        else:
            self.stack.append(item)
            print(f"Pushed {item} onto stack.")
    
    def pop(self):
        """Remove and return the top item of the stack."""
        if self.is_empty():
            print("Stack Underflow! Cannot pop from an empty stack.")
            return None
        else:
            item = self.stack.pop()
            print(f"Popped {item} from stack.")
            return item
    
    def peek(self):
        """Return the top item of the stack without removing it."""
        if self.is_empty():
            print("Stack is empty! Cannot peek.")
            return None
        else:
            return self.stack[-1]
    
    def display(self):
        """Display the contents of the stack."""
        if self.is_empty():
            print("Stack is empty!")
        else:
            print("Stack contents:", self.stack)

# Example usage
if __name__ == "__main__":
    stack_capacity = 5
    stack = Stack(stack_capacity)

    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()

    print("Top element is:", stack.peek())
    
    stack.pop()
    stack.display()
    
    stack.pop()
    stack.pop()
    stack.pop()  # This should show underflow message

    stack.push(40)
    stack.display()
