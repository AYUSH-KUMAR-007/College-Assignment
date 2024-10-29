#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *left;
    struct Node *right;
};

struct Node* insert(struct Node* node, int data) {
    if (node == NULL) {
        return createNode(data);
    }
    if (data < node->data) {
        node->left = insert(node->left, data);
    } else {
        node->right = insert(node->right, data);
    }
    return node;
}

void inorder(struct Node* node) {
    if (node == NULL) return;
    inorder(node->left);
    printf("%d ", node->data);
    inorder(node->right);
}

int main() {
    int numbers[] = {40, 10, 30, 20, 50, 60};
    int n = sizeof(numbers) / sizeof(numbers[0]);
    
    struct Node* root = NULL;
    for (int i = 0; i < n; i++) {
        root = insert(root, numbers[i]);
    }

    printf("Sorted numbers: ");
    inorder(root);
    printf("\n");
    return 0;
}
