class MultipleQueues:
    def __init__(self, num_queues, size):
        self.num_queues = num_queues  # Number of queues
        self.size = size  # Size of the overall array
        self.queue = [None] * size  # Array to hold all queues
        self.front = [-1] * num_queues  # Front indices for each queue
        self.rear = [-1] * num_queues   # Rear indices for each queue
        self.queue_size = size // num_queues  # Size for each individual queue

    # Function to check if a specific queue is empty
    def is_empty(self, queue_num):
        return self.front[queue_num] == -1

    # Function to check if a specific queue is full
    def is_full(self, queue_num):
        return (self.rear[queue_num] + 1) % self.queue_size == self.front[queue_num]

    # Function to add an element to a specific queue (enqueue)
    def enqueue(self, queue_num, element):
        if self.is_full(queue_num):
            print(f"Queue {queue_num} is full! Cannot enqueue element.")
        else:
            if self.is_empty(queue_num):  # If queue is empty, set front and rear to 0
                self.front[queue_num] = 0
                self.rear[queue_num] = 0
            else:
                self.rear[queue_num] = (self.rear[queue_num] + 1) % self.queue_size  # Circular increment
            
            # Calculate the position in the main array
            position = queue_num * self.queue_size + self.rear[queue_num]
            self.queue[position] = element
            print(f"Enqueued {element} to Queue {queue_num}")

    # Function to remove an element from a specific queue (dequeue)
    def dequeue(self, queue_num):
        if self.is_empty(queue_num):
            print(f"Queue {queue_num} is empty! Cannot dequeue element.")
        else:
            removed_element = self.queue[queue_num * self.queue_size + self.front[queue_num]]
            if self.front[queue_num] == self.rear[queue_num]:  # If queue becomes empty after this operation
                self.front[queue_num] = -1
                self.rear[queue_num] = -1
            else:
                self.front[queue_num] = (self.front[queue_num] + 1) % self.queue_size  # Circular increment
            print(f"Dequeued {removed_element} from Queue {queue_num}")

    # Function to display the elements of a specific queue
    def display(self, queue_num):
        if self.is_empty(queue_num):
            print(f"Queue {queue_num} is empty!")
        else:
            print(f"Queue {queue_num} elements:", end=" ")
            i = self.front[queue_num]
            while True:
                position = queue_num * self.queue_size + i
                print(self.queue[position], end=" ")
                if i == self.rear[queue_num]:
                    break
                i = (i + 1) % self.queue_size
            print()  # Newline for better formatting


# Test the MultipleQueues class
num_queues = 3
size = 9  # Total size of the array
multiple_queues = MultipleQueues(num_queues, size)

# Enqueue elements in different queues
multiple_queues.enqueue(0, 10)
multiple_queues.enqueue(0, 20)
multiple_queues.enqueue(1, 30)
multiple_queues.enqueue(1, 40)
multiple_queues.enqueue(2, 50)

# Display the queues
multiple_queues.display(0)
multiple_queues.display(1)
multiple_queues.display(2)

# Dequeue elements from different queues
multiple_queues.dequeue(0)
multiple_queues.dequeue(1)

# Display the queues after dequeuing
multiple_queues.display(0)
multiple_queues.display(1)
multiple_queues.display(2)

# Enqueue more elements to different queues
multiple_queues.enqueue(0, 60)
multiple_queues.enqueue(1, 70)
multiple_queues.enqueue(2, 80)

# Display the final state of the queues
multiple_queues.display(0)
multiple_queues.display(1)
multiple_queues.display(2)
