#https://www.youtube.com/watch?v=rHUWHx-5Hao

import heapq

class Graph:
    def __init__(self):
        self.graph = {}  # Adjacency list

    def add_edge(self, node, neighbor, cost):
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append((neighbor, cost))

    def uniform_cost_search(self, start, goal):
        # Priority queue (min-heap) to store (cost, node, path)
        pq = []
        heapq.heappush(pq, (0, start, []))  # (cost, node, path)

        visited = set()

        while pq:
            cost, current_node, path = heapq.heappop(pq)  # Get the node with the lowest cost

            if current_node in visited:
                continue  # Skip already visited nodes
            
            path = path + [current_node]  # Update path
            visited.add(current_node)  # Mark node as visited

            if current_node == goal:
                return path, cost  # Return the shortest path and cost

            for neighbor, edge_cost in self.graph.get(current_node, []):
                if neighbor not in visited:
                    heapq.heappush(pq, (cost + edge_cost, neighbor, path))

        return None, float('inf')  # No path found

# Example usage
graph = Graph()

graph.add_edge('A', 'B', 80)
graph.add_edge('A', 'C', 99)
graph.add_edge('B', 'D', 97)
graph.add_edge('D', 'G', 101)
graph.add_edge('C', 'G', 211)

start, goal = 'A', 'G'
path, cost = graph.uniform_cost_search(start, goal)
print("Shortest path:", path)
print("Total cost:", cost)
