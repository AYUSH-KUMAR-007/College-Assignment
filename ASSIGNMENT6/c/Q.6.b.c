#include <stdio.h>

// Standard Recursive Function to Calculate Fibonacci Series
int fibonacciRecursive(int n) {
    if (n == 0) {
        return 0;
    } else if (n == 1) {
        return 1;
    } else {
        return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2);
    }
}

// Tail-Recursive Function to Calculate Fibonacci Series
int fibonacciTailRecursive(int n, int a, int b) {
    if (n == 0) {
        return a;
    } else if (n == 1) {
        return b;
    } else {
        return fibonacciTailRecursive(n - 1, b, a + b);
    }
}

// Helper function to call the tail-recursive version with initial values
int fibonacciTail(int n) {
    return fibonacciTailRecursive(n, 0, 1);  // Starting values for Fibonacci series
}

// Main function to test both versions of the Fibonacci function
int main() {
    int number;

    // Prompt user to enter a number
    printf("Enter the number of terms in the Fibonacci series: ");
    scanf("%d", &number);

    // Display Fibonacci series using the standard recursive function
    printf("Fibonacci series (Recursive): ");
    for (int i = 0; i < number; i++) {
        printf("%d ", fibonacciRecursive(i));
    }
    printf("\n");

    // Display Fibonacci series using the tail-recursive function
    printf("Fibonacci series (Tail-Recursive): ");
    for (int i = 0; i < number; i++) {
        printf("%d ", fibonacciTail(i));
    }
    printf("\n");

    return 0;
}
