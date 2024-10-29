#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *left;
    struct Node *right;
};

void mirror(struct Node* node) {
    if (node == NULL) return;
    struct Node* temp;
    mirror(node->left);
    mirror(node->right);
    temp = node->left;
    node->left = node->right;
    node->right = temp;
}

void inorder(struct Node* node) {
    if (node == NULL) return;
    inorder(node->left);
    printf("%d ", node->data);
    inorder(node->right);
}

int main() {
    struct Node* root = NULL;
    root = insert(root, 50);
    insert(root, 30);
    insert(root, 20);
    insert(root, 40);
    insert(root, 70);
    insert(root, 60);
    insert(root, 80);

    printf("Original BST: ");
    inorder(root);
    printf("\n");

    mirror(root);
    printf("Mirror BST: ");
    inorder(root);
    printf("\n");
    return 0;
}
