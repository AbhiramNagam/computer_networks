import sys
import matplotlib.pyplot as plt
import networkx as nx

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def print_table(self, dist, src, time):
        print(f"Time {time} - Node \t Distance from Source")
        for node in range(self.V):
            print(f"{chr(97 + node)} \t {dist[node]}")

    def bellman_ford(self, src, dest):
        dist = [sys.maxsize] * self.V
        dist[src] = 0

        t = 0
        self.print_table(dist, src, time=t)

        for _ in range(self.V - 1):
            t += 1
            print(f"\nIteration {t}:")
            for u in range(self.V):
                for v in range(self.V):
                    if self.graph[u][v] != 0 and dist[u] + self.graph[u][v] < dist[v]:
                        dist[v] = dist[u] + self.graph[u][v]
            self.print_table(dist, src, time=t)

        shortest_distance = dist[dest]
        print(f"\nThe shortest distance from node {chr(97 + src)} to node {chr(97 + dest)} is {shortest_distance}")

        # Create the graph
        shortest_path_graph = nx.Graph()
        for i in range(self.V):
            for j in range(self.V):
                if self.graph[i][j] > 0:
                    shortest_path_graph.add_edge(chr(97 + i), chr(97 + j), weight=self.graph[i][j])

        # Find shortest path
        shortest_path = nx.shortest_path(shortest_path_graph, source=chr(97 + src), target=chr(97 + dest), weight='weight')
        shortest_path_edges = list(zip(shortest_path, shortest_path[1:]))
        edge_labels = {(u, v): shortest_path_graph[u][v]['weight'] for u, v in shortest_path_edges}

        # Draw the graph
        pos = nx.spring_layout(shortest_path_graph)
        nx.draw(shortest_path_graph, pos, with_labels=True, node_color='skyblue', node_size=1500)
        nx.draw_networkx_edge_labels(shortest_path_graph, pos, edge_labels=edge_labels, font_color='red')
        plt.title("Shortest Path Graph with Weights")
        plt.show()

# Test the code
if __name__ == "__main__":
    g = Graph(7)
    g.graph = [
        [0, 3, 3, 0, 0, 0, 2],
        [3, 0, 4, 3, 8, 0, 4],
        [3, 4, 0, 6, 0, 0, 0],
        [0, 3, 6, 0, 6, 8, 0],
        [0, 8, 0, 6, 0, 12, 7],
        [0, 0, 0, 8, 12, 0, 0],
        [2, 4, 0, 0, 7, 0, 0]
    ]

    source = 3
    destination = 4
    g.bellman_ford(source, destination)