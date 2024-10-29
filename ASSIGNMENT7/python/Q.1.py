class LinearQueue:
    def __init__(self, size):
        self.queue = [None] * size  # Create an array of fixed size
        self.front = -1  # Front pointer for dequeue operations
        self.rear = -1   # Rear pointer for enqueue operations
        self.size = size

    # Function to check if the queue is empty
    def is_empty(self):
        return self.front == -1

    # Function to check if the queue is full
    def is_full(self):
        return self.rear == self.size - 1

    # Function to add an element to the queue (enqueue)
    def enqueue(self, element):
        if self.is_full():
            print("Queue is full! Cannot enqueue element.")
        else:
            if self.front == -1:  # If queue is empty, set front to 0
                self.front = 0
            self.rear += 1
            self.queue[self.rear] = element
            print(f"Enqueued: {element}")

    # Function to remove an element from the queue (dequeue)
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty! Cannot dequeue element.")
        else:
            removed_element = self.queue[self.front]
            self.queue[self.front] = None  # Optional: Clear the dequeued position
            if self.front == self.rear:  # If queue becomes empty after this operation
                self.front = -1
                self.rear = -1
            else:
                self.front += 1
            print(f"Dequeued: {removed_element}")

    # Function to display the elements of the queue
    def display(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            print("Queue elements:", end=" ")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()  # Newline for better formatting

# Test the LinearQueue class
queue_size = 5
queue = LinearQueue(queue_size)

# Enqueue elements
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)

# Display the queue
queue.display()

# Dequeue elements
queue.dequeue()
queue.dequeue()

# Display the queue after dequeuing
queue.display()

# Try to enqueue more elements to show full condition
queue.enqueue(60)
queue.display()
