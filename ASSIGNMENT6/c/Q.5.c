#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

#define MAX 100

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

// Function to evaluate a postfix expression
int evaluatePostfix(char *postfix) {
    Stack s;
    initialize(&s);

    for (int i = 0; postfix[i] != '\0'; i++) {
        char ch = postfix[i];

        // If the character is a digit, convert it to integer and push onto the stack
        if (isdigit(ch)) {
            push(&s, ch - '0');  // Convert character to integer
        }
        // If the character is an operator, pop two elements from the stack and perform the operation
        else {
            int operand2 = pop(&s);
            int operand1 = pop(&s);

            switch (ch) {
                case '+':
                    push(&s, operand1 + operand2);
                    break;
                case '-':
                    push(&s, operand1 - operand2);
                    break;
                case '*':
                    push(&s, operand1 * operand2);
                    break;
                case '/':
                    if (operand2 != 0) {
                        push(&s, operand1 / operand2);
                    } else {
                        printf("Error: Division by zero!\n");
                        return -1;
                    }
                    break;
                default:
                    printf("Error: Unknown operator '%c'\n", ch);
                    return -1;
            }
        }
    }

    // The final result of the postfix expression is at the top of the stack
    return pop(&s);
}

// Main function to test the postfix evaluation
int main() {
    char postfix[MAX];

    // Prompt user to enter a postfix expression
    printf("Enter a postfix expression: ");
    fgets(postfix, sizeof(postfix), stdin);

    // Remove newline character if present
    postfix[strcspn(postfix, "\n")] = '\0';

    int result = evaluatePostfix(postfix);

    printf("Result of the postfix expression: %d\n", result);

    return 0;
}
