class MultiStack:
    def __init__(self, num_stacks, stack_size):
        self.num_stacks = num_stacks
        self.stack_size = stack_size
        self.array = [None] * (num_stacks * stack_size)
        self.sizes = [0] * num_stacks  # To keep track of each stack's current size

    def is_empty(self, stack_num):
        return self.sizes[stack_num] == 0

    def is_full(self, stack_num):
        return self.sizes[stack_num] == self.stack_size

    def index_of_top(self, stack_num):
        # Calculate the index of the top of the given stack
        offset = stack_num * self.stack_size
        return offset + self.sizes[stack_num] - 1

    def push(self, stack_num, value):
        if self.is_full(stack_num):
            raise OverflowError(f"Stack {stack_num} is full!")
        self.sizes[stack_num] += 1
        self.array[self.index_of_top(stack_num)] = value

    def pop(self, stack_num):
        if self.is_empty(stack_num):
            raise IndexError(f"Stack {stack_num} is empty!")
        top_index = self.index_of_top(stack_num)
        value = self.array[top_index]
        self.array[top_index] = None  # Clear the value
        self.sizes[stack_num] -= 1
        return value

    def peek(self, stack_num):
        if self.is_empty(stack_num):
            raise IndexError(f"Stack {stack_num} is empty!")
        return self.array[self.index_of_top(stack_num)]

# Test the MultiStack implementation
if __name__ == "__main__":
    num_stacks = 3
    stack_size = 5
    multi_stack = MultiStack(num_stacks, stack_size)

    # Push values to different stacks
    multi_stack.push(0, 10)
    multi_stack.push(0, 20)
    multi_stack.push(1, 30)
    multi_stack.push(2, 40)
    multi_stack.push(2, 50)

    # Peek values from different stacks
    print(f"Top of stack 0: {multi_stack.peek(0)}")  # Should print 20
    print(f"Top of stack 1: {multi_stack.peek(1)}")  # Should print 30
    print(f"Top of stack 2: {multi_stack.peek(2)}")  # Should print 50

    # Pop values from different stacks
    print(f"Popped from stack 0: {multi_stack.pop(0)}")  # Should print 20
    print(f"Popped from stack 2: {multi_stack.pop(2)}")  # Should print 50
