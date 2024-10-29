#include <stdio.h>
#include <stdlib.h>

#define MAX 100  // Total size of the array
#define STACK_COUNT 3  // Number of stacks

// Structure to represent multiple stacks
typedef struct {
    int arr[MAX];           // Array to store stack elements
    int top[STACK_COUNT];   // Array to track top elements of each stack
    int size;               // Size of each stack
} MultiStack;

// Function to initialize the multi-stack
void initialize(MultiStack *ms, int size) {
    ms->size = size;
    for (int i = 0; i < STACK_COUNT; i++) {
        ms->top[i] = -1;  // Initialize tops to -1 (indicating empty stacks)
    }
}

// Function to push an element onto a specific stack
void push(MultiStack *ms, int stackNum, int value) {
    if (stackNum < 0 || stackNum >= STACK_COUNT) {
        printf("Invalid stack number!\n");
        return;
    }
    
    if (ms->top[stackNum] + 1 >= ms->size) {
        printf("Stack %d overflow!\n", stackNum);
        return;
    }

    // Calculate actual position in the array
    int pos = stackNum * ms->size + (++ms->top[stackNum]);
    ms->arr[pos] = value;
    printf("Pushed %d onto stack %d\n", value, stackNum);
}

// Function to pop an element from a specific stack
int pop(MultiStack *ms, int stackNum) {
    if (stackNum < 0 || stackNum >= STACK_COUNT) {
        printf("Invalid stack number!\n");
        return -1;  // Return -1 to indicate an error
    }

    if (ms->top[stackNum] == -1) {
        printf("Stack %d underflow!\n", stackNum);
        return -1;  // Return -1 to indicate an error
    }

    // Calculate actual position in the array
    int pos = stackNum * ms->size + (ms->top[stackNum]--);
    return ms->arr[pos];
}

// Function to display the contents of a specific stack
void displayStack(MultiStack *ms, int stackNum) {
    if (stackNum < 0 || stackNum >= STACK_COUNT) {
        printf("Invalid stack number!\n");
        return;
    }

    printf("Stack %d: ", stackNum);
    for (int i = 0; i <= ms->top[stackNum]; i++) {
        printf("%d ", ms->arr[stackNum * ms->size + i]);
    }
    printf("\n");
}

// Main function to test the multiple stacks implementation
int main() {
    MultiStack ms;
    initialize(&ms, MAX / STACK_COUNT);  // Initialize with equal size for each stack

    // Push elements onto different stacks
    push(&ms, 0, 10);
    push(&ms, 0, 20);
    push(&ms, 1, 30);
    push(&ms, 1, 40);
    push(&ms, 2, 50);

    // Display stacks
    displayStack(&ms, 0);
    displayStack(&ms, 1);
    displayStack(&ms, 2);

    // Pop elements from stacks
    printf("Popped from stack 0: %d\n", pop(&ms, 0));
    printf("Popped from stack 1: %d\n", pop(&ms, 1));

    // Display stacks after popping
    displayStack(&ms, 0);
    displayStack(&ms, 1);
    displayStack(&ms, 2);

    return 0;
}
