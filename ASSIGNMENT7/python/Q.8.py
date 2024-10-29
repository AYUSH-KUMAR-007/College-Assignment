class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []  # Stack for enqueue operations
        self.stack2 = []  # Stack for dequeue operations

    # Function to enqueue an element to the queue
    def enqueue(self, item):
        self.stack1.append(item)  # Push item onto stack1
        print(f"Enqueued {item} to the queue.")

    # Function to dequeue an element from the queue
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty! Cannot dequeue element.")
            return None
        
        # If stack2 is empty, transfer elements from stack1 to stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())  # Pop from stack1 and push to stack2
        
        return self.stack2.pop()  # Pop the top element from stack2

    # Function to check if the queue is empty
    def is_empty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0

    # Function to display the current elements in the queue
    def display(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            # The current elements in the queue are in stack2 and stack1
            # Elements in stack2 are in correct order, while elements in stack1 need to be reversed
            print("Queue elements:", end=" ")
            temp_stack = self.stack2.copy()  # Copy stack2 to avoid modifying it
            while temp_stack:
                print(temp_stack.pop(), end=" ")
            # Now print stack1 in reverse order
            for item in reversed(self.stack1):
                print(item, end=" ")
            print()  # Newline for better formatting


# Test the QueueUsingStacks class
queue = QueueUsingStacks()

# Enqueue elements to the queue
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

# Display the queue
queue.display()

# Dequeue elements from the queue
print(f"Dequeued: {queue.dequeue()}")
print(f"Dequeued: {queue.dequeue()}")

# Display the queue after dequeuing
queue.display()

# Enqueue more elements
queue.enqueue(40)
queue.enqueue(50)

# Final state of the queue
queue.display()
