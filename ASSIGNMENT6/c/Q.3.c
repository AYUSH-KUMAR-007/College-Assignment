#include <stdio.h>
#include <string.h>

// Function to check if the number of opening and closing parentheses are equal
void checkParenthesisBalance(const char *str) {
    int openCount = 0, closeCount = 0;

    // Traverse the string and count parentheses
    for (int i = 0; i < strlen(str); i++) {
        if (str[i] == '(') {
            openCount++;
        } else if (str[i] == ')') {
            closeCount++;
        }
    }

    // Check if the counts are equal
    if (openCount == closeCount) {
        printf("The number of opening and closing parentheses are equal.\n");
    } else {
        printf("The number of opening and closing parentheses are not equal.\n");
        printf("Opening parentheses: %d, Closing parentheses: %d\n", openCount, closeCount);
    }
}

// Main function to test the parenthesis check
int main() {
    char input[100];

    // Prompt user to enter a string
    printf("Enter a string with parentheses: ");
    fgets(input, sizeof(input), stdin);

    // Remove newline character if present
    input[strcspn(input, "\n")] = '\0';

    // Check if parentheses are balanced
    checkParenthesisBalance(input);

    return 0;
}
