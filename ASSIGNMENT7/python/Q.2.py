# Node class to represent each element in the linked list
class Node:
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Pointer to the next node


# LinearQueue class using a linked list
class LinearQueue:
    def __init__(self):
        self.front = None  # Pointer to the front node
        self.rear = None   # Pointer to the rear node

    # Function to check if the queue is empty
    def is_empty(self):
        return self.front is None

    # Function to add an element to the queue (enqueue)
    def enqueue(self, element):
        new_node = Node(element)
        if self.rear is None:  # If the queue is empty
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node  # Link the new node at the end of the queue
            self.rear = new_node       # Update the rear pointer
        print(f"Enqueued: {element}")

    # Function to remove an element from the queue (dequeue)
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty! Cannot dequeue element.")
        else:
            removed_element = self.front.data
            self.front = self.front.next  # Move the front pointer to the next node
            if self.front is None:  # If the queue becomes empty, update the rear as well
                self.rear = None
            print(f"Dequeued: {removed_element}")

    # Function to display the elements of the queue
    def display(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            print("Queue elements:", end=" ")
            current = self.front
            while current:
                print(current.data, end=" ")
                current = current.next
            print()  # Newline for better formatting


# Test the LinearQueue class
queue = LinearQueue()

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
queue.display()
