#include <stdio.h>

int findOddOccurrence(int arr[], int n) {
    int result = 0;
    for (int i = 0; i < n; i++) {
        result ^= arr[i];
    }
    return result;
}

int main() {
    int arr[] = {2, 3, 4, 3, 2, 4, 4};
    int n = sizeof(arr) / sizeof(arr[0]);
    int result = findOddOccurrence(arr, n);

    printf("The number occurring odd times is: %d\n", result);
    return 0;
}
