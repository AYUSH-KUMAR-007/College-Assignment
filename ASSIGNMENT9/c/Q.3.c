#include <stdio.h>

void printAllSubarraysWithZeroSum(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        int sum = 0;
        for (int j = i; j < n; j++) {
            sum += arr[j];
            if (sum == 0) {
                printf("Subarray found from index %d to %d\n", i, j);
            }
        }
    }
}

int main() {
    int arr[] = {3, 4, -7, 3, 1, 3, 1, -4, -2, -2};
    int n = sizeof(arr) / sizeof(arr[0]);
    printAllSubarraysWithZeroSum(arr, n);
    return 0;
}
