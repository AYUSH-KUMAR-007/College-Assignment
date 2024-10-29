class Node:
    """A node of the linked list used in the stack."""
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    """A stack implementation using a linked list."""
    def __init__(self):
        self.top = None

    def is_empty(self):
        """Check if the stack is empty."""
        return self.top is None

    def push(self, item):
        """Add an item to the top of the stack."""
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        print(f"Pushed {item} onto stack.")

    def pop(self):
        """Remove and return the top item of the stack."""
        if self.is_empty():
            print("Stack Underflow! Cannot pop from an empty stack.")
            return None
        else:
            popped_node = self.top
            self.top = self.top.next
            print(f"Popped {popped_node.data} from stack.")
            return popped_node.data

    def peek(self):
        """Return the top item of the stack without removing it."""
        if self.is_empty():
            print("Stack is empty! Cannot peek.")
            return None
        else:
            return self.top.data

    def display(self):
        """Display the contents of the stack."""
        if self.is_empty():
            print("Stack is empty!")
            return
        current = self.top
        stack_contents = []
        while current:
            stack_contents.append(current.data)
            current = current.next
        print("Stack contents:", stack_contents)

# Example usage
if __name__ == "__main__":
    stack = Stack()

    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()

    print("Top element is:", stack.peek())
    
    stack.pop()
    stack.display()
    
    stack.pop()
    stack.pop()  # This should show underflow message

    stack.pop()  # This should show underflow message

    stack.push(40)
    stack.display()
