#include <stdio.h>

void findPairsWithDifference(int arr[], int n, int diff) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (abs(arr[i] - arr[j]) == diff) {
                printf("Pair found (%d, %d)\n", arr[i], arr[j]);
            }
        }
    }
}

int main() {
    int arr[] = {1, 5, 3, 4, 2};
    int diff = 2;
    int n = sizeof(arr) / sizeof(arr[0]);
    findPairsWithDifference(arr, n, diff);
    return 0;
}
