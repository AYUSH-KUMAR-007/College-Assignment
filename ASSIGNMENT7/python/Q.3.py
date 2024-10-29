class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size  # Create an array of fixed size
        self.front = -1  # Front pointer for dequeue operations
        self.rear = -1   # Rear pointer for enqueue operations

    # Function to check if the queue is empty
    def is_empty(self):
        return self.front == -1

    # Function to check if the queue is full
    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    # Function to add an element to the queue (enqueue)
    def enqueue(self, element):
        if self.is_full():
            print("Queue is full! Cannot enqueue element.")
        else:
            if self.front == -1:  # If queue is empty, set front to 0
                self.front = 0
            self.rear = (self.rear + 1) % self.size  # Circular increment
            self.queue[self.rear] = element
            print(f"Enqueued: {element}")

    # Function to remove an element from the queue (dequeue)
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty! Cannot dequeue element.")
        else:
            removed_element = self.queue[self.front]
            if self.front == self.rear:  # If queue becomes empty after this operation
                self.front = -1
                self.rear = -1
            else:
                self.front = (self.front + 1) % self.size  # Circular increment
            print(f"Dequeued: {removed_element}")

    # Function to display the elements of the queue
    def display(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            print("Queue elements:", end=" ")
            i = self.front
            while True:
                print(self.queue[i], end=" ")
                if i == self.rear:  # Stop when we reach the rear
                    break
                i = (i + 1) % self.size  # Circular increment
            print()  # Newline for better formatting


# Test the CircularQueue class
queue_size = 5
queue = CircularQueue(queue_size)

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

# Enqueue more elements
queue.enqueue(60)
queue.enqueue(70)

# Display the final state of the queue
queue.display()
