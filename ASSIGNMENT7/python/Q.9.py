from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()  # Initialize a queue using deque

    # Function to enqueue an element to the queue
    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued {item} to the queue.")

    # Function to dequeue an element from the queue
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty! Cannot dequeue element.")
            return None
        return self.queue.popleft()  # Pop from the front of the queue

    # Function to check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # Function to reverse the queue
    def reverse(self):
        if self.is_empty():
            return
        # Remove the front element
        front = self.dequeue()
        # Reverse the remaining queue
        self.reverse()
        # Add the removed element to the back of the queue
        self.enqueue(front)

    # Function to display the current elements in the queue
    def display(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            print("Queue elements:", list(self.queue))  # Convert deque to list for display


# Test the Queue class
queue = Queue()

# Enqueue elements to the queue
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)

# Display the original queue
print("Original queue:")
queue.display()

# Reverse the queue
queue.reverse()

# Display the reversed queue
print("Reversed queue:")
queue.display()
