#include <stdio.h>

int checkSubarrayWithZeroSum(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        int sum = 0;
        for (int j = i; j < n; j++) {
            sum += arr[j];
            if (sum == 0) {
                return 1;
            }
        }
    }
    return 0;
}

int main() {
    int arr[] = {4, 2, -3, 1, 6};
    int n = sizeof(arr) / sizeof(arr[0]);
    if (checkSubarrayWithZeroSum(arr, n)) {
        printf("Subarray with 0 sum exists\n");
    } else {
        printf("No subarray with 0 sum\n");
    }
    return 0;
}
