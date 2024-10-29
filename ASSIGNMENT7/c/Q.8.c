#include <stdio.h>
#include <stdlib.h>

struct Stack {
    int* arr;
    int top;
    int capacity;
};

struct Stack* createStack(int capacity) {
    struct Stack* stack = (struct Stack*)malloc(sizeof(struct Stack));
    stack->capacity = capacity;
    stack->top = -1;
    stack->arr = (int*)malloc(stack->capacity * sizeof(int));
    return stack;
}

int isFull(struct Stack* stack) {
    return stack->top == stack->capacity - 1;
}

int isEmpty(struct Stack* stack) {
    return stack->top == -1;
}

void push(struct Stack* stack, int item) {
    if (isFull(stack)) return;
    stack->arr[++stack->top] = item;
}

int pop(struct Stack* stack) {
    if (isEmpty(stack)) return -1;
    return stack->arr[stack->top--];
}

struct Queue {
    struct Stack* s1;
    struct Stack* s2;
};

struct Queue* createQueue(int capacity) {
    struct Queue* queue = (struct Queue*)malloc(sizeof(struct Queue));
    queue->s1 = createStack(capacity);
    queue->s2 = createStack(capacity);
    return queue;
}

void enqueue(struct Queue* queue, int item) {
    push(queue->s1, item);
}

int dequeue(struct Queue* queue) {
    if (isEmpty(queue->s2)) {
        while (!isEmpty(queue->s1)) {
            push(queue->s2, pop(queue->s1));
        }
    }
    return pop(queue->s2);
}

void display(struct Queue* queue) {
    if (isEmpty(queue->s1) && isEmpty(queue->s2)) {
        printf("Queue is empty\n");
        return;
    }
    printf("Queue elements: ");
    for (int i = 0; i <= queue->s1->top; i++) {
        printf("%d ", queue->s1->arr[i]);
    }
    for (int i = 0; i <= queue->s2->top; i++) {
        printf("%d ", queue->s2->arr[i]);
    }
    printf("\n");
}

int main() {
    struct Queue* queue = createQueue(5);
    enqueue(queue, 10);
    enqueue(queue, 20);
    enqueue(queue, 30);
    printf("Dequeued: %d\n", dequeue(queue));
    display(queue);
    return 0;
}
