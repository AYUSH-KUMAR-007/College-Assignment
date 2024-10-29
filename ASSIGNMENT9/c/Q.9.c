#include <stdio.h>

int findMinIndexRepeating(int arr[], int n) {
    int minIndex = n;
    int index[100] = {0};

    for (int i = 0; i < n; i++) {
        if (index[arr[i]] != 0) {
            if (index[arr[i]] - 1 < minIndex) {
                minIndex = index[arr[i]] - 1;
            }
        } else {
            index[arr[i]] = i + 1;
        }
    }

    return (minIndex == n) ? -1 : minIndex;
}

int main() {
    int arr[] = {4, 5, 6, 4, 5, 3};
    int n = sizeof(arr) / sizeof(arr[0]);
    int minIndex = findMinIndexRepeating(arr, n);
    if (minIndex != -1) {
        printf("Minimum index of repeating element is %d\n", minIndex);
    } else {
        printf("No repeating elements found\n");
    }
    return 0;
}
