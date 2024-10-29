#include <stdio.h>

// Standard Recursive Function to Calculate Factorial
int factorialRecursive(int n) {
    if (n == 0 || n == 1) {
        return 1;
    } else {
        return n * factorialRecursive(n - 1);
    }
}

// Tail-Recursive Function to Calculate Factorial
int factorialTailRecursive(int n, int accumulator) {
    if (n == 0 || n == 1) {
        return accumulator;
    } else {
        return factorialTailRecursive(n - 1, n * accumulator);
    }
}

// Helper function to call the tail-recursive version with an initial accumulator
int factorialTail(int n) {
    return factorialTailRecursive(n, 1);  // Initial accumulator value is 1
}

// Main function to test both versions of the factorial function
int main() {
    int number;

    // Prompt user to enter a number
    printf("Enter a number to find its factorial: ");
    scanf("%d", &number);

    // Calculate factorial using the standard recursive function
    int resultRecursive = factorialRecursive(number);
    printf("Factorial (Recursive) of %d is: %d\n", number, resultRecursive);

    // Calculate factorial using the tail-recursive function
    int resultTailRecursive = factorialTail(number);
    printf("Factorial (Tail-Recursive) of %d is: %d\n", number, resultTailRecursive);

    return 0;
}
