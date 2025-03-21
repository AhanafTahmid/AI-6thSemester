from queue import PriorityQueue

def best_first_search(start, goal, graph):
    visited = set()
    pq = PriorityQueue()
    pq.put((0, start))  # (priority, node)
    while not pq.empty():
        cost, node = pq.get() #getout/ dequeing
        if node in visited:
            continue

        print(node, end=" ") # Print the path
        visited.add(node)

        if node == goal:
            print("\nGoal Reached!")
            return

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                pq.put((weight, neighbor))  # Priority Queue orders by weight

    print("\nGoal not reachable!")

# Graph Representation (Adjacency List)
graph = {
    'A': [('B', 3), ('C', 2)],
    'B': [('A', 5), ('C', 2), ('D', 2), ('E', 3)],
    'C': [('A', 5), ('B', 3), ('F', 2), ('G', 4)],
    'D': [('H', 1), ('I', 99)],
    'F': [('J', 99)],
    'G': [('K', 99), ('L', 3)]
}

start = 'A'
goal = 'H'
best_first_search(start, goal, graph)
