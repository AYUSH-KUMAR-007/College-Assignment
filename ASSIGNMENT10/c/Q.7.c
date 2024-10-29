#include <stdio.h>
#include <stdlib.h>

struct TNode {
    int data;
    struct TNode *left;
    struct TNode *right;
    int lthread, rthread; // lthread and rthread indicate if left/right is a thread
};

struct TNode* createThreadedNode(int data) {
    struct TNode* newNode = (struct TNode*)malloc(sizeof(struct TNode));
    newNode->data = data;
    newNode->left = newNode->right = NULL;
    newNode->lthread = newNode->rthread = 0;
    return newNode;
}

void insert(struct TNode** root, int data) {
    struct TNode* newNode = createThreadedNode(data);
    if (*root == NULL) {
        *root = newNode;
        return;
    }

    struct TNode* current = *root;
    struct TNode* parent = NULL;

    while (current != NULL) {
        parent = current;
        if (data < current->data) {
            if (current->lthread == 0)
                current = current->left;
            else
                break;
        } else {
            if (current->rthread == 0)
                current = current->right;
            else
                break;
        }
    }

    if (data < parent->data) {
        parent->left = newNode;
        parent->lthread = 0; // left is not a thread anymore
        newNode->left = parent->left; // thread to in-order predecessor
        newNode->right = parent; // thread to parent
        newNode->rthread = 1; // right is a thread
    } else {
        parent->right = newNode;
        parent->rthread = 0; // right is not a thread anymore
        newNode->right = parent->right; // thread to in-order successor
        newNode->left = parent; // thread to parent
        newNode->lthread = 1; // left is a thread
    }
}

void inorder(struct TNode* root) {
    if (root == NULL) return;

    struct TNode* current = root;
    while (current->lthread == 0) {
        current = current->left;
    }

    while (current != NULL) {
        printf("%d ", current->data);
        if (current->rthread == 1) {
            current = current->right;
        } else {
            current = current->right;
            while (current != NULL && current->lthread == 0) {
                current = current->left;
            }
        }
    }
}

int main() {
    struct TNode* root = NULL;
    insert(&root, 20);
    insert(&root, 10);
    insert(&root, 30);
    insert(&root, 5);
    insert(&root, 15);

    printf("Inorder traversal of threaded binary tree: ");
    inorder(root);
    printf("\n");
    return 0;
}
