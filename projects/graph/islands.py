class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

def get_neighbors(vertex, graph_matrix):
    x = vertex[0]
    y = vertex[1]
    neighbors = []
    #north
    if y > 0 and graph_matrix[y-1][x] == 1:
        neighbors.append((x, y-1))
    #south
    if y < len(graph_matrix) - 1 and graph_matrix[y + 1][x] == 1:
        neighbors.append((x, y+1))
    #east
    if x < len(graph_matrix[0]) -1  and graph_matrix[y][x+1] == 1:
        neighbors.append((x+1, y))
    #west
    if x > 0 and graph_matrix[y][x-1] == 1:
        neighbors.append((x-1, y))

    return neighbors

def dft(x, y, matrix, visited):
    s = Stack()
    s.push((x, y))
    while s.size() > 0:
        v = s.pop()
        y = v[1]
        x = v[0]
        if not visited[y][x]:
            visited[y][x] = True
            for neighbor in get_neighbors((x, y), matrix):
                s.push(neighbor)
    return visited

def island_counter(matrix):
    # created a visited matrix
    visited = []
    island_count = 0
    for i in range(len(matrix)):
        visited.append([False] * len(matrix[0]))
    # walk through each cell in the matrix
    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            if not visited[y][x]:
                if matrix[y][x] == 1:
                    visited = dft(x, y, matrix, visited)
                    # increment counter by 1
                    island_count += 1
    return island_count

islands = [[0, 1, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 1, 0, 0], [1, 0, 1, 0, 0], [1, 1, 0, 0, 0]]

print(island_counter(islands))