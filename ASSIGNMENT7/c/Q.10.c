#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void generateBinaryNumbers(int n) {
    char** arr = (char**)malloc(n * sizeof(char*));
    for (int i = 0; i < n; i++) {
        arr[i] = (char*)malloc(32 * sizeof(char)); // Allocate space for binary representation
    }

    arr[0] = "1"; // Start from 1

    for (int i = 1; i < n; i++) {
        sprintf(arr[i], "%s0", arr[i - 1]); // Append 0 to previous number
        strcpy(arr[i + 1], arr[i - 1]); // Copy previous number
        arr[i + 1][strlen(arr[i + 1]) - 1] = '1'; // Change last digit to 1
        i++; // Increment to skip the newly added binary number
    }

    printf("Binary numbers from 1 to %d:\n", n);
    for (int i = 0; i < n; i++) {
        printf("%s\n", arr[i]);
    }

    for (int i = 0; i < n; i++) {
        free(arr[i]); // Free memory for each binary number
    }
    free(arr); // Free the array of pointers
}

int main() {
    int n = 5; // Change this number to generate more binary numbers
    generateBinaryNumbers(n);
    return 0;
}
