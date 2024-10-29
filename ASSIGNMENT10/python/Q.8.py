class Graph:
    def __init__(self, vertices):
        self.vertices = vertices  # Number of vertices
        self.adjacency_list = [[] for _ in range(vertices)]  # Initialize adjacency list

    def add_edge(self, u, v):
        # Add edge from u to v (for undirected graph, add v to u's list as well)
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)  # Uncomment this line for undirected graph

    def print_graph(self):
        for i in range(self.vertices):
            print(f"Vertex {i}: ", end="")
            print(" -> ".join(map(str, self.adjacency_list[i])))

# Example Usage
if __name__ == "__main__":
    # Create a graph with 5 vertices (0 to 4)
    g = Graph(5)
    
    # Add edges
    g.add_edge(0, 1)
    g.add_edge(0, 4)
    g.add_edge(1, 4)
    g.add_edge(1, 3)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)

    # Print the adjacency list
    print("Adjacency List of the Graph:")
    g.print_graph()
