#include <stdio.h>
#include <stdlib.h>

#define MAX 32  // Maximum size of the stack

// Stack structure definition
typedef struct {
    int items[MAX];
    int top;
} Stack;

// Function to initialize the stack
void initialize(Stack *s) {
    s->top = -1;
}

// Function to check if the stack is empty
int isEmpty(Stack *s) {
    return s->top == -1;
}

// Function to check if the stack is full
int isFull(Stack *s) {
    return s->top == MAX - 1;
}

// Function to push an element onto the stack
void push(Stack *s, int value) {
    if (isFull(s)) {
        printf("Stack overflow!\n");
    } else {
        s->items[++(s->top)] = value;
    }
}

// Function to pop an element from the stack
int pop(Stack *s) {
    if (isEmpty(s)) {
        printf("Stack underflow!\n");
        return -1;  // Returning -1 to indicate error
    } else {
        return s->items[(s->top)--];
    }
}

// Function to convert decimal to binary using stack
void decimalToBinary(int decimal) {
    Stack s;
    initialize(&s);

    // Edge case for decimal 0
    if (decimal == 0) {
        printf("Binary representation: 0\n");
        return;
    }

    // Convert decimal to binary
    while (decimal > 0) {
        int remainder = decimal % 2;  // Get remainder
        push(&s, remainder);           // Push remainder onto stack
        decimal /= 2;                  // Update decimal
    }

    // Print binary representation by popping from stack
    printf("Binary representation: ");
    while (!isEmpty(&s)) {
        printf("%d", pop(&s));        // Pop from stack and print
    }
    printf("\n");
}

// Main function to test the decimal to binary conversion
int main() {
    int decimal;

    // Prompt user to enter a decimal number
    printf("Enter a decimal number: ");
    scanf("%d", &decimal);

    // Convert decimal to binary
    decimalToBinary(decimal);

    return 0;
}
