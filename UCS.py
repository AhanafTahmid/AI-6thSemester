#https://www.youtube.com/watch?v=rHUWHx-5Hao

from queue import PriorityQueue

def ucs(start, goal, graph):
    visit = set()  # To keep track of visited nodes
    pq = PriorityQueue()  # Priority Queue to process nodes by minimum cost
    pq.put((0, start, []))  # (cost, node, path)

    while not pq.empty():
        cost, node, path = pq.get()  # Get node with the lowest accumulated cost

        if node in visit:
            continue  # Skip if the node has already been visited

        path = path + [node]  # Add the current node to the path
        visit.add(node)  # Mark the node as visited

        print(node, end=" ")  # Print the node as you visit it

        if node == goal:
            print("\nGoal Reached!")
            print("Path:", path)
            print("Total Cost:", cost)
            return

        # Process neighbors of the current node
        for neighbor, edge_cost in graph.get(node, []):
            if neighbor not in visit:
                total_cost = cost + edge_cost  # Accumulate the cost
                pq.put((total_cost, neighbor, path))  # Put the neighbor in the queue with its cost

    print("\nGoal not reachable!")
    return "NOT FOUND"


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

ucs(start, goal, graph)