import heapq

class Graph:
    def __init__(self):
        self.graph = {}  # Adjacency list

    def add_edge(self, node, neighbor, cost):
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append((neighbor, cost))

    def a_star(self, start, goal, heuristic):
        # Priority queue for A* (min-heap)
        pq = []
        heapq.heappush(pq, (0, start))  # (f(n), node)
        
        g_costs = {start: 0}  # g(n) values
        came_from = {start: None}  # To track path

        while pq:
            current_f, current_node = heapq.heappop(pq)

            if current_node == goal:
                return self.reconstruct_path(came_from, start, goal)

            for neighbor, cost in self.graph.get(current_node, []):
                new_g = g_costs[current_node] + cost  # Calculate g(n)

                if neighbor not in g_costs or new_g < g_costs[neighbor]:
                    g_costs[neighbor] = new_g
                    f_cost = new_g + heuristic[neighbor]  # f(n) = g(n) + h(n)
                    heapq.heappush(pq, (f_cost, neighbor))
                    came_from[neighbor] = current_node

        return None  # No path found

    def reconstruct_path(self, came_from, start, goal):
        path = []
        node = goal
        while node:
            path.append(node)
            node = came_from[node]
        return path[::-1]  # Reverse the path

# Example usage
graph = Graph()
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 4)
graph.add_edge('B', 'D', 2)
graph.add_edge('C', 'D', 1)
graph.add_edge('B', 'E', 5)
graph.add_edge('D', 'E', 3)

# Heuristic values (assume an estimate to goal 'E')
heuristic = {
    'A': 6, 'B': 3, 'C': 4, 'D': 2, 'E': 0
}

start, goal = 'A', 'E'
path = graph.a_star(start, goal, heuristic)
print("Shortest path:", path)
