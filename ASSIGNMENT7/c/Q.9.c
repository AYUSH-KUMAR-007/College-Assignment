#include <stdio.h>
#include <stdlib.h>

struct Queue {
    int* arr;
    int front, rear, size, capacity;
};

struct Queue* createQueue(int capacity) {
    struct Queue* queue = (struct Queue*)malloc(sizeof(struct Queue));
    queue->capacity = capacity;
    queue->front = queue->size = 0;
    queue->rear = capacity - 1;
    queue->arr = (int*)malloc(queue->capacity * sizeof(int));
    return queue;
}

int isFull(struct Queue* queue) {
    return (queue->size == queue->capacity);
}

int isEmpty(struct Queue* queue) {
    return (queue->size == 0);
}

void enqueue(struct Queue* queue, int item) {
    if (isFull(queue)) return;
    queue->rear = (queue->rear + 1) % queue->capacity;
    queue->arr[queue->rear] = item;
    queue->size++;
}

int dequeue(struct Queue* queue) {
    if (isEmpty(queue)) return -1;
    int item = queue->arr[queue->front];
    queue->front = (queue->front + 1) % queue->capacity;
    queue->size--;
    return item;
}

void reverseQueue(struct Queue* queue) {
    if (!isEmpty(queue)) {
        int item = dequeue(queue);
        reverseQueue(queue);
        enqueue(queue, item);
    }
}

void display(struct Queue* queue) {
    if (isEmpty(queue)) {
        printf("Queue is empty\n");
        return;
    }
    printf("Queue elements: ");
    for (int i = queue->front; i < queue->size + queue->front; i++) {
        printf("%d ", queue->arr[i % queue->capacity]);
    }
    printf("\n");
}

int main() {
    struct Queue* queue = createQueue(5);
    enqueue(queue, 10);
    enqueue(queue, 20);
    enqueue(queue, 30);
    printf("Original Queue: ");
    display(queue);
    reverseQueue(queue);
    printf("Reversed Queue: ");
    display(queue);
    return 0;
}
