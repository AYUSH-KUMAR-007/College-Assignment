class Node:
    """Class to represent a node in the linked list."""
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node


class Dequeue:
    """Class to represent the double-ended queue."""
    def __init__(self):
        self.front = None  # Front pointer
        self.rear = None   # Rear pointer

    # Function to check if the dequeue is empty
    def is_empty(self):
        return self.front is None

    # Function to add an element at the front of the dequeue
    def insert_front(self, element):
        new_node = Node(element)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
        print(f"Inserted {element} at the front.")

    # Function to add an element at the rear of the dequeue
    def insert_rear(self, element):
        new_node = Node(element)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node
        print(f"Inserted {element} at the rear.")

    # Function to remove an element from the front of the dequeue
    def delete_front(self):
        if self.is_empty():
            print("Dequeue is empty! Cannot delete element from front.")
        else:
            removed_element = self.front.data
            if self.front == self.rear:  # If only one element is present
                self.front = self.rear = None
            else:
                self.front = self.front.next
                self.front.prev = None
            print(f"Deleted {removed_element} from the front.")

    # Function to remove an element from the rear of the dequeue
    def delete_rear(self):
        if self.is_empty():
            print("Dequeue is empty! Cannot delete element from rear.")
        else:
            removed_element = self.rear.data
            if self.front == self.rear:  # If only one element is present
                self.front = self.rear = None
            else:
                self.rear = self.rear.prev
                self.rear.next = None
            print(f"Deleted {removed_element} from the rear.")

    # Function to display the elements in the dequeue
    def display(self):
        if self.is_empty():
            print("Dequeue is empty!")
        else:
            print("Dequeue elements:", end=" ")
            current = self.front
            while current:
                print(current.data, end=" ")
                current = current.next
            print()  # Newline for better formatting


# Test the Dequeue class
dequeue = Dequeue()

# Insert elements at the front and rear
dequeue.insert_rear(10)
dequeue.insert_rear(20)
dequeue.insert_front(5)
dequeue.insert_front(1)

# Display the dequeue
dequeue.display()

# Delete elements from the front and rear
dequeue.delete_front()
dequeue.delete_rear()

# Display the dequeue after deletions
dequeue.display()

# Insert more elements
dequeue.insert_front(30)
dequeue.insert_rear(40)

# Final state of the dequeue
dequeue.display()
