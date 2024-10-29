#include <stdio.h>
#include <stdlib.h>

// Node structure definition for linked list
struct Node {
    int data;
    struct Node* next;
};

// Function to check if the stack is empty
int isEmpty(struct Node* top) {
    return top == NULL;
}

// Function to push an element onto the stack
void push(struct Node** top, int value) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    if (newNode == NULL) {
        printf("Stack overflow! Cannot push %d\n", value);
        return;
    }
    newNode->data = value;
    newNode->next = *top;
    *top = newNode;
    printf("Pushed %d onto the stack\n", value);
}

// Function to pop an element from the stack
int pop(struct Node** top) {
    if (isEmpty(*top)) {
        printf("Stack underflow! Cannot pop\n");
        return -1;  // Returning -1 to indicate error
    }
    struct Node* temp = *top;
    int poppedValue = temp->data;
    *top = (*top)->next;
    free(temp);
    return poppedValue;
}

// Function to peek at the top element of the stack
int peek(struct Node* top) {
    if (isEmpty(top)) {
        printf("Stack is empty! No top element\n");
        return -1;  // Returning -1 to indicate error
    }
    return top->data;
}

// Main function to test the stack implementation
int main() {
    struct Node* stackTop = NULL;  // Initialize an empty stack

    push(&stackTop, 10);
    push(&stackTop, 20);
    push(&stackTop, 30);
    push(&stackTop, 40);

    printf("Top element is %d\n", peek(stackTop));

    printf("Popped element is %d\n", pop(&stackTop));
    printf("Popped element is %d\n", pop(&stackTop));

    push(&stackTop, 50);

    printf("Top element is %d\n", peek(stackTop));

    return 0;
}
