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

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()  # Set to keep track of visited nodes
        visited.add(start)  # Mark the current node as visited
        dfs_order = [start]  # List to store the DFS traversal order

        # Recur for all the vertices adjacent to this vertex
        for neighbor in self.adjacency_list.get(start, []):
            if neighbor not in visited:
                dfs_order.extend(self.dfs(neighbor, visited))

        return dfs_order

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
    
    # Perform DFS starting from vertex 0
    dfs_result = g.dfs(0)

    # Print the result of DFS
    print("DFS Traversal starting from vertex 0:", dfs_result)
