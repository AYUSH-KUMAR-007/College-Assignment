#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

struct Node* front = NULL;
struct Node* rear = NULL;

void enqueue(int item) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = item;
    newNode->next = NULL;
    if (rear == NULL) {
        front = rear = newNode;
    } else {
        rear->next = newNode;
        rear = newNode;
    }
}

void dequeue() {
    if (front == NULL) {
        printf("Queue is empty\n");
    } else {
        struct Node* temp = front;
        printf("Dequeued: %d\n", front->data);
        front = front->next;
        free(temp);
        if (front == NULL) {
            rear = NULL;
        }
    }
}

void display() {
    struct Node* temp = front;
    if (temp == NULL) {
        printf("Queue is empty\n");
    } else {
        printf("Queue elements: ");
        while (temp != NULL) {
            printf("%d ", temp->data);
            temp = temp->next;
        }
        printf("\n");
    }
}

int main() {
    enqueue(10);
    enqueue(20);
    enqueue(30);
    dequeue();
    display();
    return 0;
}
