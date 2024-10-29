#include <stdio.h>

void findTriplet(int arr[], int n, int K) {
    for (int i = 0; i < n - 2; i++) {
        for (int j = i + 1; j < n - 1; j++) {
            for (int k = j + 1; k < n; k++) {
                if (arr[i] + arr[j] + arr[k] == K) {
                    printf("Triplet: %d, %d, %d\n", arr[i], arr[j], arr[k]);
                    return;
                }
            }
        }
    }
    printf("No triplet found\n");
}

int main() {
    int arr[] = {1, 4, 45, 6, 10, 8};
    int K = 22;
    int n = sizeof(arr) / sizeof(arr[0]);

    findTriplet(arr, n, K);
    return 0;
}
