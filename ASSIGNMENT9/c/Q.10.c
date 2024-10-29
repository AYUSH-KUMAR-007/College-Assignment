#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int value;
    int frequency;
    int firstIndex;
} Element;

int compare(const void *a, const void *b) {
    Element *e1 = (Element *)a;
    Element *e2 = (Element *)b;
    if (e1->frequency == e2->frequency)
        return e1->firstIndex - e2->firstIndex;
    return e2->frequency - e1->frequency;
}

void sortByFrequency(int arr[], int n) {
    Element elements[100];
    int count[100] = {0}, index[100] = {-1};

    for (int i = 0; i < n; i++) {
        int val = arr[i];
        count[val]++;
        if (index[val] == -1) {
            index[val] = i;
        }
    }

    int k = 0;
    for (int i = 0; i < 100; i++) {
        if (count[i] > 0) {
            elements[k].value = i;
            elements[k].frequency = count[i];
            elements[k].firstIndex = index[i];
            k++;
        }
    }

    qsort(elements, k, sizeof(Element), compare);

    for (int i = 0; i < k; i++) {
        for (int j = 0; j < elements[i].frequency; j++) {
            printf("%d ", elements[i].value);
        }
    }
    printf("\n");
}

int main() {
    int arr[] = {2, 5, 2, 8, 5, 6, 8, 8};
    int n = sizeof(arr) / sizeof(arr[0]);
    sortByFrequency(arr, n);
    return 0;
}
