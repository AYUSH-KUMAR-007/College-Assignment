#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

struct Graph {
    int vertices;
    struct Node** adjLists;
};

struct Node* createNode(int v) {
    struct Node* newNode = malloc(sizeof(struct Node));
    newNode->data = v;
    newNode->next = NULL;
    return newNode;
}

struct Graph* createGraph(int vertices) {
    struct Graph* graph = malloc(sizeof(struct Graph));
    graph->vertices = vertices;

    graph->adjLists = malloc(vertices * sizeof(struct Node*));

    for (int i = 0; i < vertices; i++) {
        graph->adjLists[i] = NULL;
    }

    return graph;
}

void addEdge(struct Graph* graph, int src, int dest) {
    struct Node* newNode = createNode(dest);
    newNode->next = graph->adjLists[src];
    graph->adjLists[src] = newNode;
}

void bfs(struct Graph* graph, int startVertex) {
    int* visited = malloc(graph->vertices * sizeof(int));
    for (int i = 0; i < graph->vertices; i++) {
        visited[i] = 0;
    }

    struct Node* queue = NULL; // Initialize an empty queue

    visited[startVertex] = 1; // Mark the current node as visited
    printf("Visited %d\n", startVertex);

    struct Node* temp = graph->adjLists[startVertex];

    while (temp) {
        int adjVertex = temp->data;
        if (!visited[adjVertex]) {
            visited[adjVertex] = 1; // Mark it as visited
            printf("Visited %d\n", adjVertex);
        }
        temp = temp->next;
    }
}

int main() {
    struct Graph* graph = createGraph(5);
    addEdge(graph, 0, 1);
    addEdge(graph, 0, 4);
    addEdge(graph, 1, 2);
    addEdge(graph, 1, 3);
    addEdge(graph, 1, 4);
    addEdge(graph, 2, 3);
    addEdge(graph, 3, 4);

    printf("Breadth First Search starting from vertex 0:\n");
    bfs(graph, 0);
    return 0;
}
