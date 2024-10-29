#include <stdio.h>

void maxLengthSubarrayWithSum(int arr[], int n, int target) {
    int maxLength = 0;
    int start = -1, end = -1;

    for (int i = 0; i < n; i++) {
        int sum = 0;
        for (int j = i; j < n; j++) {
            sum += arr[j];
            if (sum == target && (j - i + 1) > maxLength) {
                maxLength = j - i + 1;
                start = i;
                end = j;
            }
        }
    }

    if (start != -1) {
        printf("Subarray with given sum is from index %d to %d\n", start, end);
    } else {
        printf("No subarray with given sum found\n");
    }
}

int main() {
    int arr[] = {5, 6, -5, 5, 3, 5, 3, -2, 0};
    int sum = 8;
    int n = sizeof(arr) / sizeof(arr[0]);
    maxLengthSubarrayWithSum(arr, n, sum);
    return 0;
}
