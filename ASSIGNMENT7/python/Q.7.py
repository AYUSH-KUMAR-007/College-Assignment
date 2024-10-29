from collections import deque

class StackUsingQueues:
    def __init__(self):
        self.queue1 = deque()  # Main queue to store elements
        self.queue2 = deque()  # Auxiliary queue for stack operations

    # Function to push an element onto the stack
    def push(self, item):
        # Add the new item to the auxiliary queue
        self.queue2.append(item)
        
        # Move all elements from queue1 to queue2
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        
        # Swap the names of the two queues
        self.queue1, self.queue2 = self.queue2, self.queue1
        print(f"Pushed {item} onto the stack.")

    # Function to pop the top element from the stack
    def pop(self):
        if self.is_empty():
            print("Stack is empty! Cannot pop element.")
            return None
        popped_item = self.queue1.popleft()  # Remove the front element from queue1
        print(f"Popped {popped_item} from the stack.")
        return popped_item

    # Function to peek at the top element of the stack
    def peek(self):
        if self.is_empty():
            print("Stack is empty! Cannot peek.")
            return None
        return self.queue1[0]  # Return the front element without removing it

    # Function to check if the stack is empty
    def is_empty(self):
        return len(self.queue1) == 0

    # Function to display the current elements in the stack
    def display(self):
        if self.is_empty():
            print("Stack is empty!")
        else:
            print("Stack elements:", list(self.queue1))  # Convert deque to list for display


# Test the StackUsingQueues class
stack = StackUsingQueues()

# Push elements onto the stack
stack.push(10)
stack.push(20)
stack.push(30)

# Display the stack
stack.display()

# Peek at the top element
print(f"Top element: {stack.peek()}")

# Pop elements from the stack
stack.pop()
stack.pop()

# Display the stack after popping
stack.display()

# Push more elements
stack.push(40)
stack.push(50)

# Final state of the stack
stack.display()
