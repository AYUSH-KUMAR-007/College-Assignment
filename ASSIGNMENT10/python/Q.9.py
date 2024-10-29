from collections import deque

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, u, v):
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)  # Uncomment this line for undirected graph

    def bfs(self, start):
        visited = set()      # Set to keep track of visited nodes
        queue = deque([start])  # Initialize the queue with the starting node
        bfs_order = []      # List to store the BFS traversal order

        while queue:
            vertex = queue.popleft()  # Dequeue a vertex from the queue
            if vertex not in visited:
                visited.add(vertex)   # Mark the vertex as visited
                bfs_order.append(vertex)  # Add it to the BFS order

                # Add all unvisited neighbors to the queue
                for neighbor in self.adjacency_list.get(vertex, []):
                    if neighbor not in visited:
                        queue.append(neighbor)

        return bfs_order

# Example Usage
if __name__ == "__main__":
    g = Graph()
    
    # Adding edges
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 5)
    g.add_edge(2, 6)
    
    # Perform BFS starting from vertex 0
    bfs_result = g.bfs(0)

    # Print the result of BFS
    print("BFS Traversal starting from vertex 0:", bfs_result)
