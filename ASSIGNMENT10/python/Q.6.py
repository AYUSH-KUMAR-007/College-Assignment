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

    def mirror(self, node):
        if node is not None:
            # Swap the left and right children
            node.left, node.right = node.right, node.left
            # Recursively call mirror on left and right children
            self.mirror(node.left)
            self.mirror(node.right)

# Example Usage
if __name__ == "__main__":
    # Create a binary search tree
    bst = BinarySearchTree()
    keys = [15, 10, 20, 8, 12, 17, 25]
    
    for key in keys:
        bst.insert(key)

    # Print original in-order traversal
    original_inorder = []
    bst.inorder_traversal(bst.root, original_inorder)
    print("Original In-order Traversal of BST:", original_inorder)

    # Find the mirror image
    bst.mirror(bst.root)

    # Print mirrored in-order traversal
    mirrored_inorder = []
    bst.inorder_traversal(bst.root, mirrored_inorder)
    print("In-order Traversal of Mirrored BST:", mirrored_inorder)
