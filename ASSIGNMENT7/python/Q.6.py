import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []  # List to store the heap elements

    # Function to insert an element into the priority queue
    def push(self, item, priority):
        # The heapq module uses a min-heap, so we invert the priority to implement a max-heap
        heapq.heappush(self.heap, (-priority, item))
        print(f"Inserted {item} with priority {priority}")

    # Function to remove and return the element with the highest priority
    def pop(self):
        if self.is_empty():
            print("Priority Queue is empty! Cannot pop element.")
            return None
        else:
            priority, item = heapq.heappop(self.heap)  # Pops the highest priority item
            print(f"Popped {item} with priority {-priority}")
            return item

    # Function to check if the priority queue is empty
    def is_empty(self):
        return len(self.heap) == 0

    # Function to display the current elements in the priority queue
    def display(self):
        if self.is_empty():
            print("Priority Queue is empty!")
        else:
            print("Priority Queue elements:")
            for priority, item in self.heap:
                print(f"Item: {item}, Priority: {-priority}")  # Invert priority for display


# Test the PriorityQueue class
priority_queue = PriorityQueue()

# Inserting elements with priorities
priority_queue.push("Task A", 1)
priority_queue.push("Task B", 3)
priority_queue.push("Task C", 2)

# Display the current state of the priority queue
priority_queue.display()

# Popping elements based on priority
priority_queue.pop()
priority_queue.pop()

# Display the queue after popping
priority_queue.display()

# Insert more elements
priority_queue.push("Task D", 5)
priority_queue.push("Task E", 4)

# Final state of the priority queue
priority_queue.display()
