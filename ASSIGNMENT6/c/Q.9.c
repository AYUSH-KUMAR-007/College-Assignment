#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 100  // Maximum size of the stack

// Stack structure definition
typedef struct {
    char items[MAX];
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
void push(Stack *s, char value) {
    if (isFull(s)) {
        printf("Stack overflow!\n");
    } else {
        s->items[++(s->top)] = value;
    }
}

// Function to pop an element from the stack
char pop(Stack *s) {
    if (isEmpty(s)) {
        printf("Stack underflow!\n");
        return '\0';  // Returning null character to indicate error
    } else {
        return s->items[(s->top)--];
    }
}

// Function to reverse a string using stack
void reverseString(char *str) {
    Stack s;
    initialize(&s);
    int length = strlen(str);

    // Push all characters of the string onto the stack
    for (int i = 0; i < length; i++) {
        push(&s, str[i]);
    }

    // Pop all characters from the stack and overwrite the original string
    for (int i = 0; i < length; i++) {
        str[i] = pop(&s);
    }
}

// Main function to test string reversal
int main() {
    char str[MAX];

    // Prompt user to enter a string
    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);

    // Remove newline character if present
    str[strcspn(str, "\n")] = '\0';

    // Reverse the string
    reverseString(str);

    // Print the reversed string
    printf("Reversed string: %s\n", str);

    return 0;
}
