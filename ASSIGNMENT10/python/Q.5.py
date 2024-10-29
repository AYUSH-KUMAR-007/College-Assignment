class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.value:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_recursive(node.right, key)

    def inorder_traversal(self, node, result):
        if node is not None:
            self.inorder_traversal(node.left, result)
            result.append(node.value)
            self.inorder_traversal(node.right, result)

def sort_numbers_with_bst(numbers):
    bst = BinarySearchTree()
    
    # Insert all numbers into the BST
    for number in numbers:
        bst.insert(number)

    # Retrieve the sorted numbers
    sorted_numbers = []
    bst.inorder_traversal(bst.root, sorted_numbers)
    return sorted_numbers

# Example Usage
if __name__ == "__main__":
    numbers = [35, 10, 15, 30, 5, 50, 40]
    
    sorted_numbers = sort_numbers_with_bst(numbers)

    # Print results
    print("Original Numbers:", numbers)
    print("Sorted Numbers:", sorted_numbers)
