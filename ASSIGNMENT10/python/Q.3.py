class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_data):
        self.root = TreeNode(root_data)

    def insert(self, data):
        new_node = TreeNode(data)
        queue = [self.root]
        
        while queue:
            current = queue.pop(0)
            if current.left is None:
                current.left = new_node
                return
            else:
                queue.append(current.left)

            if current.right is None:
                current.right = new_node
                return
            else:
                queue.append(current.right)

    def is_full_tree(self, node):
        if node is None:
            return True
        if (node.left is None and node.right is not None) or (node.left is not None and node.right is None):
            return False
        return self.is_full_tree(node.left) and self.is_full_tree(node.right)

    def count_nodes(self, node):
        if node is None:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

    def is_complete_tree(self, node, index, number_nodes):
        if node is None:
            return True
        if index >= number_nodes:
            return False
        return (self.is_complete_tree(node.left, 2 * index + 1, number_nodes) and
                self.is_complete_tree(node.right, 2 * index + 2, number_nodes))

# Example Usage
if __name__ == "__main__":
    # Create a binary tree and insert nodes
    bt = BinaryTree(1)
    bt.insert(2)
    bt.insert(3)
    bt.insert(4)
    bt.insert(5)
    
    # Check if the tree is full and complete
    full_tree = bt.is_full_tree(bt.root)
    number_of_nodes = bt.count_nodes(bt.root)
    complete_tree = bt.is_complete_tree(bt.root, 0, number_of_nodes)

    # Print results
    print("Is the tree full?:", full_tree)
    print("Is the tree complete?:", complete_tree)
