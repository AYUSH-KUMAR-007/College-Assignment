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

    def inorder_traversal(self, node, result):
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.data)
            self.inorder_traversal(node.right, result)

    def preorder_traversal(self, node, result):
        if node:
            result.append(node.data)
            self.preorder_traversal(node.left, result)
            self.preorder_traversal(node.right, result)

    def postorder_traversal(self, node, result):
        if node:
            self.postorder_traversal(node.left, result)
            self.postorder_traversal(node.right, result)
            result.append(node.data)

# Example Usage
if __name__ == "__main__":
    # Create a binary tree and insert nodes
    bt = BinaryTree(1)  # Root node
    bt.insert(2)
    bt.insert(3)
    bt.insert(4)
    bt.insert(5)

    # Traversal results
    inorder_result = []
    preorder_result = []
    postorder_result = []

    bt.inorder_traversal(bt.root, inorder_result)
    bt.preorder_traversal(bt.root, preorder_result)
    bt.postorder_traversal(bt.root, postorder_result)

    # Print results
    print("In-order Traversal:", inorder_result)
    print("Pre-order Traversal:", preorder_result)
    print("Post-order Traversal:", postorder_result)
