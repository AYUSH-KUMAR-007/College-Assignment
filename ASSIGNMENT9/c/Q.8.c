#include <stdio.h>

void groupByFirstOccurrence(int arr[], int n) {
    int seen[100] = {0};

    for (int i = 0; i < n; i++) {
        if (seen[arr[i]] == 0) {
            for (int j = 0; j < n; j++) {
                if (arr[j] == arr[i]) {
                    printf("%d ", arr[j]);
                }
            }
            seen[arr[i]] = 1;
        }
    }
    printf("\n");
}

int main() {
    int arr[] = {4, 5, 6, 4, 5, 3};
    int n = sizeof(arr) / sizeof(arr[0]);
    groupByFirstOccurrence(arr, n);
    return 0;
}
