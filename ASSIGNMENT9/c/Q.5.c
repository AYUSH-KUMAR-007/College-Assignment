#include <stdio.h>

void maxLengthEqualZeroOne(int arr[], int n) {
    int maxLength = 0;
    int start = -1, end = -1;

    for (int i = 0; i < n; i++) {
        int count0 = 0, count1 = 0;
        for (int j = i; j < n; j++) {
            if (arr[j] == 0)
                count0++;
            else
                count1++;

            if (count0 == count1 && (j - i + 1) > maxLength) {
                maxLength = j - i + 1;
                start = i;
                end = j;
            }
        }
    }

    if (start != -1) {
        printf("Subarray with equal 0’s and 1’s is from index %d to %d\n", start, end);
    } else {
        printf("No subarray with equal 0’s and 1’s\n");
    }
}

int main() {
    int arr[] = {0, 0, 1, 0, 1, 1, 0};
    int n = sizeof(arr) / sizeof(arr[0]);
    maxLengthEqualZeroOne(arr, n);
    return 0;
}
