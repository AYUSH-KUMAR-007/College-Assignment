class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Create root node
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Display the tree structure
def display_tree(node, level=0):
    if node:
        display_tree(node.right, level + 1)
        print(' ' * 4 * level + '->', node.val)
        display_tree(node.left, level + 1)

display_tree(root)
