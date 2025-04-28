# def sum(a, b):
#     return a+b
# print(sum(1,3))

#10,12,123
# x = input()
# li = x.split(',')
# ans = 0
# for val in li:
#     ans+= (int(val))
# print(ans)

# li = [i for i in range(1, 5)]
# print(li)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["brand2"] = "23"
# print(thisdict)
# thisdict.pop("model")
# print(thisdict)


# set1 = {"abc", 34, True, 40, "male", 40}
# print(len(set1))

# thislist = ["apple", "cherry", "orange", "apple", "mango"]
# thislist.insert(1,"apple222")
# print(thislist)

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:4] = ["a","blackcurrant", "watermelon"]
# print(thislist)


# tup = ("apple", "singara")
# print(tup)

# thistuple = "apple", "banana", "cherry", "apple", "cherry"
# print(type(thistuple))
# print(thistuple[4])


# x = lambda val : val + val + val
# print(x(2))


# numbers = [1, 2, 3, 4, 5]
# squared = list(map(lambda x: x * x, numbers))
# print(squared)  # [1, 4, 9, 16, 25]

# import heapq
# heap = [1, 3, 5, 7, 9, 2]
# heapq.heappush(heap, 4)  # Adds 4 while maintaining the heap property
# print(heap)


# mat = []
# for i in range(8):
#     r = []
#     for j in range(8):
#         r.append(i)
#     mat.append(r)

# # print(mat)

# for i in range(8):
#     r = []
#     for j in range(8):
#         if(mat[i][j] == 7):
#             print("OK")

# ----------------------------------------------------------------------------------------- #

# UCS 


# from queue import PriorityQueue
# def ucs(start, goal, g):
#     visit = set()
#     pq = PriorityQueue()
#     pq.put((0, start))
#     while not pq.empty():
#         cost, node = pq.get()
#         if node in visit:
#             continue
#         print( node, end=" ")
#         visit.add(node)

#         if( node == goal ):
#             return "FOUND"

#         for n, c in g[node]:
#             if n not in visit:
#                 pq.put((c, n))


# graph = {
#     'A': [('B', 3), ('C', 2)],
#     'B': [('A', 5), ('C', 2), ('D', 2), ('E', 3)],
#     'C': [('A', 5), ('B', 3), ('F', 2), ('G', 4)],
#     'D': [('H', 1), ('I', 99)],
#     'F': [('J', 99)],
#     'G': [('K', 99), ('L', 3)]
# }

# ucs('A', 'H', graph)




# hillClimbing
import random

class chess:
    def __init__(self):
        self.board = [random.randint(0,7) for _ in range(8)]
    main_board = []
    def print_board(self):
        for i in range(8):
            line = []
            for j in range(8):
                if( self.board[i] == j):
                    line.append('Q')
                else:
                    line.append('.')
            self.main_board.append(line)
        
    def calc(self, board):
        # Calculate the number of conflicts (queens attacking each other) for a given board state.
        conflicts = 0
        for row1 in range(8):
            for row2 in range(row1 + 1, 8):
                if board[row1] == board[row2]:  # Same column
                    conflicts += 1
                if abs(board[row1] - board[row2]) == abs(row1 - row2):  # Same diagonal
                    conflicts += 1
        return conflicts
    
    def hill_climb(self):
        curr = self.calc(self.board)
        print(curr)

        while(True):
            for row in range(0, 8):
                oc = self.board[row]
                for col in range(8):
                    if( col != oc):
                        nb = self.board[:]
                        nb[row] = col
                        new_conflicts = 0
                        if new_conflicts < curr:  # If we find a better board
                            self.board = nb  # Accept the new board
                            current_conflicts = new_conflicts  # Update current conflicts
                            found_better = True  # Set the flag to true
                            break  # Move on without checking further neighbors

                if found_better:
                    break  # Move to the next iteration with the new board

            if not found_better:  # If no better neighbor was found, we are stuck
                break

        return current_conflicts == 0  # Return True 
    

cs = chess()
print(cs.board)
cs.print_board()
# print(cs.main_board.split(','))

for row in cs.main_board:
    print(' '.join(row))

cs.hill_climb()

