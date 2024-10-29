#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *left;
    struct Node *right;
};

int isFullBinaryTree(struct Node* node) {
    if (node == NULL) return 1;
    if (node->left == NULL && node->right == NULL) return 1;
    if (node->left != NULL && node->right != NULL)
        return isFullBinaryTree(node->left) && isFullBinaryTree(node->right);
    return 0;
}

int countNodes(struct Node* node) {
    if (node == NULL) return 0;
    return 1 + countNodes(node->left) + countNodes(node->right);
}

int isCompleteBinaryTree(struct Node* root, int index, int number_nodes) {
    if (root == NULL) return 1;
    if (index >= number_nodes) return 0;
    return isCompleteBinaryTree(root->left, 2 * index + 1, number_nodes) &&
           isCompleteBinaryTree(root->right, 2 * index + 2, number_nodes);
}

int main() {
    struct Node *root = createNode(1);
    root->left = createNode(2);
    root->right = createNode(3);
    root->left->left = createNode(4);
    root->left->right = createNode(5);

    int node_count = countNodes(root);
    printf("Is full binary tree: %s\n", isFullBinaryTree(root) ? "Yes" : "No");
    printf("Is complete binary tree: %s\n", isCompleteBinaryTree(root, 0, node_count) ? "Yes" : "No");
    return 0;
}
