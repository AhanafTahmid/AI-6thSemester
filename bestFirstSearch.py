from queue import PriorityQueue

def best_first_search(start, goal, graph, heuristic):
    visited = set()
    pq = PriorityQueue()
    pq.put((heuristic[start], start))  # Using heuristic as priority

    while not pq.empty():
        h_val, node = pq.get()

        if node in visited:
            continue

        print(node, end=" ")  # Print the path
        visited.add(node)

        if node == goal:
            print("\nGoal Reached!")
            return

        for neighbor, _ in graph.get(node, []):
            if neighbor not in visited:
                pq.put((heuristic[neighbor], neighbor))  # Use heuristic only

    print("\nGoal not reachable!")

start = 'A'
goal = 'G'

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5), ('G', 2)],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

heuristic = {
    'A': 5,
    'B': 4,
    'C': 2,
    'D': 6,
    'E': 3,
    'F': 5,
    'G': 0
}

best_first_search(start, goal, graph, heuristic)