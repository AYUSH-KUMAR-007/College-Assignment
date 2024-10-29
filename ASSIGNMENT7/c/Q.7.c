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

struct Stack {
    struct Queue* q1;
    struct Queue* q2;
};

struct Stack* createStack(int capacity) {
    struct Stack* stack = (struct Stack*)malloc(sizeof(struct Stack));
    stack->q1 = createQueue(capacity);
    stack->q2 = createQueue(capacity);
    return stack;
}

void push(struct Stack* stack, int item) {
    enqueue(stack->q2, item);
    while (!isEmpty(stack->q1)) {
        enqueue(stack->q2, dequeue(stack->q1));
    }
    struct Queue* temp = stack->q1;
    stack->q1 = stack->q2;
    stack->q2 = temp;
}

int pop(struct Stack* stack) {
    return dequeue(stack->q1);
}

void display(struct Stack* stack) {
    if (isEmpty(stack->q1)) {
        printf("Stack is empty\n");
        return;
    }
    printf("Stack elements: ");
    for (int i = stack->q1->front; i < stack->q1->size + stack->q1->front; i++) {
        printf("%d ", stack->q1->arr[i % stack->q1->capacity]);
    }
    printf("\n");
}

int main() {
    struct Stack* stack = createStack(5);
    push(stack, 10);
    push(stack, 20);
    push(stack, 30);
    printf("Popped: %d\n", pop(stack));
    display(stack);
    return 0;
}
