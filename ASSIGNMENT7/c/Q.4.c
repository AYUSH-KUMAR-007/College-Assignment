#include <stdio.h>
#define MAX 10

int array[MAX];
int front1 = -1, rear1 = -1;
int front2 = MAX, rear2 = MAX;

void enqueue1(int item) {
    if (rear1 + 1 == rear2) {
        printf("Queue 1 is full\n");
    } else {
        if (front1 == -1)
            front1 = 0;
        array[++rear1] = item;
    }
}

void enqueue2(int item) {
    if (rear1 + 1 == rear2) {
        printf("Queue 2 is full\n");
    } else {
        if (front2 == MAX)
            front2 = MAX - 1;
        array[--rear2] = item;
    }
}

void dequeue1() {
    if (front1 == -1 || front1 > rear1) {
        printf("Queue 1 is empty\n");
    } else {
        printf("Dequeued from Queue 1: %d\n", array[front1++]);
    }
}

void dequeue2() {
    if (front2 == MAX || front2 < rear2) {
        printf("Queue 2 is empty\n");
    } else {
        printf("Dequeued from Queue 2: %d\n", array[front2--]);
    }
}

void display() {
    printf("Queue 1: ");
    for (int i = front1; i <= rear1; i++) {
        printf("%d ", array[i]);
    }
    printf("\nQueue 2: ");
    for (int i = front2; i >= rear2; i--) {
        printf("%d ", array[i]);
    }
    printf("\n");
}

int main() {
    enqueue1(10);
    enqueue1(20);
    enqueue2(30);
    dequeue1();
    display();
    return 0;
}
