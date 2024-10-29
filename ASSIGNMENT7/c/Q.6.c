#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    int priority;
    struct Node* next;
};

struct Node* front = NULL;

void enqueue(int item, int priority) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = item;
    newNode->priority = priority;
    newNode->next = NULL;

    if (front == NULL || priority < front->priority) {
        newNode->next = front;
        front = newNode;
    } else {
        struct Node* temp = front;
        while (temp->next != NULL && temp->next->priority <= priority) {
            temp = temp->next;
        }
        newNode->next = temp->next;
        temp->next = newNode;
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
    }
}

void display() {
    struct Node* temp = front;
    if (temp == NULL) {
        printf("Queue is empty\n");
    } else {
        printf("Priority Queue elements: ");
        while (temp != NULL) {
            printf("%d(%d) ", temp->data, temp->priority);
            temp = temp->next;
        }
        printf("\n");
    }
}

int main() {
    enqueue(10, 2);
    enqueue(20, 1);
    enqueue(30, 3);
    dequeue();
    display();
    return 0;
}
