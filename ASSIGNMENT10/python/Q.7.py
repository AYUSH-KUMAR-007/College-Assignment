class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.is_threaded = False  # Indicates if the right pointer is a thread

class ThreadedBinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return
        
        current = self.root
        parent = None
        
        while current:
            parent = current
            if data < current.data:
                current = current.left
            else:
                current = current.right

        if data < parent.data:
            parent.left = new_node
            # Create a thread to the parent
            new_node.right = parent
            new_node.is_threaded = True
        else:
            parent.right = new_node
            # Create a thread to the parent
            new_node.right = self.inorder_successor(parent)
            if new_node.right:
                new_node.is_threaded = True

    def inorder_successor(self, node):
        current = node.right
        while current and current.left:
            current = current.left
        return current

    def inorder_traversal(self):
        current = self.root
        # Go to the leftmost node
        while current and current.left:
            current = current.left
        
        # Now current is the leftmost node
        while current:
            print(current.data, end=' ')
            # If the node has a thread, use it
            if current.is_threaded:
                current = current.right
            else:
                current = current.right
                # Move to the leftmost node of the right subtree
                while current and current.left:
                    current = current.left

# Example Usage
if __name__ == "__main__":
    tbt = ThreadedBinaryTree()
    data = [20, 10, 30, 5, 15, 25, 35]
    
    for value in data:
        tbt.insert(value)

    print("In-order Traversal of the Two-Way Threaded Binary Tree:")
    tbt.inorder_traversal()
