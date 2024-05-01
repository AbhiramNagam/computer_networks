import sys
import matplotlib.pyplot as plt
import networkx as nx  # Added networkx import

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def min_distance(self, dist, spt_set):
        min_dist = sys.maxsize
        min_index = 0

        for v in range(self.V):
            if dist[v] < min_dist and spt_set[v] == False:
                min_dist = dist[v]
                min_index = v

        return min_index

    def print_table(self, dist, src, time):
        print(f"Time {time} - Node \t Distance from Source")
        for node in range(self.V):
            print(f"{chr(97 + node)} \t {dist[node]}")

    def dijkstra(self, src, dest):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        spt_set = [False] * self.V

        t = 0

        # Display initial distance vector table
        self.print_table(dist, src, time=t)

        for cout in range(self.V):
            u = self.min_distance(dist, spt_set)
            spt_set[u] = True

            # Increment t for each iteration
            t += 1

            # Print computation details
            print(f"\nComputing at Node {chr(97 + u)} (t={t}):")
            for v in range(self.V):
                if self.graph[u][v] > 0 and spt_set[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
                    print(f"Updating distance to Node {chr(97 + v)} from {dist[v] - self.graph[u][v]} to {dist[v]}")

            # Print distance vector table for each iteration
            self.print_table(dist, src, time=t)

        # Create the final graph with shortest path
        shortest_path_graph = nx.Graph()
        for i in range(self.V):
            for j in range(self.V):
                if self.graph[i][j] > 0:
                    shortest_path_graph.add_edge(chr(97 + i), chr(97 + j), weight=self.graph[i][j])

        shortest_path = nx.shortest_path(shortest_path_graph, source=chr(97 + src), target=chr(97 + dest), weight='weight')
        shortest_path_edges = list(zip(shortest_path, shortest_path[1:]))
        edge_labels = {(u, v): shortest_path_graph[u][v]['weight'] for u, v in shortest_path_edges}

        pos = nx.spring_layout(shortest_path_graph)
        nx.draw(shortest_path_graph, pos, with_labels=True, node_color='skyblue', node_size=1500)
        nx.draw_networkx_edge_labels(shortest_path_graph, pos, edge_labels=edge_labels, font_color='red')
        plt.title("Shortest Path Graph with Weights")
        plt.show()

        return dist[dest]

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

    src = 3
    dt = 4
    shortest_distance = g.dijkstra(src, dt)
    print(f"\nThe shortest distance from node {chr(97 + src)} to node {chr(97 + dt)} is {shortest_distance}")